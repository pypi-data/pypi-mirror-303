import json
import time
import requests


def catch(retries=10, delay=10):
    def decorator(func):
        def wrapper(*args, **kwargs):
            self = args[0]
            headers = kwargs.get('headers', {})
            kwargs['headers'] = {**{'Access-Key': self.access_key}, **headers}

            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == retries-1:
                        if isinstance(e, json.JSONDecodeError):
                            raise json.JSONDecodeError(f'JSONDecoderError {e.msg}') from None
                        raise e from None
                time.sleep(delay)

        return wrapper

    return decorator

