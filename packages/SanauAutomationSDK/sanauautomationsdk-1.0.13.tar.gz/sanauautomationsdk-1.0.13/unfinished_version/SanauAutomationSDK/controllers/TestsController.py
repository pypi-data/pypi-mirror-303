from src.SanauAutomationSDK.controllers.BaseController import BaseController
from src.SanauAutomationSDK.database.models.Test import Test


class TestsController(BaseController):

    def __init__(self, db):
        super().__init__(model=Test(db=db))
