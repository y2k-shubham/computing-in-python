#Copy your Burrito class from the last exercise. Now, add
#a method called "get_cost" to the Burrito class. It should
#accept zero arguments (except for "self", of course) and
#it will return a float. Here's how the cost should be
#computed:
#
# - The base cost of a burrito is $5.00
# - If the burrito's meat is "chicken", "pork" or "tofu",
#   add $1.00 to the cost
# - If the burrito's meat is "steak", add $1.50 to the cost
# - If extra_meat is True and meat is not set to False, add
#   $1.00 to the cost
# - If guacamole is True, add $0.75 to the cost
#
#Make sure to return the result as a float even if the total
#is a round number (e.g. for burrito with no meat or
#guacamole, return 5.0 instead of 5).


#Write your code here!
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

    def get_cost(self) -> float:
        cost = 5.00

        if self.get_meat():
            if self.get_meat() in ["chicken", "pork", "tofu"]:
                cost += 1.00
            elif self.get_meat() == 'steak':
                cost += 1.50

            if self.get_extra_meat():
                cost += 1.00

        if self.get_guacamole():
            cost += 0.75

        return cost


#Below are some lines of code that will test your class.
#You can change the value of the variable(s) to test your
#class with different inputs.
#
#If your function works correctly, this will originally
#print: 7.75
a_burrito = Burrito("pork", False, "white", "black", extra_meat = True, guacamole = True)
print(a_burrito.get_cost())
