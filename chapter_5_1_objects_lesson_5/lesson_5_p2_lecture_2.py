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


from typing import Callable

separator = "###########################"


def modify_show(person: Person,
                name_modifier: Callable[[Name], None]) -> None:
    print("Before modification")
    print(person)

    name_modifier(person.name)

    print("After  modification")
    print(person)


def modify_demo(attempt_name: str,
                name_modifier: Callable[[Name], None]) -> None:
    print(separator)
    print(attempt_name)
    print()

    person = Person(
        name=Name(first_name="shubham", last_name="gupta"),
        eye_color="brown",
        age=25
    )
    modify_show(person=person, name_modifier=name_modifier)

    print(separator)


###########################
# name_modifier demo
###########################


# demo - 1
def name_modifier_1(name: Name) -> None:
    name.first_name = name.first_name.upper()
    name.last_name = name.last_name.upper()


modify_demo(attempt_name="attempt-1", name_modifier=name_modifier_1)


# demo - 2
def name_modifier_2(name: Name) -> None:
    def str_modifier(string: str) -> None:
        string = string.upper()

    str_modifier(name.first_name)
    str_modifier(name.last_name)


modify_demo(attempt_name="attempt-2", name_modifier=name_modifier_2)
