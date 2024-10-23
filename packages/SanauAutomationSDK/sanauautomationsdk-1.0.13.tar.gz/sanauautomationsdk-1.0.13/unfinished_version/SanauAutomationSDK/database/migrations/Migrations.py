from src.SanauAutomationSDK.database.models.Test import Test


class Migrations:
    def __init__(self, db):
        self.db = db

    def create_tables(self):
        self.db.create_tables([Test(db=self.db)])
        pass
