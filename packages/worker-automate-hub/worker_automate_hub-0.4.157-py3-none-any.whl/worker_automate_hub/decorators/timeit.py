import functools
import time


def timeit(func):
    """
    Um decorator para imprimir o tempo de execução de uma função.

    Ele printa o tempo de execução da função em segundos, com 4 casas decimais.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(
            f"Função {func.__name__} executada em {end_time - start_time:.4f} segundos"
        )
        return result

    return wrapper
