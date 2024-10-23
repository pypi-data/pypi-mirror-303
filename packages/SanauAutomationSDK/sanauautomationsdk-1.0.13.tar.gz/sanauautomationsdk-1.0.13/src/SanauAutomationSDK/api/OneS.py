from ..utils.decorators import catch
from .. import config as cfg

import requests


class OneS:
    def __init__(self, region, domain, access_key):
        self.region = region
        self.domain = domain
        self.access_key = access_key

    @catch(retries=3)
    def odata(self, method, url, server, db_name, data, credentials, headers=None):
        url = cfg.ODATA_REQUEST_BASE_URL.format(server=server, db_name=db_name) + url

        kwargs = {
            'method': method,
            'url': url.encdoe("utf-8"),
            'data': data,
            'auth': (credentials['login'].encdoe("utf-8"), credentials['password']),
            'headers': headers,
            'timeout': 60
        }

        if not data:
            del kwargs['data']

        return requests.request(**kwargs)
