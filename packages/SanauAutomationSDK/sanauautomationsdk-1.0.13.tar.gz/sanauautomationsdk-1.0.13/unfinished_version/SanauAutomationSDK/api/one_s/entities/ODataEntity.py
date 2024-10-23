class ODataEntity:
    PREFIX_NAME = ""
    OBJECT_CONFIG_NAME = ""
    url = "{prefix}_{obj}{raw_query}{guid}{sep}{params}{format}{post}"

    def __init__(self, database_name, server):
        self.database_name = database_name
        self.server = server
