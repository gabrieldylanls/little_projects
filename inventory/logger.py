from functools import wraps
import os


def logger(original_function):
    @wraps(original_function)
    def wrapper(*args, **kwargs):
        with open(f"{os.getcwd()}/inventory/inventory_traces.txt", mode="a") as fw:
            fw.write(
                f"{original_function.__name__} has been running with args {args}, kwargs {kwargs}\n"
            )

        return original_function(*args, **kwargs)

    return wrapper
