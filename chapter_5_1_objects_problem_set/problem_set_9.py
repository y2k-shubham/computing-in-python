# Copy your Burrito class from the last exercise. Now,
# write a getter and a setter method for each attribute.
# Each setter should accept a value as an argument. If the
# value is a valid value, it should set the corresponding
# attribute to the given value. Otherwise, it should set the
# attribute to False.
#
# Edit the constructor to use these new setters and getters.
# In other words, if we were to call:
#
# new_burrito = Burrito("spaghetti", True, True, False)
#
# new_burrito.meat would be False because "spaghetti" is not
# one of the valid options. Note that you should NOT try to
# check if the new value is valid in both the constructor and
# the setter: instead, just call the setter from the
# constructor using something like self.set_meat(meat).
#
# Valid values for each setter are as follows:
#
# - set_meat: "chicken", "pork", "steak", "tofu", False
# - set_to_go: True, False
# - set_rice: "brown", "white", False
# - set_beans: "black", "pinto", False
# - set_extra_meat: True, False
# - set_guacamole: True, False
# - set_cheese: True, False
# - set_pico: True, False
# - set_corn: True, False
#
# Make sure you name each setter with the format:
# "set_some_attribute" and "get_some_attribute"
#
# For example, the getter for meat would be get_meat. The
# getter for to_go would be get_to_go.
#
# Hint: Your code is going to end up *very* long. This
# will be the longest program you've written so far, but
# it isn't the most complex. Complexity and length are
# often very different!
#
# Hint 2: Checking for valid values will be much easier
# if you make a list of valid values for each attribute
# and check the new value against that.


# Write your code here!
from typing import Union


class Burrito:
    def __init__(self,
                 meat,
                 to_go,
                 rice,
                 beans,
                 extra_meat: bool = False,
                 guacamole: bool = False,
                 cheese: bool = False,
                 pico: bool = False,
                 corn: bool = False) -> None:
        self.set_meat(meat=meat)
        self.set_to_go(to_go=to_go)
        self.set_rice(rice=rice)
        self.set_beans(beans=beans)
        self.set_extra_meat(extra_meat=extra_meat)
        self.set_guacamole(guacamole=guacamole)
        self.set_cheese(cheese=cheese)
        self.set_pico(pico=pico)
        self.set_corn(corn=corn)

    def get_meat(self) -> Union[str, bool]:
        return self.meat

    def get_to_go(self) -> bool:
        return self.to_go

    def get_rice(self) -> Union[str, bool]:
        return self.rice

    def get_beans(self) -> Union[str, bool]:
        return self.beans

    def get_extra_meat(self) -> bool:
        return self.extra_meat

    def get_guacamole(self) -> bool:
        return self.guacamole

    def get_cheese(self) -> bool:
        return self.cheese

    def get_pico(self) -> bool:
        return self.pico

    def get_corn(self) -> bool:
        return self.corn

    def set_meat(self, meat: str) -> None:
        valid_meats = ["chicken", "pork", "steak", "tofu"]
        self.meat = meat if meat in valid_meats else False

    def set_to_go(self, to_go: bool) -> None:
        self.to_go = to_go if isinstance(to_go, bool) else False

    def set_rice(self, rice: str) -> None:
        valid_rice = ["brown", "white"]
        self.rice = rice if rice in valid_rice else False

    def set_beans(self, beans: str) -> None:
        valid_beans = ["black", "pinto"]
        self.beans = beans if beans in valid_beans else False

    def set_extra_meat(self, extra_meat: bool) -> None:
        self.extra_meat = extra_meat if isinstance(extra_meat, bool) else False

    def set_guacamole(self, guacamole: bool) -> None:
        self.guacamole = guacamole if isinstance(guacamole, bool) else False

    def set_cheese(self, cheese: bool) -> None:
        self.cheese = cheese if isinstance(cheese, bool) else False

    def set_pico(self, pico: bool) -> None:
        self.pico = pico if isinstance(pico, bool) else False

    def set_corn(self, corn: bool) -> None:
        self.corn = corn if isinstance(corn, bool) else False

# Feel free to add code below to test out the class that
# you've written. It won't be used for grading.
