from playhouse.postgres_ext import *
from .BaseModel import BaseModel
from datetime import datetime, timezone


class Test(BaseModel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        table_name = 'tests'

    id = PrimaryKeyField()
    name = CharField()
    is_active = BooleanField(default=True)
    created_at = DateTimeField(default=datetime.now(timezone.utc))
    updated_at = DateTimeField(default=datetime.now(timezone.utc))
