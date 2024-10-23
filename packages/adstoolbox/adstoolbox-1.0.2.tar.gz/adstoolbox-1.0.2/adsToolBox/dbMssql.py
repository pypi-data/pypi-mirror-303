from datetime import datetime
import pymssql
import timeit
import polars as pl
from .timer import timer, get_timer
from .dataFactory import data_factory

class dbMssql(data_factory):
    def __init__(self, dictionnary: dict, logger, batch_size=10_000):
        """
        instancie la classe dbMssql, qui hérite de dataFactory
        :param dictionnary: Un dictionnaire contenant tous les paramètres nécéssaires pour lancer une connexion sql server
        :param logger: un logger ads qui va gérer les logs des actions de la classe
        :param batch_size: la taille des batchs en lecture et écriture
        """
        self.connection = None
        self.logger = logger
        self.__database = dictionnary['database']
        self.__user = dictionnary['user']
        self.__password = dictionnary['password']
        self.__port = dictionnary['port']
        self.__host = dictionnary['host']
        self.__batch_size = batch_size

    @timer
    def connect(self):
        """
        lance la connexion avec les identifiants passés à l'initialisation de la classe
        toutes les méthodes de la classe nécéssitent une connexion active
        :return: la connexion
        """
        if self.logger is not None: self.logger.info("Tentative de connexion avec la base de données.")
        try:
            self.connection = pymssql.connect(
                server=f"{self.__host}:{self.__port}",
                user=self.__user,
                password=self.__password,
                database=self.__database
            )
            if self.logger is not None: self.logger.info(f"Connexion établie avec la base de données.")
            return self.connection
        except Exception as e:
            if self.logger is not None: self.logger.error(f"Échec de la connexion à la base de données: {e}")
            raise

    def sqlQuery(self, query):
        """
        lit la base de données avec la requête query
        :param query: la requête
        :return: les données lues avec yield
        """
        self.logger.debug(f"Exécution de la requête de lecture : {query}")
        start_time = datetime.now()
        try:
            timer_start = timeit.default_timer()
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                cols = [desc[0] for desc in cursor.description]
                self.logger.info("Requête exécutée avec succès, début de la lecture des résultats.")
                while True:
                    rows = cursor.fetchmany(self.__batch_size)
                    if not rows:
                        break
                    yield rows
                    self.logger.info(f"{len(rows)} lignes lues.")
            end_time = datetime.now()
            self.logger.log_to_db(start_time, end_time, status='success', message="Requête de lecture exécutée.")
            if get_timer():
                elapsed_time = timeit.default_timer() - timer_start
                self.logger.info(f"Temps d'exécution de sqlQuery: {elapsed_time:.4f} secondes")
        except Exception as e:
            end_time = datetime.now()
            self.logger.error(f"Échec de la lecture des données: {e}")
            self.logger.log_to_db(start_time, end_time, status="failure", message=str(e))
            raise

    @timer
    def sqlExec(self, query):
        """
        execute une requête sur la base de données, un create ou delete table par exemple
        :param query: la requête
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                self.logger.info(f"Requête exécutée avec succès.")
                self.connection.commit()
        except Exception as e:
            self.logger.error(f"Échec de l'exécution de la requête: {e}")
            raise

    @timer
    def sqlScalaire(self, query):
        """
        execute une requête et retourne le premier résultat
        :param query: la requête
        :return: le résultat de la requête
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                self.logger.info(f"Requête exécutée avec succès.")
                data = cursor.fetchone()
                return data
        except Exception as e:
            self.logger.error(f"Échec de l'exécution de la requête: {e}")
            raise


    @timer
    def insert(self, table, cols=[], row=[]):
        """
        insère des données dans la base de données
        :param table: nom de la table dans laquelle insérer
        :param cols: liste des colonnes dans lesquelles insérer
        :param row: liste des valeurs à insérer
        :return: le résultat de l'opération, l'erreur et la la ligne concernée en cas d'erreur
        """
        start_time = datetime.now()
        try:
            with self.connection.cursor() as cursor:
                placeholders = ", ".join(["%s"] * len(cols))
                query = f"INSERT INTO {table} ({', '.join(cols)}) VALUES ({placeholders})"
                cursor.execute(query, row)
                self.connection.commit()
                self.logger.info(f"{cursor.rowcount} lignes insérées avec succès dans la table {table}.")
                self.logger.log_to_db(start_time, datetime.now(), status='success', message="Insertion réussie.")
                return ["SUCCESS"]
        except Exception as e:
            self.logger.error(f"Échec de l'insertion des données: {e}")
            self.logger.log_to_db(start_time, datetime.now(), status='failure', message=str(e))
            self.connection.rollback()
            return "ERROR", str(e), row

    @timer
    def insertMany(self, table, cols=[], rows=[]):
        """
        similaire à insert classique, mais insère par batch de taille 'batch_size', avec executemany
        :param table: nom de la table dans laquelle insérer
        :param cols: liste des colonnes dans lesquelles insérer
        :param rows: liste des lignes à insérer
        :return: le résultat de l'opération, l'erreur et la le batch concerné en cas d'erreur
        """
        start_time = datetime.now()
        try:
            with self.connection.cursor() as cursor:
                placeholders = ", ".join(["%s"] * len(cols))
                query = f"INSERT INTO {table} ({', '.join(cols)}) VALUES ({placeholders})"
                cursor.executemany(query, rows)
                self.connection.commit()
                self.logger.info(f"{cursor.rowcount} lignes insérées avec succès dans la table {table}.")
                self.logger.log_to_db(start_time, datetime.now(), status='success', message="Insertion réussie.")
                return ["SUCCESS"]
        except Exception as e:
            self.logger.error(f"Échec de l'insertion des données: {e}")
            self.logger.log_to_db(start_time, datetime.now(), status='failure', message=str(e))
            self.connection.rollback()
            return "ERROR", str(e), rows

    @timer
    def insertBulk(self, table, cols=[], rows=[]):
        """
        similaire à insertMany, mais utilise bulk_copy, bien plus rapide
        :param table: nom de la table dans laquelle insérer
        :param cols: liste des colonnes dans lesquelles insérer
        :param rows: liste des lignes à insérer
        :return: le résultat de l'opération, l'erreur et la le batch concerné en cas d'erreur
        """
        start_time = datetime.now()
        try:
            if isinstance(rows, list):
                df = pl.DataFrame(rows, orient='row')
            elif isinstance(rows, pl.DataFrame):
                df = rows
            else:
                raise ValueError("Les données doivent être une liste de tuples ou un DataFrame Polars")
            data = [tuple(row) for row in df.iter_rows(named=False)]
            with self.connection.cursor() as cursor:
                self.connection.bulk_copy(
                    table_name=table,
                    elements=data,
                    column_ids=cols,
                    batch_size=self.__batch_size
                )
                self.connection.commit()
            self.logger.info(f"{len(data)} ligne(s) insérée(s) avec succès dans la table {table}.")
            self.logger.log_to_db(start_time, datetime.now(), status="success", message="Insertion(s) réussie(s)")
            return ["SUCCESS"]
        except Exception as e:
            self.logger.error(f"Échec de l'insertion des données: {e}")
            self.logger.log_to_db(start_time, datetime.now(), status='failure', message=str(e))
            self.connection.rollback()
            return "ERROR", str(e), rows