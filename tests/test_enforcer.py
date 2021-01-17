import unittest
from Gatekeeper import Enforcer


class TestEnforcer(unittest.TestCase):
    def test_type_enforced(self) -> None:
        """

        :return:
        """

        @Enforcer.type_enforced(int)
        def func(x):
            return x

        self.assertEqual(10, func(10))

    def test_type_enforced_error(self) -> None:
        """

        :return:
        """

        @Enforcer.type_enforced(int)
        def func(x):
            return x

        self.assertRaises(Exception, func, (10,))

    def test_length_list(self) -> None:
        """
        Test for @Enforcer.length decorator when the argument is a list and
        the adjustment flag is set to False and the argument length is equal to the
        given length value.

        :return:
        """

        @Enforcer.length(3)
        def func(x):
            return x

        self.assertEqual([1, 2, 3], func([1, 2, 3]))

    def test_length_str(self) -> None:
        """
        Test for @Enforcer.length decorator when the argument is a string and
        the adjustment flag is set to False and the argument length is equal to the
        given length value.

        :return:
        """

        @Enforcer.length(4)
        def func(x):
            return x

        self.assertEqual("test", func("test"))

    def test_length_list_error(self) -> None:
        """
        Test for @Enforcer.length decorator when the argument is a list and
        the adjustment flag is set to False.

        :return: None
        """

        @Enforcer.length(5)
        def func(x):
            return x

        self.assertRaises(Exception, func, ([1, 2, 3],))

    def test_length_str_error(self) -> None:
        """
        Test for @Enforcer.length decorator when the argument is a string and
        the adjustment flag is set to False.

        :return: None
        """

        @Enforcer.length(5)
        def func(x):
            return x

        self.assertRaises(Exception, func, ("test",))

    def test_length_list_adj(self) -> None:
        """
        Test for @Enforcer.length decorator when the argument is a list and
        the adjustment flag is set to True.

        :return: None
        """

        @Enforcer.length(5, adjust=True, fill_value=None)
        def func(x):
            return x

        self.assertEqual([1, 2, 3, None, None], func([1, 2, 3]))

    def test_length_str_adj(self) -> None:
        """
        Test for @Enforcer.length decorator when the argument is a string and
        the adjustment flag is set to True.

        :return: None
        """

        @Enforcer.length(6, adjust=True, fill_value="*")
        def func(x):
            return x

        self.assertEqual("test**", func("test"))

    def test_length_set_adj(self) -> None:
        """
        Test for @Enforcer.length decorator when the argument is a set and
        the adjustment flag is set to True.

        :return: None
        """

        @Enforcer.length(5, adjust=True, fill_value=None)
        def func(x):
            return x

        self.assertRaises(Exception, func, ({1, 2, 3},))
