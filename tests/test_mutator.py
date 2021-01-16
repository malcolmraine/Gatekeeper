import unittest
from Gatekeeper import Mutator


class Person(Mutator):
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.dob = ""
        self.age = 0
        self.address = ""

    @Mutator.lower
    def get_first_name_attribute(self, value):
        return value

    @Mutator.upper
    def get_last_name_attribute(self, value):
        return value

    @Mutator.lower
    def set_first_name_attribute(self, value):
        return value

    @Mutator.upper
    def set_last_name_attribute(self, value):
        return value

    @Mutator.datetime('%m/%d/%Y')
    def get_dob_attribute(self, value):
        return value

    @Mutator.cast(int)
    def set_age_attribute(self, value):
        return value

    @staticmethod
    def set_address_attribute(value):
        # Using mutator without decorator
        return value.upper()


class TestMutator(unittest.TestCase):
    def test_cast(self):
        person = Person()
        person.age = 55.989872

        self.assertEqual(55, person.age)

    def test_upper(self):
        person = Person()
        person.last_name = "doe"

        self.assertEqual("DOE", person.last_name)

    def test_lower(self):
        person = Person()
        person.first_name = "JOHN"

        self.assertEqual("john", person.first_name)

    def test_datetime(self):
        person = Person()
        person.dob = "1983-03-19T00:00:00Z"

        self.assertEqual("03/19/1983", person.dob)