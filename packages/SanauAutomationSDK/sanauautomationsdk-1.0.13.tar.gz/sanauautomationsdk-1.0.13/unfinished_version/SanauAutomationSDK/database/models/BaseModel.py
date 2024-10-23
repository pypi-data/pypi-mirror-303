from playhouse.postgres_ext import *


class BaseModel(Model):

    def __init__(self, *args, **kwargs):
        db = kwargs.pop('db', None)
        if db:
            self._meta.database = db
        super().__init__(*args, **kwargs)

    class Meta:
        database = None
