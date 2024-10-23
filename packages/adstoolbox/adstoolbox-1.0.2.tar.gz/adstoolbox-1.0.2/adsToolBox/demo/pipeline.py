from faker import Faker
import logging
from adsToolBox.loadEnv import env
from adsToolBox.dbPgsql import dbPgsql
from adsToolBox.dbMssql import dbMssql
from adsToolBox.pipeline import pipeline
from adsToolBox.logger import Logger
from adsToolBox.global_config import set_timer

logger = Logger(None, logging.DEBUG, "EnvLogger")
env = env(logger, 'C:/Users/mvann/Desktop/ADS/Projects/adsGenericFunctions/adsToolBox/demo/.env')

logger_connection = dbPgsql({'database': env.PG_DWH_DB
                          , 'user': env.PG_DWH_USER
                          , 'password': env.PG_DWH_PWD
                          , 'port': env.PG_DWH_PORT
                          , 'host': env.PG_DWH_HOST},
                      None)
logger_connection.connect()
logger = Logger(logger_connection, logging.INFO, "AdsLogger", "LOGS",
                    "LOGS_details")
set_timer(True)

# Déclarons une source base de données
source = dbPgsql({'database':env.PG_DWH_DB
                    , 'user':env.PG_DWH_USER
                    , 'password':env.PG_DWH_PWD
                    , 'port':env.PG_DWH_PORT
                    , 'host':env.PG_DWH_HOST}
                    ,logger)

# Déclarer une destination
destination = {
    'name': 'test',
    'db': dbMssql({'database':env.MSSQL_DWH_DB, 'user':env.MSSQL_DWH_USER,
                   'password':env.MSSQL_DWH_PWD, 'port':env.MSSQL_DWH_PORT_VPN
                    , 'host':env.MSSQL_DWH_HOST_VPN}, logger),
    'table': 'insert_test_2',
    'cols': [2, 3]
}
destination["db"].connect()
destination["db"].sqlExec('''
IF OBJECT_ID('dbo.insert_test_2', 'U') IS NOT NULL 
    DROP TABLE dbo.insert_test_2;

CREATE TABLE dbo.insert_test_2 (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)
);
''')

# Voici la requête pour la source (lecture des données)
query = '''
SELECT name, email FROM insert_test;
'''

# Déclaration du pipeline
pipe = pipeline({
    'db_source': source, # La source du pipeline
    'query_source': query, # La requête qui sera exécutée sur cette source
    'db_destination': destination, # La destination du pipeline
    'mode': 'bulk'
}, logger)

rejects = pipe.run() # pipeline.run() renvoie les rejets du pipeline, ce sera une liste vide s'il n'y en a pas
#print(f"Rejets : {rejects}")

# Les deux batch_size sont à 1, chaque ligne sera inséré une par une, ce sera lent, mais les rejets seront des batchs
# de 1 ligne.

logger.info("Fin de la démonstration")