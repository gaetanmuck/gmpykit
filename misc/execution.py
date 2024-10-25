import threading


def deco_interval(sec):
    """
    This decorator will run the decorated function each given seconds.
    """

    def inner(fct):
        def wrapper(*args, **kwargs):
            set_interval(fct, sec, args, kwargs)

        return wrapper

    return inner


def set_interval(func, sec, *args, **kwargs):
    """
    This function aims at making the same thing as the likely named function in Javascript:
    Run a function each given time.
    If the function needs arguments, they need to be given as keyword arguments to set_interval,
    and they will also be given as keyword arguments to the called functions
    """

    def func_wrapper():
        set_interval(func, sec)
        func(*args, **kwargs)

    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t
