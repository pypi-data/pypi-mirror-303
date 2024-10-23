from ...Wrapper import Wrapper
from ....utils.logutils import logger


class AlertsHandler:

    def __init__(self, api_wrapper: Wrapper):
        self.api_wrapper = api_wrapper

    def resolve_all_alerts(self, entity_id, keys):
        return self.api_wrapper.resolve_all_alerts(entity_id=entity_id, keys=keys)

    def create_alert(self, entity_id, key, message=None, model_class='Entity', severity=100, resolvable=True):
        params = {'model_class': model_class, 'model_id': entity_id, 'model_key': key,
                  'model_alert': message, 'model_severity': severity, 'model_resolvable': resolvable}

        try:
            alert = self.api_wrapper.post_alerts(params=params)
            return alert
        except Exception as e:
            logger.error(f'Failed to create alert: {e}')
            raise e

    def resolve_alert(self, entity_id, key, model_class='Entity', severity=100, resolvable=True):
        params = {'model_class': model_class, 'model_id': entity_id, 'model_key': key,
                  'model_severity': severity, 'model_resolvable': resolvable}

        try:
            alert = self.api_wrapper.resolve_alert(params=params)
            return alert
        except Exception as e:
            logger.error(f'Failed to resolve alert: {e}')
            raise e

    def get_alert(self, entity_id, key, message=None, model_class='Entity', severity=100, resolvable=True):
        params = {'model_class': model_class, 'model_id': entity_id, 'model_key': key,
                  'model_alert': message, 'model_severity': severity, 'model_resolvable': resolvable}

        try:
            request = self.api_wrapper.get_alert(params=params)
            if request is not None:
                return request.json()
            else:
                return None
        except Exception as e:
            raise e
