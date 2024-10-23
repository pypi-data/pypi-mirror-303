from ..utils.decorators import catch
from .. import config as cfg

import json
import requests
import urllib.request


class Arm:
    def __init__(self, region, domain, access_key):
        self.region = region
        self.domain = domain
        self.access_key = access_key

    #################### Central apis ####################

    @catch()
    def get_currency_rates(self, currency_date, headers=None):
        return urllib.request.urlopen(url=cfg.NATIONAL_BANK.format(currency_date=currency_date))

    @catch()
    def get_domains(self, headers=None):
        return requests.get(url=cfg.DOMAINS, headers=headers).json()['domains']


    #################### Partner apis ####################

    @catch()
    def get_databases(self, headers=None):
        return requests.get(url=cfg.ONE_S_DATABASES.format(domain=self.domain), headers=headers).json()

    @catch()
    def get_database(self, name, headers=None):
        return requests.get(url=cfg.ONE_S_DATABASE.format(domain=self.domain, database=name), headers=headers).json()

    @catch()
    def get_my_new_tasks(self, headers=None):
        return requests.get(url=cfg.MY_NEW_TASKS.format(domain=self.domain), headers=headers).json()

    @catch()
    def get_last_new_task(self, headers=None):
        return requests.get(url=cfg.LAST_NEW_TASK.format(domain=self.domain), headers=headers).json()

    @catch()
    def get_tasks(self, headers=None):
        return requests.get(url=cfg.TASKS.format(domain=self.domain), headers=headers).json()

    @catch()
    def get_tasks_by_status(self, status, headers=None):
        return requests.get(url=cfg.TASKS_WITH_STATUS.format(domain=self.domain, status=status), headers=headers).json()

    @catch()
    def update_task_status(self, task_id, params, headers=None):
        return requests.put(url=cfg.UPDATE_TASK_STATUS.format(domain=self.domain, task_id=task_id), params=params, headers=headers).json()

    @catch()
    def post_task_comment(self, task_id, params, headers=None):
        return requests.post(url=cfg.POST_TASK_COMMENT.format(domain=self.domain, task_id=task_id), params=params, headers=headers).json()

    @catch()
    def delete_all_task_comments(self, task_id, headers=None):
        return requests.delete(url=cfg.DELETE_TASK_COMMENTS.format(domain=self.domain, task_id=task_id), headers=headers)

    @catch()
    def get_db_employees(self, db_name, headers=None):
        return requests.get(url=cfg.ARM_EMPLOYEES.format(domain=self.domain, db_name=db_name), headers=headers).json()

    @catch()
    def post_taxation_organ(self, out_dict, headers=None):
        return requests.post(url=cfg.FETCH_TAXATION_ORGANS.format(domain=self.domain),
                             data=json.dumps({'taxation_organs': out_dict}), headers=headers)

    @catch(retries=2, delay=1)
    def get_alert(self, params, headers=None):
        return requests.get(cfg.GET_ALERT.format(domain=self.domain), params=params, headers=headers)

    @catch(retries=10, delay=5)
    def post_alerts(self, params, headers=None):
        return requests.post(url=cfg.POST_ALERTS.format(domain=self.domain), params=params, headers=headers)

    @catch()
    def resolve_alert(self, params, headers=None):
        return requests.put(url=cfg.RESOLVE_ALERT.format(domain=self.domain), params=params, headers=headers)

    @catch(delay=5)
    def resolve_all_alerts(self, entity_id, keys, headers=None):
        return requests.delete(url=cfg.RESOLVE_ALL_ALERTS.format(domain=self.domain),
                               json={'entity_id': entity_id, 'keys': keys}, headers=headers)


    #################### FileVault apis ####################

    @catch()
    def get_file(self, params, headers=None):
        return requests.get(url=cfg.FILE_VAULT_DOWNLOAD_FILE.format(domain=self.domain), params=params, headers=headers)


    #################### OGD apis ####################

    @catch()
    def get_ogd_excel(self, headers=None):
        return requests.get(url=cfg.OGD_EXCEL)


    #################### Oked apis ####################

    @catch()
    def get_all_okeds(self, headers=None):
        return requests.get(url=cfg.OKEDS.format(domain=self.domain), headers=headers).json()