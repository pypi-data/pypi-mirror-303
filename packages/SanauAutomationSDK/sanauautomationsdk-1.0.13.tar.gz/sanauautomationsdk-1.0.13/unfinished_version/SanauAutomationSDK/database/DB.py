from src.SanauAutomationSDK.database.migrations.Migrations import Migrations
from playhouse.postgres_ext import *


class DB:

    def __init__(self, db_name, user, password, host, port):
        self.db = PostgresqlExtDatabase(db_name, user=user, password=password, host=host, port=port)
        self.db.connect()

    def close_connection(self):
        self.db.close()

    def create_missing_tables(self):
        Migrations(self.db).create_tables()
