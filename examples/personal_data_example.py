from Gatekeeper import Mutator


class Person(Mutator):
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.dob = ""
        self.age = 0
        self.address = ""

    @Mutator.upper
    def get_first_name_attribute(self, value):
        return value

    @Mutator.upper
    def get_last_name_attribute(self, value):
        return value

    @Mutator.upper
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

    def set_address_attribute(self, value):
        # Using mutator without decorator
        return value.upper()


person = Person()
person.first_name = "john"
person.last_name = "doe"
person.dob = "1983-03-19T00:00:00Z"
person.age = 55.989872
person.address = "123 abc ln. PeopleTown, USA"

print(person.first_name)
print(person.last_name)
print(person.dob)
print(person.age)
print(person.address)

