def new_register(func_container, before_func = lambda f: None):
    """
    :param func_container:
    :param before_func: lambda f: print(f"run {f.__name__}")
    :return:
    """
    def cmd_register(func):
        def wrapper(*args, **kwargs):
            before_func(func)
            return func(*args, **kwargs)
        func_container.append(func)
        return wrapper
    return cmd_register
