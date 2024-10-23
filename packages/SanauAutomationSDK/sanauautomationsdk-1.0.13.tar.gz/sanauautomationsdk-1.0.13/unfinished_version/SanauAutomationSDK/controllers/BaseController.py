from datetime import datetime, timezone
import json


class BaseController:
    def __init__(self, model):
        self.model = model

    def create(self, **kwargs):
        model_defaults = self.model._meta.defaults
        for k, v in model_defaults.items():
            if k.name == 'created_at' or k.name == 'updated_at':
                if k.name not in kwargs:
                    kwargs[k.name] = datetime.now(timezone.utc)
            else:
                if k.name not in kwargs:
                    kwargs[k.name] = v

        for k, v in kwargs.items():
            if isinstance(v, dict):
                kwargs[k] = json.dumps(v)
        # TODO: сделать возврат объекта модели после его создания
        return self.model.raw(
            f'''INSERT INTO {self.model._meta.table_name} ({", ".join([k for k in kwargs.keys()])}) VALUES ({", ".join([f"'{v}'" for v in kwargs.values()])})''').execute()

    def _get_by(self, **kwargs):
        condition_text = ''
        order_by, order_type = kwargs.pop('sorting_policy', ('created_at', 'DESC'))
        for i, (k, v) in enumerate(kwargs.items()):
            if isinstance(v, list):
                condition_text += '( ' + 'OR '.join([f"{k}='{list_item}' " for list_item in v]) + ') '
            elif isinstance(v, tuple) and len(v) == 2:
                if v[0] == 'DATE':
                    condition_text += f"DATE({k})='{v[1]}' "
                elif v[0] == 'IN':
                    if not len(v[1]):
                        continue
                    in_list = ', '.join([f"'{item}'" for item in v[1]])
                    condition_text += f"{k} IN ({in_list}) "
                elif v[0] in ['<', '>', '=', '<=', '>=', '<>']:
                    condition_text += f"{k}{v[0]}'{v[1]}' "
            else:
                condition_text += f"{k}='{v}' "
            if len(kwargs.keys()) > i + 1:
                condition_text += 'AND '

        result = self.model.raw(f'''SELECT * FROM {self.model._meta.table_name} WHERE {condition_text} ORDER BY {order_by} {order_type}''').execute()
        return result

    def get_or_none(self, **kwargs):
        result = self._get_by(**kwargs)
        return result[0] if result else None

    def get_all(self, **kwargs):
        result = self._get_by(**kwargs)
        return result if result else None

    def update(self, **kwargs):
        if 'id' not in kwargs:
            raise ValueError('id is required')
        all_fields = list(self.model._meta.fields.keys())
        id_value = kwargs.pop('id')
        where = kwargs.pop('_where', None)
        if where is not None and not isinstance(where, dict):
            raise ValueError("_where must be a dictionary")
        where_clause = f"id = '{id_value}'" if where is None else " AND ".join([f"{k} = '{v}'" for k, v in where.items()])
        update_data = {'updated_at': datetime.now(timezone.utc)} if 'updated_at' in all_fields else {}

        for k, v in kwargs.items():
            if k not in all_fields:
                raise ValueError(f'{k} is not a valid field')
            update_data[k] = json.dumps(v) if isinstance(v, dict) else v

        if self.model.raw(f'''UPDATE {self.model._meta.table_name} SET {", ".join([f"{k} = '{update_data[k]}'" for k, v in kwargs.items()])} WHERE {where_clause}''').execute() == 0:
            return None
        return self.get_or_none(id=id_value)

    def delete(self, item_id):
        self.model.raw(f"DELETE FROM {self.model._meta.table_name} WHERE id = {item_id}").execute()
