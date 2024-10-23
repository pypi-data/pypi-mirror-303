import gc
from functools import wraps

def garbage_collector_at_the_end(func):
    """
    Decorador para ejecutar el garbage collector después de que la función decorada termine.

    Parameters:
    func (callable): La función que será decorada.

    Returns:
    callable: La función decorada.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        gc.collect()
        # print(f"Garbage collector ejecutado después de la función: {func.__name__}")

        return result

    return wrapper
