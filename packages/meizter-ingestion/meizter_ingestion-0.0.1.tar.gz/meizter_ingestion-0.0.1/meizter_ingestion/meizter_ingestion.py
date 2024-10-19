# Importações
import daft
import pyarrow as pa
from pyarrow import flight
import requests
from IPython.core.magic import (Magics, magics_class, cell_magic)
import os
from dotenv import load_dotenv
import pandas as pd
import requests
import pyarrow.fs as fs
import pyarrow.parquet as pq
# Classe de segredos
class secret:
    @staticmethod
    def get_secrets(keys):
        load_dotenv()
        service_token = os.getenv('AWS')
        url = "https://api.doppler.com/v3/configs/config/secrets/download?format=json"

        headers = {
            "Authorization": f"Bearer {service_token}"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            secrets = response.json()

            selected_secrets = {key: secrets.get(key) for key in keys if key in secrets}
            return selected_secrets
        else:
            print(f"Erro ao buscar segredos: {response.status_code}, {response.text}")
            return None

# Executor de consultas no Dremio
class DremioQueryExecutor:
    def __init__(self):
        secrets = secret.get_secrets(["LOGIN_ENDPOINT", "GRPC_ENDPOINT", "USER_DREMIO", "PASS_DREMIO"])
        if secrets:
            self.login_endpoint = secrets.get("LOGIN_ENDPOINT")
            self.grpc_endpoint = secrets.get("GRPC_ENDPOINT")
            self.username = secrets.get("USER_DREMIO")
            self.password = secrets.get("PASS_DREMIO")
            self.token = self._get_token()
            self.client = self._connect_to_dremio()
            self.options = self._get_flight_options()
            self.query = "" 
        else:
            raise Exception("Erro ao buscar segredos. Não foi possível inicializar o DremioQueryExecutor.")
    
    def _get_token(self):
        payload = {
            "userName": self.username,
            "password": self.password
        }
        response = requests.post(self.login_endpoint, json=payload)
        if response.status_code == 200:
            return response.json().get("token", "")
        else:
            raise Exception(f"Falha ao obter o token. Status code: {response.status_code}")

    def _connect_to_dremio(self):
        return flight.FlightClient(self.grpc_endpoint)

    def _get_flight_options(self):
        headers = [(b'authorization', f'Bearer {self.token}'.encode('utf-8'))]
        return flight.FlightCallOptions(headers=headers)

    def execute_query(self, query):
        self.query = query
        try:
            descriptor = flight.FlightDescriptor.for_command(query)
            flight_info = self.client.get_flight_info(descriptor, self.options)
            reader = self.client.do_get(flight_info.endpoints[0].ticket, self.options)

            batches = []
            for batch in reader:
                record_batch = batch.data
                arrow_table = pa.Table.from_batches([record_batch])
                daft_df = daft.from_arrow(arrow_table)
                batches.append(daft_df)

            df_final = batches[0]
            for df in batches[1:]:
                df_final = df_final.append(df)
            
            return df_final
        
        except flight.FlightUnavailableError as e:
            print("Erro: Não foi possível conectar ao servidor Dremio.")
            print(f"Detalhes do erro: {e}")
        except pa.ArrowInvalid as e:
            print("Erro de SQL: Verifique sua query SQL.")
            error_message = str(e)
            if "SQL Query" in error_message:
                query_error = error_message.split("SQL Query")[-1].strip()
                print(f"Erro encontrado na query: {query_error}")
            else:
                print(f"Detalhes do erro: {error_message}")
        except Exception as e:
            print("Erro inesperado:")
            print(f"Detalhes do erro: {e}")

    def query_to_df(self, sql_query):
        """Permite execução de query passando a SQL diretamente em uma string"""
        return self.execute_query(sql_query)

# Classe para Ingestão de Dados no Dremio
class mzr_ingestion_dremio:
    def __init__(self, catalogo, source, table):
        self.executor = DremioQueryExecutor()
        secrets = secret.get_secrets(["BUCKET_GLOBAL", "CATALOG"])
        self.lake = secrets.get("CATALOG")
        self.bucket_global = secrets.get("BUCKET_GLOBAL")
        self.catalogo = catalogo
        self.source = source
        self.table = table

    def bronze_select(self):
        df = self.executor.query_to_df(
            f'''
            SELECT
                * ,
                TO_CHAR(CURRENT_DATE, 'yyyy-MM-dd') AS dt_ingestion
            from s3."{self.bucket_global}".transient.{self.catalogo}.{self.source}."{self.table}"."{self.table}.parquet"
            '''
        )
        return df

    def bronze_overwrite(self):
        self.executor.query_to_df(
            f'''
            CREATE TABLE IF NOT EXISTS {self.lake}.{self.catalogo}.{self.source}.bronze.{self.table} 
            AS
            SELECT
                *,
                TO_CHAR(CURRENT_DATE, 'yyyy-MM-dd') AS dt_ingestion
            FROM s3."{self.bucket_global}".transient.{self.catalogo}.{self.source}."{self.table}"."{self.table}.parquet";
            '''
        )
        self.executor.query_to_df(
            f'''
            TRUNCATE TABLE {self.lake}.{self.catalogo}.{self.source}.bronze.{self.table};
            '''
        )
        self.executor.query_to_df(
            f'''
            INSERT INTO {self.lake}.{self.catalogo}.{self.source}.bronze.{self.table}
            SELECT
                *,
                TO_CHAR(CURRENT_DATE, 'yyyy-MM-dd') AS dt_ingestion
            FROM s3."{self.bucket_global}".transient.{self.catalogo}.{self.source}."{self.table}"."{self.table}.parquet";
            '''
        )        
        self.clean_transient()
        return print(f"Full Load: {self.lake}.{self.catalogo}.{self.source}.bronze.{self.table} foi finalizado com Sucesso! ")
    
    def bronze_incremental(self):
        df = self.executor.query_to_df(
            f'''
            INSERT INTO {self.lake}.{self.catalogo}.{self.source}.bronze.{self.table}
            SELECT
                *,
                TO_CHAR(CURRENT_DATE, 'yyyy-MM-dd') AS dt_ingestion
            from s3."{self.bucket_global}".transient.{self.catalogo}.{self.source}."{self.table}"."{self.table}.parquet"
            '''
        )
        self.clean_transient()
        return df

    def drop_table(self, schema):
        df = self.executor.query_to_df(
            f'''
            DROP TABLE {self.lake}.{self.catalogo}.{self.source}.{schema}.{self.table}
            '''
        )
        return df

    def optimize(self, schema):
        self.executor.query_to_df(
            f'''
            OPTIMIZE TABLE {self.lake}.{self.catalogo}.{self.source}.{schema}.{self.table}
            '''
        )
        print(f"OPTIMIZE na {self.lake}.{self.catalogo}.{self.source}.{schema}.{self.table}")
    
    def clean_transient(self):
        df = self.executor.query_to_df(
            f'''
            DROP TABLE s3."{self.bucket_global}".transient.{self.catalogo}.{self.source}."{self.table}"."{self.table}.parquet"
            '''
        )
        
        return df

# Classe de Magic Function para Jupyter
@magics_class
class sqlmagic(Magics):
    def __init__(self, shell):
        super().__init__(shell)
        self.executor = DremioQueryExecutor()  # Instancia o DremioQueryExecutor aqui

    @cell_magic
    def sql(self, line, cell):
        var_name = line.strip()
        query = cell.strip()
        df = self.executor.execute_query(query)
        self.shell.user_ns[var_name] = df
        display(df)

    @staticmethod
    def activate():
        """Método para registrar a magic function e inicializar o executor"""
        ip = get_ipython()
        ip.register_magics(sqlmagic(ip))  # Passa o shell diretamente

class mzr_ingestion_transient:

    def __init__(self, catalog, source, table):
        secrets = secret.get_secrets(["ACCESS_KEY", "SECRET_KEY", "REGION", "BUCKET_TRANSIENT"])
        self.access_key = secrets.get("ACCESS_KEY")
        self.access_secret_key = secrets.get("SECRET_KEY")
        self.bucket_transient = secrets.get("BUCKET_TRANSIENT")
        self.region = secrets.get("REGION")
        self.catalog = catalog
        self.source = source
        self.table = table


    def conn_s3(self):
        s3 = fs.S3FileSystem(
        access_key=self.access_key,
        secret_key=self.access_secret_key,
        region=self.region
        )
        return s3

    def to_transient(self, df):
        s3 = self.conn_s3()
        df = df.to_arrow()
        if not df:
            print('O arquivo DF está vázio!!')
            return
        
        catalogo = f'{self.catalog}/{self.source}/{self.table}/{self.table}.parquet'
        bucket = self.bucket_transient
        caminho_s3 = f"{bucket}/{catalogo}"

        if not catalogo.strip(): 
            print('Caminho incorreto, verificar informações')
            return

        try:
            pq.write_table(df, caminho_s3, filesystem=s3)
            print(f'Dados escritos com sucesso em: {caminho_s3}')
        except Exception as e:
             print(f'Erro ao escrever no S3: {e}')