class Enforcer(object):
    @staticmethod
    def type_enforced(*args_types, **kwargs_types):
        """

        :param args_types:
        :param kwargs_types:
        :return:
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
    def length(n):
        """
        
        :param n:
        :return:
        """

        def wrap(fn):
            def wrapper(*args, **kwargs):
                for idx, arg in enumerate(args):
                    if len(list(arg)) != n:
                        raise Exception(f"Length violation at argument {idx}")

                return fn(*args, **kwargs)

            return wrapper

        return wrap
