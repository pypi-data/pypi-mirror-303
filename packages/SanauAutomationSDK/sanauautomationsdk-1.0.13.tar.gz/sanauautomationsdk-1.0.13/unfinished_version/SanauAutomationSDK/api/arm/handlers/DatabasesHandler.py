from ...Wrapper import Wrapper
from ....utils.logutils import logger


class DatabasesHandler:

    def __init__(self, api_wrapper: Wrapper):
        self.api_wrapper = api_wrapper

    def get_1c_databases(self):
        try:
            response = self.api_wrapper.get_databases()
            return response
        except Exception as e:
            logger.error(f"Не удается выгрузить базы из АРМа с ошибкой: {e}")
            return []

    def get_1c_database(self, database):
        try:
            response = self.api_wrapper.get_database(database=database)
            return response
        except Exception as e:
            logger.error(f"Не удается выгрузить базу {database} из АРМа с ошибкой: {e}")
            return []
