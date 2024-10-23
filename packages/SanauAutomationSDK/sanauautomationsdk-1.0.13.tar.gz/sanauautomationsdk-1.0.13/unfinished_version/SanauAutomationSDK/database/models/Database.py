from .BaseModel import BaseModel
from playhouse.postgres_ext import *
from datetime import datetime, timezone


class Database(BaseModel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        table_name = 'databases'

    id = IntegerField(primary_key=True)
    name = CharField()
    configuration = CharField()
    server = CharField()
    entity_id = IntegerField()
    sync_period = IntervalField()
    created_at = DateTimeField(default=datetime.now(timezone.utc))
