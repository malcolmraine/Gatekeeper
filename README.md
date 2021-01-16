# Gatekeeper
Python module providing mutator and enforcement method functionality.

## Components
### Mutator
Class offering mutator method functionality without requiring private properties and/or ```@property``` decorators

### Enforcer
Class containing decorators for various method argument type and format enforcement.

## Usage
From ```examples/personal_data_example.py```:

```python
from Gatekeeper import Mutator


class Person(Mutator):
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.dob = ""

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

    @Mutator.datetime('%Y-%m-%dT%H:%M:%SZ')
    def get_dob_attribute(self, value):
        return value


person = Person()
person.first_name = "john"
person.last_name = "doe"
person.dob = "06/29/1983"

print(person.first_name)
print(person.last_name)
print(person.dob)
```
