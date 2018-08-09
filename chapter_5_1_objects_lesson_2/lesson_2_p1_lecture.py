# 5.1.2

class Person_1:

    def __init__(self):
        self.first_name = "[no first name]"
        self.last_name = "[no last name]"
        self.eye_color = "[no eye color]"
        self.age = -1

# composition

class Name:

    def __init__(self):
        self.first_name = "[no first name]"
        self.last_name = "[no last name]"


class Person_2:

    def __init__(self):
        self.name = Name()
        self.eye_color = "[no eye color]"
        self.age = -1

