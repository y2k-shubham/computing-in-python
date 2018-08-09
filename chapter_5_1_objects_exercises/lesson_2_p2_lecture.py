###########################
# class definitions
###########################

class Name:

    def __init__(self):
        self.first_name = "[no first name]"
        self.last_name = "[no last name]"

    def __repr__(self):
        repr = """
            First-Name : {}
            Last -Name : {}
        """.format(self.first_name, self.last_name)
        return repr


class Person_2:

    def __init__(self):
        self.name = Name()
        self.eye_color = "[no eye color]"
        self.age = -1

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
import copy

separator_attempt = "###########################"


def modify_show(person: Person_2,
                modifier: Callable[[Person_2], Person_2]) -> None:
    print("Before modification")
    print(person)

    modified_person = modifier(person)

    print("After modification")
    print(modified_person)


def modify_demo(attempt_name: str,
                modifier: Callable[[Person_2], Person_2]) -> None:
    print(separator_attempt)
    print(attempt_name)
    print()

    person = Person_2()
    modify_show(person, modifier)

    print(separator_attempt)


###########################
# modifier demo
###########################

# demo - 1
def modifier_1(new_first_name: str) -> Callable[[Person_2], Person_2]:
    def actual_modifier(person):
        modified_person = copy.deepcopy(person)
        modified_person.name.first_name = new_first_name
        return modified_person

    return actual_modifier

modify_demo(attempt_name="attempt-1", modifier=modifier_1(new_first_name="Daniel"))


# demo - 2
def modifier_2(new_first_name: str) -> Callable[[Person_2], Person_2]:
    def actual_modifier(person):
        modified_person = person
        modified_name = Name()
        modified_name.first_name = new_first_name
        modified_person.name = modified_name
        return modified_person

    return actual_modifier

modify_demo(attempt_name="attempt-2", modifier=modifier_1(new_first_name="Richard"))
