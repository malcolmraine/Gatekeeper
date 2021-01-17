from datetime import datetime
import maya


class Mutator(object):
    def __getattribute__(self, name: str):
        """
        Override for __getattribute__ magic method. It checks for the attribute's
        respective mutator method and calls it if it exists. If the mutator does not
        exist, the parent __getattribute magic method is called.

        :param name: Attribute name
        :return: Mutated attribute value
        """
        try:
            return object.__getattribute__(self, f"get_{name}_attribute")(
                object.__getattribute__(self, name)
            )
        except AttributeError:
            return object.__getattribute__(self, name)

    def __setattr__(self, name: str, value):
        """
        Override for __setattr__ magic method. It checks for the attribute's
        respective mutator method and calls it if it exists. If the mutator does not
        exist, the parent __setattr__ magic method is called.

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
        Wrapper to automatically mutate a string attribute value to uppercase.

        :param fn: Mutator method handle
        :return: wrapper method.
        """

        def wrapper(*args, **kwargs):
            return fn(*args, **kwargs).upper()

        return wrapper

    @staticmethod
    def lower(fn):
        """
        Wrapper to automatically mutate a string attribute value to lowercase.

        :param fn: Mutator method handle
        :return: wrapper method.
        """

        def wrapper(*args, **kwargs):
            return fn(*args, **kwargs).lower()

        return wrapper

    @staticmethod
    def cast(cast_type):
        """
        Wrapper to automatically cast a value to a given type.

        :param cast_type: Type to cast to
        :return: wrapper method.
        """

        def wrap(fn):
            def wrapper(*args, **kwargs):
                print(cast_type)
                return cast_type(fn(*args, **kwargs))

            return wrapper

        return wrap

    @staticmethod
    def datetime(fmt: str):
        """
        Wrapper to automatically mutate a string attribute value to a given datetime format.

        :param fmt: Datetime format.
        :return: wrapper method.
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

    @staticmethod
    def round(n: int):
        """
        Rounds the wrapped function output to a given number of decimal places.

        :param n: Number of decimal places to round to
        :return: Rounded output
        """

        def wrap(fn):
            def wrapper(*args, **kwargs):
                return round(fn(*args, **kwargs), n)

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
