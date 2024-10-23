class Alert:

    def __init__(self, model_class, model_id, model_key, model_alert=None, model_severity=100, model_resolvable=True):
        self.model_class = model_class
        self.model_id = model_id
        self.model_alert = model_alert
        self.model_key = model_key
        self.model_severity = model_severity
        self.model_resolvable = model_resolvable
