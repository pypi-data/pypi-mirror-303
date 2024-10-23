class DB1C:

    def __init__(self, **kwargs):
        self.id = kwargs['database']['id']
        self.path = kwargs['database']['name']
        self.configuration = kwargs['database']['configuration']
        self.server = kwargs['database']['server']
        self.entity_id = kwargs['database']['entity']['id']
        self.disabled_esf_check = kwargs['database']['entity']['accounting_settings']['disable_esf_check']
        self.skip_validation_periods = kwargs['database']['entity']['skip_validation_periods']
        self.start_at = kwargs['sync']['start_at']
        self.end_at = kwargs['sync']['end_at']
        self.sync = kwargs['sync']['sync']
        self.is_vat_payer = kwargs['database']['entity']['accounting_settings']['is_vat_payer'],
        self.taxation_mode = kwargs['database']['entity']['taxation_mode'],
        self.main_oked_code = kwargs['database']['entity']['main_oked_code'],
        self.secondary_oked_codes = kwargs['database']['entity']['secondary_oked_codes'],
        self.team = kwargs['database']['entity']['team'],
        self.taxation_mode_changed_at = kwargs['database']['entity']['accounting_settings']['taxation_mode_changed_at'],
        self.period = kwargs['sync']['period'],
        self.slug = kwargs['database']['entity']['slug'],
        self.file_vault_uuid = kwargs['database']['entity']['file_vault_uuid'],
        self.db_entity = kwargs['database']
        self.connection_error = None
        self.countries = {}
