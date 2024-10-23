from .ODataEntity import ODataEntity


class User(ODataEntity):
    PREFIX_NAME = "Catalog"
    OBJECT_CONFIG_NAME = "Пользователи"

    def __init__(self, database_name, server):
        super().__init__(database_name, server)