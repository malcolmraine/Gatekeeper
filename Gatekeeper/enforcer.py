class Enforcer(object):
    @staticmethod
    def type_enforced(*args_types, **kwargs_types):
        """
        Enforces types of given arguments.

        :param args_types: Argument ypes to enforce.
        :param kwargs_types: Keyword argument types to enforce.
        :return: Function wrapper
        """

        def wrap(fn):
            def wrapper(*args, **kwargs):
                print(args, args_types)
                for n, _type in enumerate(args_types):
                    if not isinstance(args[n], _type):
                        raise TypeError(f"Invalid type input for {fn}")

                return fn(*args, **kwargs)

            return wrapper

        return wrap

    @staticmethod
    def length(n, adjust=False, fill_value=None):
        """
        Enforces a length for provided list arguments.

        :param n: Required list length
        :param adjust: If True, fill the rest of the list with specified values if the list is
                        too short of cut the list down if too long.
        :param fill_value: Value to fill rest of list with if fill=True
        :return: Function wrapper
        """

        def wrap(fn):
            def wrapper(*args, **kwargs):
                if adjust:
                    modified_args = list(args)
                    for i in range(len(modified_args)):
                        if len(list(modified_args[i])) < n:
                            modified_args[i].extend(
                                [fill_value] * (n - len(modified_args[n]))
                            )
                        elif len(list(args[i])) > n:
                            modified_args[i] = modified_args[i][:n]

                    return fn(*modified_args, **kwargs)
                else:
                    for i in range(len(args)):
                        if len(args[i]) != n:
                            raise Exception(f"Length violation at argument {i}")

                    return fn(*args, **kwargs)

            return wrapper

        return wrap

    @staticmethod
    def saturate(low: int or float, high: int or float):
        """
        Limits the output of the wrapped function to given range.

        :param low: Low-end saturation limit
        :param high: High-end saturation limit
        :return: Limited output
        """

        def wrap(fn):
            def wrapper(*args, **kwargs):
                out = fn(*args, **kwargs)

                if out < low:
                    return low
                elif out > high:
                    return high
                else:
                    return out

            return wrapper

        return wrap
