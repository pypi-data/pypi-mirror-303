from ...Wrapper import Wrapper
from ..entities.ODataEntity import ODataEntity
from ....classes.OneSApiCredentials import OneSApiCredentials
from ....exceptions.odata import *
from ....utils.logutils import logger

import requests
import json
import time


class ODataHandler:

    def __init__(self, odata_entity: ODataEntity, api_wrapper: Wrapper, credentials: OneSApiCredentials):
        self.odata_entity = odata_entity
        self.api_wrapper = api_wrapper
        self.credentials = credentials

    def odata_request(self, method, guid=None, data=None, params=None, json=True, approve=False, raw_query=None):
        url = self.odata_entity.url.format(prefix=self.odata_entity.PREFIX_NAME,
                                     obj=self.odata_entity.OBJECT_CONFIG_NAME,
                                     guid="(guid'{}')".format(guid) if guid else "",
                                     raw_query=raw_query if raw_query else "",
                                     sep="?" if json or params else "",
                                     params=params if params else "",
                                     format="&$format=json" if json else "",
                                     post="/Post()" if approve else "")
        print("url", method, url)

        try:
            return self.api_wrapper.odata(method=method, url=url, server=self.odata_entity.server,
                                          db_name=self.odata_entity.database_name, data=data,
                                          credentials={'login': self.credentials.login, 'password': self.credentials.password})
        except requests.exceptions.Timeout:
            logger.error(f"Retrying process: max retries reacher, db - {self.odata_entity.database_name}")
            raise ODataTimeOutError("Max retries reached")

    def create(self, **kwargs):
        try:
            return self.odata_request("POST", data=json.dumps(kwargs)).json()
        except Exception as e:
            return {"status": str(e)}

    def all(self, **kwargs):
        response = self.odata_request("GET", **kwargs)

        if response.status_code == 408:
            time.sleep(20)
            self.all(**kwargs)

        try:
            return self._get_data(response)
        except Exception as e:
            raise e

    def filter_by(self, **kwargs):
        response = self.odata_request("GET", params=kwargs)

        try:
            return self._get_data(response)
        except Exception as e:
            raise e

    def _get_data(self, response):
        try:
            data = response.json()
            if 'odata.error' in data:
                raise ODataError(data['odata.error']['message']['value'])
            if 'value' in data:
                return data['value']
            else:
                raise ODataError(f"Ключ 'value' не найден в полученном ответе от 1С: {json.dumps(data)}")

        except json.decoder.JSONDecodeError:
            if response.status_code == 404:
                raise ODataNotFoundError(url=f"http://{self.odata_entity.server}/{self.odata_entity.database_name}/odata/standard.odata/")

            if response.status_code == 401:
                raise ODataAuthenticationError(self.credentials.login)

        raise ODataUnknownError(f"Неизвестная ошибка ({response.status_code} - {response.text})")

    def find_by_ref_key(self, ref_key):
        result = self.filter_by(params=f"$filter=Ref_Key eq guid'{ref_key}'")
        return result[0] if result else None

    def find_by_individual_key(self, individual_key):
        result = self.filter_by(params=f"$filter=ФизЛицо_Key eq guid'{individual_key}'")
        return result[0] if result else None

    def get_keys(self, value_name=None):
        return {key[value_name or 'Description']: key['Ref_Key'] for key in self.filter_by(method="GET")}

    def get_information_register_data(self, individual_key):
        individual_attribute_name = 'Физлицо_Key' if self.odata_entity.OBJECT_CONFIG_NAME == "СведенияОбИнвалидностиФизлиц" else 'ФизЛицо_Key'

        try:
            result = [item for item in self.all() if item[individual_attribute_name] == individual_key]
            return result[0] if result else None
        except KeyError:
            return None
        except IndexError:
            return None
        except Exception as e:
            return {"status": str(e)}

    @staticmethod
    def get_patch_url(object_ref_key, object_type, contact_specify, contact_type_ref_key, contact_type):
        return f"(Объект='{object_ref_key}', Объект_Type='{object_type}', Тип='{contact_specify}'," \
               f" Вид='{contact_type_ref_key}', Вид_Type='{contact_type}')?$format=json"

    def exists(self, guid):
        response = self.odata_request("GET", guid=str(guid))

        try:
            if self._get_data(response):
                return True
        except ODataError as odata_error:
            if "odata entity is not found" in odata_error.message:
                return False
        except Exception as e:
            raise e

    def approve(self, guid):
        try:
            return self.odata_request("POST", guid=str(guid), json=False, approve=True)
        except Exception as e:
            return {'status': str(e)}
