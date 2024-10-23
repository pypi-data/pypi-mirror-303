# GET
ONE_S_DATABASES = "https://{domain}/botapi/v1/one_s/databases"
ONE_S_DATABASE = "https://{domain}/botapi/v1/one_s/database/{database}"
ARM_EMPLOYEES = "https://{domain}/botapi/v1/one_s/databases/{db_name}/employees"
MY_NEW_TASKS = "https://{domain}/botapi/v1/tasks/my?status=new"
LAST_NEW_TASK = "https://{domain}/botapi/v1/tasks/last_new_task"
TASKS = "https://{domain}/botapi/v1/tasks"
TASKS_WITH_STATUS = "https://{domain}/botapi/v1/tasks?status={status}"
FILE_VAULT_DOWNLOAD_FILE = "https://files.{domain}/download/file"
NATIONAL_BANK = "https://nationalbank.kz/rss/get_rates.cfm?fdate={currency_date}"
OGD_EXCEL = "https://kgd.gov.kz/sites/default/files/spravochniki/spravochnik_kodifikator_s_ukazaniem_bin_i_rekvizitami_dlya_zachisleniya_platezhey_v_byudzhet_po_organam_gosudarstvennyh_dohodov_respubliki_kazahstan.xlsx"
DOMAINS = "https://auth.sanau.kz/domains_without_devs"
GET_ALERT = "https://{domain}/botapi/v1/alert"
OKEDS = "https://{domain}/api/v3/python_integration/get_all_okeds"

# POST
POST_ALERTS = "https://{domain}/botapi/v1/alerts"
FETCH_TAXATION_ORGANS = "https://{domain}/api/v3/python_integration/fetch_taxation_organs"
POST_TASK_COMMENT = "https://{domain}/botapi/v1/tasks/{task_id}/comments"

# PUT
RESOLVE_ALERT = "https://{domain}/botapi/v1/alerts/resolve"
UPDATE_TASK_STATUS = "https://{domain}/botapi/v1/tasks/{task_id}"

# DELETE
RESOLVE_ALL_ALERTS = "https://{domain}/botapi/v1/alerts/resolve_all"
DELETE_TASK_COMMENTS = "https://{domain}/botapi/v1/tasks/{task_id}/comments/destroy_all"


# ODATA
ODATA_REQUEST_BASE_URL = "http://{server}/{database_name}/odata/standard.odata/"
