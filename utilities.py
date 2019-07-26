import inspect


def fc(conn, fun):
    """
    Get the parameters of a function and call it
    :param conn: the connection for OpenStack commands
    :param fun: the function to call
    :return: the result of the function call
    """
    par = dict()
    par['conn'] = conn
    params = set_params(fun, par)
    print(params)

    return fun(**params)


def set_params(fun, my_params):
    """
    Set the parameters required for a function
    :param fun: the function to analyze
    :param my_params: already set parameters
    :return: a dict containing keys and values of the parameters
    """
    params = inspect.signature(fun).parameters
    res = dict()

    print('Parameters for function ' + fun.__name__)

    for key in my_params.keys():
        if key in params:
            res[key] = my_params[key]

    for par in params:
        if par not in res.keys():
            p = input("Value for {par}: ".format(par=par))
            if p:
                res[par] = p

    return res
