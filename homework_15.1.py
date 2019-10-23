# Extend the existing @logger decorator which writes logs to a file
# called log.txt instead of console
from functools import wraps


def logger(func):
    @wraps(func)
    def decorator(*args):
        with open('homework_directory/log.txt', 'w') as file:
            file.write(*args)
            print(f"It`s fine : {func.__name__} is working")
    return decorator


@logger
def logger_decorator(log):
    return log


logger_decorator("Do you wont me to do this homework?")
