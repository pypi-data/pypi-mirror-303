import sys
import os
import datetime
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from SanauAutomationSDK.api.Wrapper import Wrapper

api_wrapper = Wrapper('KZ', 'pbo.kz', '7nuLUYDYeQLyd3Rn')
data = {
    'file_vault_uuid': "34B62952-7898-408E-BC9A-08D10FD08B6F",
    'folder_name': "Оборотно-сальдовая ведомость/05.05.2024/",
    'file_name': "8f363db8-dea4-4fbd-8026-66d6ed05e53a_osv_current_year.xlsx",
}
# print(api_wrapper.get_filevault_file(params=data))
try:
    print(api_wrapper.get_test())
except Exception as e:
    print("get: ", e)

try:
    print(api_wrapper.post_test())
except Exception as e:
    print("post: ", e)

try:
    print(api_wrapper.put_test())
except Exception as e:
    print("put: ", e)

try:
    print(api_wrapper.delete_test())
except Exception as e:
    print("delete: ", e)
    
print(api_wrapper.get_db_employees('abo-2'))

# pbo_wrapper = Wrapper('KZ', 'pbo.kz', '7nuLUYDYeQLyd3Rn')
# print(pbo_wrapper.get_database(name='bagat'))

# try:
#     print(api_wrapper.get_databases())
#     print("Test passed")
# except Exception as e:
#     print(e)
