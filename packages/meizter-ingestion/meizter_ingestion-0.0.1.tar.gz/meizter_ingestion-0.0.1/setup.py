from setuptools import setup

setup(
    name='meizter_ingestion',
    version='0.0.1',
    packages=['meizter_ingestion'], 
    install_requires=[
        'getdaft==0.3.4',     
        'pyarrow==17.0.0',    
        'requests==2.32.3',   
        'ipython',            
        'python-dotenv',      
        'pandas==2.2.3',      
        'numpy==2.1.1',       
        'fsspec==2023.12.2',  
        's3fs==2023.12.2'     
    ],
    license='MIT License',
    author='Douglas Borges Martins',
    author_email="douglas@meizter.com",
    description='pacote para manipulação do Dremio',
)
