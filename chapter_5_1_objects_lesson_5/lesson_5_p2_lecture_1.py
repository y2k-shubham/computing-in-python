###########################
# class definitions
###########################


class Name:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        repr = """
            First-Name : {}
            Last -Name : {}
        """.format(self.first_name, self.last_name)
        return repr


class Person:
    def __init__(self, name: Name, eye_color: str, age: int):
        self.name = name
        self.eye_color = eye_color
        self.age = age

    def __repr__(self):
        repr = """
            Name      :-{}
            Eye-Color : {}
            Age       : {}
        """.format(self.name, self.eye_color, self.age)
        return repr


###########################
# modifier template methods
###########################


import copy
from typing import Callable

separator_attempt = "###########################"


def modify_show(person: Person,
                copier: Callable[[Person], Person],
                modifier: Callable[[Person], Person]) -> None:
    copied_person = copier(person)

    print("Before modification")
    print("Person Original:-{}".format(person))
    print("Person Copied  :-{}".format(copied_person))

    copied_person = modifier(copied_person)

    print("After modification")
    print("Person Original:-{}".format(person))
    print("Person Copied  :-{}".format(copied_person))


def modify_demo(attempt_name: str,
                copier: Callable[[Person], Person],
                modifier: Callable[[Person], Person]) -> None:
    print(separator_attempt)
    print(attempt_name)
    print()

    person = Person(Name("first-name", "last-name"), "eye-color", 25)
    modify_show(person, copier, modifier)

    print(separator_attempt)


###########################
# copier demo
###########################


def modifier(person: Person) -> Person:
    if hasattr(person.name, 'first_name'):
        person.name.first_name = "new-first-name"
    else:
        print("original name: {}".format(person.name))
        person.name = "new-name"

    person.eye_color = "new-eye-color"
    return person


# demo - 1
def copier_1(person: Person) -> Person:
    return person


modify_demo("attempt-1", copier_1, modifier)


# demo - 2
def copier_2(person: Person) -> Person:
    return copy.copy(person)


modify_demo("attempt-2", copier_2, modifier)


# demo - 3
def copier_3(person: Person) -> Person:
    return copy.deepcopy(person)


modify_demo("attempt-3", copier_3, modifier)
