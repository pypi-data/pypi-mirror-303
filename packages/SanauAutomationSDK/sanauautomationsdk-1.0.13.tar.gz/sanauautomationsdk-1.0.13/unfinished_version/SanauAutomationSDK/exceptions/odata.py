class ODataUnknownError(Exception):
    def __init__(self, message="Неизвестная ошибка"):
        self.message = message
        super().__init__(self.message)


class ODataError(Exception):
    def __init__(self, message="Ошибка получения данных из интерфейса OData"):
        self.message = message
        super().__init__(self.message)


class ODataNotFoundError(Exception):
    def __init__(self, message="Не настроен web inst на сервер 1С или неправильно указан путь", url=None):
        self.message = message + f" ({url})"
        super().__init__(self.message)


class ODataAuthenticationError(Exception):
    def __init__(self, used_login):
        self.message = f"Не удалось авторизоваться под пользователем \"{used_login}\""
        super().__init__(self.message)


class ODataTooManyConnectionsError(Exception):
    def __init__(self, message="Too many connections"):
        self.message = message
        super().__init__(self.message)


class ODataTimeOutError(Exception):
    def __init__(self, message="Out of time!"):
        self.message = message
        super().__init__(self.message)
