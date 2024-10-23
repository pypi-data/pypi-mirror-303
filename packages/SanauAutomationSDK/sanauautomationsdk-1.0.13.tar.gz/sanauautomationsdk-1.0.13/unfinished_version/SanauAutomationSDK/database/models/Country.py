from .BaseModel import BaseModel
from playhouse.postgres_ext import *
from datetime import datetime, timezone
from .Database import Database


class Country(BaseModel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        table_name = 'countries'

    id = IntegerField(primary_key=True)
    database_id = ForeignKeyField(Database, backref='countries')
    ref_key = UUIDField()
    name = CharField(max_length=50)
    second_alpha_code = CharField(max_length=10)
    created_at = DateTimeField(default=datetime.now(timezone.utc))
    updated_at = DateTimeField(default=datetime.now(timezone.utc))
