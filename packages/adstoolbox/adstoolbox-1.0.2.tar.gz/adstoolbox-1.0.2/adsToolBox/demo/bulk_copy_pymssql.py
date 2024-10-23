from adsToolBox.loadEnv import env
from adsToolBox.logger import Logger
from adsToolBox.dbMssql import dbMssql

import logging
import time

logger = Logger(None, logging.DEBUG, "EnvLogger")
env = env(logger, 'C:/Users/mvann/Desktop/ADS/Projects/adsGenericFunctions/adsToolBox/demo/.env')

source = dbMssql({
    'database': env.MSSQL_DWH_DB,
    'user': env.MSSQL_DWH_USER,
    'password': env.MSSQL_DWH_PWD,
    'port': env.MSSQL_DWH_PORT_VPN,
    'host': env.MSSQL_DWH_HOST_VPN
}, logger)

source.connect()

# Création de la table si elle n'existe pas
source.sqlExec('''
IF OBJECT_ID('dbo.insert_test', 'U') IS NOT NULL 
    DROP TABLE dbo.insert_test;

CREATE TABLE dbo.insert_test (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)
);
''')

rows = [(f'Name {i}', f'email{i}@example.com') for i in range(50_000)]

def insert_bulk(source, table, cols_ids, rows):
    start = time.time()
    source.insertBulk(table, cols_ids, rows)
    print(f"Ancienne méthode - Temps d'exécution: {time.time() - start} secondes")

insert_bulk(source, "dbo.insert_test", [2, 3], rows)