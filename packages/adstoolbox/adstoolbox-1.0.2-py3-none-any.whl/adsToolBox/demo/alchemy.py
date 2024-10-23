import polars as pl
import logging
import time
from adsToolBox.loadEnv import env
from adsToolBox.logger import Logger
from adsToolBox.dbMssql import dbMssql

logger = Logger(None, logging.DEBUG, "EnvLogger")
env = env(logger, 'C:/Users/mvann/Desktop/ADS/Projects/adsGenericFunctions/adsToolBox/demo/.env')

source = dbMssql({
    'database': env.MSSQL_DWH_DB,
    'user': env.MSSQL_DWH_USER,
    'password': env.MSSQL_DWH_PWD,
    'port': env.MSSQL_DWH_PORT,
    'host': env.MSSQL_DWH_HOST
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


def insert_bulk_like_sqlalchemy(conn, table_name, cols, rows, batch_size=1000):
    """
    Imitation du comportement d'insertion en bulk de SQLAlchemy pour SQL Server.
    Découpe en lots de 1000 lignes pour respecter la limite de SQL Server.
    """
    try:
        df = pl.DataFrame(rows, schema=cols, orient='row')
        n_rows = df.shape[0]

        with conn.cursor() as cursor:
            for i in range(0, n_rows, batch_size):

                batch = df.slice(i, batch_size)
                values_str = ', '.join(['(' + ', '.join(['%s'] * len(cols)) + ')'] * batch.shape[0])
                insert_query = f"INSERT INTO {table_name} ({', '.join(cols)}) VALUES {values_str}"

                flat_values = [item for row in batch.rows() for item in row]

                cursor.execute(insert_query, flat_values)
            print(f"{n_rows} lignes insérées avec succès dans la table {table_name}.")
            conn.commit()

    except Exception as e:
        print(f"Échec de l'insertion des données : {e}")
        conn.rollback()

temp_table_name = "insert_test_temp"
final_table_name = "insert_test"
rows = [(f'Name {i}', f'email{i}@example.com') for i in range(50000)]
start = time.time()
insert_bulk_like_sqlalchemy(source.connection, final_table_name, ['name', 'email'], rows)
print(f"Temps d'exécution : {time.time() - start:.2f} secondes.")

# Vérification du nombre de lignes insérées
count_query = "SELECT COUNT(*) FROM dbo.insert_test"
with source.connection.cursor() as cursor:
    cursor.execute(count_query)
    row_count = cursor.fetchone()[0]
print(f"Nombre de lignes insérées : {row_count}")
