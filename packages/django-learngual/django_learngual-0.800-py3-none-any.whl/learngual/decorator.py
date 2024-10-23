from functools import wraps

from django.utils import translation


# Decorator version
def language_decorator(lang):
    """
    A decorator that activates a specific language during the function execution
    and reverts to the original language after the function completes.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_language = translation.get_language()
            translation.activate(lang)
            try:
                return func(*args, **kwargs)
            finally:
                translation.activate(current_language)

        return wrapper

    return decorator
