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
                            if isinstance(modified_args[i], str):
                                modified_args[i] += str(fill_value) * (
                                    n - len(modified_args[i])
                                )
                            elif isinstance(modified_args[i], list):
                                modified_args[i].extend(
                                    [fill_value] * (n - len(modified_args[i]))
                                )
                            else:
                                raise Exception(
                                    f"Length violation at argument {i}; Cannot adjust length."
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
