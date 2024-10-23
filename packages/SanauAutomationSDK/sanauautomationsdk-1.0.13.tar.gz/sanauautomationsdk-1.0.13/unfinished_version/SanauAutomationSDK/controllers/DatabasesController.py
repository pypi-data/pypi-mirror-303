from .BaseController import BaseController
from ..database.models.Database import Database


class DatabasesController(BaseController):

    def __init__(self, db):
        super().__init__(model=Database(db=db))
