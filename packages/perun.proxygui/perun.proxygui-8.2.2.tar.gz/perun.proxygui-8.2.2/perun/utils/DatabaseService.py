from perun.connector import Logger
from pymongo import MongoClient
from pymongo.collection import Collection
from sqlalchemy import Engine, create_engine, Table, MetaData, inspect


class DatabaseService:
    def __init__(self, cfg):
        self.__CFG = cfg
        self.logger = Logger.get_logger(__name__)

    def get_mongo_db_collection(self, cfg_db_name: str) -> Collection:
        client = MongoClient(self.__CFG[cfg_db_name]["connection_string"])
        database_name = self.__CFG[cfg_db_name]["database_name"]
        collection_name = self.__CFG[cfg_db_name]["collection_name"]

        return client[database_name][collection_name]

    def get_postgres_engine(self, db_config_name) -> Engine:
        """Prepares postgres engine"""
        if db_config_name == "mitre_database":
            connection_string = self.__CFG["user_manager"][db_config_name][
                "connection_string"
            ]
        else:
            connection_string = self.__CFG[db_config_name]["connection_string"]
        engine = create_engine(connection_string)

        return engine

    def get_postgres_table(self, engine, table_name) -> Table:
        """Retrieves table from postgres db"""
        metadata = MetaData()
        metadata.reflect(engine)

        inspector = inspect(engine)
        if table_name not in inspector.get_table_names():
            self.logger.error("Table '{}' does not exist".format(table_name))
            raise Exception("Invalid configuration.")
        return Table(table_name, metadata, autoload=True)
