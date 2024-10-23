from ...Wrapper import Wrapper
from ..models.DB1C import DB1C
from ...one_s.handlers.ODataHandler import ODataHandler
from ....utils.logutils import logger
from .AlertsHandler import AlertsHandler
from ....exceptions.odata import *
from ...one_s.handlers.UsersHandler import UsersHandler
from ....classes.OneSApiCredentials import OneSApiCredentials

from dateutil.relativedelta import relativedelta
from datetime import datetime, date


class DB1CHandler:

    def __init__(self, api_wrapper: Wrapper, odata_credentials: OneSApiCredentials):
        self.api_wrapper = api_wrapper
        self.odata_credentials = odata_credentials

    def get_database(self, database_name, start_at=None, end_at=None, sync=True, period=1) -> DB1C or False:
        database = self.api_wrapper.get_database(name=database_name)

        if 'configuration' not in database or database['configuration'] != "Бухгалтерия":
            return False

        return DB1C(database=database, sync={'start_at': start_at, 'end_at': end_at, 'sync': sync, 'period': period})

    def fetch(self, database_names=None, start_at=None, end_at=None, sync=True, period=1) -> list[DB1C]:
        output = []
        all_databases = self.api_wrapper.get_databases()

        # TODO: Разобраться с этой строчкой, почему 'INSIDE_NETWORK' нет в .env
        # if os.getenv('INSIDE_NETWORK') and (db['server'] == "192.168.88.100"):
        #     server = "5.188.65.184:8999"

        for db in all_databases:
            if 'configuration' not in db or db['configuration'] != "Бухгалтерия":
                continue

            if (database_names is not None) and (db['name'] in database_names):
                continue
            output.append(DB1C(database=db,  sync={'start_at': start_at, 'end_at': end_at, 'sync': sync, 'period': period}))

        return output

    def fetch_items(self, cls, db1c: DB1C, from_date=None, to_date=None, order_key="Ref_Key"):
        filters = []
        page_size = 1000
        offset = 0

        if from_date:
            filters.append(f"Date ge datetime'{from_date}T00:00:00'")

        if to_date:
            filters.append(f"Date le datetime'{to_date}T23:59:59'")

        while True:
            params = "{filter}&{orderby}&{top}&{skip}".format(
                filter=f"$filter={' and '.join(filters)}",
                top=f"$top={page_size}",
                skip=f"$skip={offset}",
                orderby=f"$orderby={order_key} desc"
            )

            result = cls(database_name=db1c.path, server=db1c.server).all(params=params)
            for item in result:
                yield item

            if len(result) == 1000:
                offset += page_size
            else:
                break

    def fetch_items_using_monthly_pagination(self, cls, db1c: DB1C, from_date, to_date):

        cursor = from_date
        new_cursor = cursor.replace(day=1) + relativedelta(months=1)

        while True:
            filters = [
                f"Date ge datetime'{cursor}T00:00:00'",
                f"Date le datetime'{new_cursor}T00:00:00'"
            ]
            params = f"$filter={' and '.join(filters)}"

            result = cls(database_name=db1c.path, server=db1c.server).all(params=params)
            for item in result:
                yield item

            if new_cursor > to_date:
                break

    # @property TODO: Проверить нужен декоратор или нет
    def get_sync_range(self, db1c: DB1C) -> tuple[date, date]:
        start = datetime.strptime(db1c.db_entity['entity']['entry_date'], '%Y-%m-%dT%H:%M:%SZ').date()
        end = datetime.now().date()
        return start, end

    def check_connection(self, db1c) -> dict:
        logger.info(f"Checking connection with {db1c.path}")

        try:
            message = "Успешная проверка базы"

            UsersHandler(api_wrapper=self.api_wrapper, credentials=self.odata_credentials, database_name=db1c.path, server=db1c.server).all()
            AlertsHandler(api_wrapper=self.api_wrapper).resolve_alert(db1c.entity_id, "one_s_database_presence")
            return {'db1c': db1c,
                    'message': message,
                    'status': True}

        except ODataError as e:
            message = "Не настроена внешняя обработка"
            db1c.connection_error = e
            AlertsHandler(api_wrapper=self.api_wrapper).create_alert(db1c.entity_id, "one_s_database_presence", message, severity=200)
            logger.error(f"{message}: {e}")
            return {'db1c': db1c,
                    'message': message,
                    'status': False}

        except Exception as e:
            message = f"Не удалось подключиться к базе 1С: {e}"
            db1c.connection_error = e
            AlertsHandler(api_wrapper=self.api_wrapper).create_alert(db1c.entity_id, "one_s_database_presence", message, severity=200)
            logger.error(f"{message}: {e}")
            return {'db1c': db1c,
                    'message': message,
                    'status': False}
