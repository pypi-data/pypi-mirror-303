from .ODataHandler import ODataHandler
from ..entities.User import User
from ....classes.OneSApiCredentials import OneSApiCredentials


class UsersHandler(ODataHandler):

    def __init__(self, api_wrapper, credentials: OneSApiCredentials, database_name, server):
        super().__init__(odata_entity=User(database_name, server), api_wrapper=api_wrapper, credentials=credentials)

    def get_by(self, target, key):
        try:
            return [item[target] for item in self.all() if item[target] == key][0]
        except Exception as e:
            return {'status': str(e)}
