from datetime import datetime
import maya


class Mutator(object):
    def __getattribute__(self, name):
        """

        :param name:
        :return:
        """
        try:
            return object.__getattribute__(self, f"get_{name}_attribute")(
                object.__getattribute__(self, name)
            )
        except AttributeError:
            return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        """

        :param name:
        :param value:
        :return:
        """
        try:
            object.__setattr__(
                self,
                name,
                object.__getattribute__(self, f"set_{name}_attribute")(value),
            )
        except AttributeError:
            object.__setattr__(self, name, value)

    @staticmethod
    def upper(fn):
        """

        :param fn:
        :return:
        """
        def wrapper(*args, **kwargs):
            return fn(*args, **kwargs).upper()

        return wrapper

    @staticmethod
    def lower(fn):
        """

        :param fn:
        :return:
        """
        def wrapper(*args, **kwargs):
            return fn(*args, **kwargs).lower()

        return wrapper

    @staticmethod
    def datetime(fmt):
        """

        :param fmt:
        :return:
        """
        def wrap(fn):
            def wrapper(*args, **kwargs):
                out: str or datetime = fn(*args, **kwargs)

                if isinstance(out, str):
                    return maya.parse(out).datetime().strftime(fmt)
                else:
                    return out.strftime(fmt)

            return wrapper
        return wrap
