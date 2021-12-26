from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("%s() called, request: %s" % (func.__name__, args))
        result = func(*args, **kwargs)
        print("%s() called, result: %s" % (func.__name__, result))
        return result

    return wrapper


def log_with(text):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("[%s] %s() called, request: %s" % (text, func.__name__, args))
            result = func(*args, **kwargs)
            print("[%s] %s() called, result: %s" % (text, func.__name__, result))
            return result

        return wrapper

    return decorator


@log
def my_format(msg):
    return "prefix %s subfix" % msg


@log_with('custom message')
def my_format_1(msg):
    return "prefix %s subfix" % msg


if __name__ == '__main__':
    print(my_format("hello"))
    print(my_format_1("hello"))
