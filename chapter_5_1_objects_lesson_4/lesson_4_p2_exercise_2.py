#Previously, you wrote a class called ExerciseSession that
#had three attributes: an exercise name, an intensity, and a
#duration.
#
#Add a new method to that class called calories_burned.
#calories_burned should have no parameters (besides self, as
#every method in a class has). It should return an integer
#representing the number of calories burned according to the
#following formula:
#
# - If the intensity is "Low", 4 calories are burned per
#   minute.
# - If the intensity is "Moderate", 8 calories are burned
#   per minute.
# - If the intensity is "High", 12 calories are burned per
#   minute.
#
#You may copy your class from the previous exercise and just
#add to it.


#Add your code here!
class ExerciseSession:

    def __init__(self,
                 exercise: str,
                 intensity: str,
                 duration: int):
        self.exercise = exercise
        self.intensity = intensity
        self.duration = duration

    def get_exercise(self) -> str:
        return self.exercise

    def get_intensity(self) -> str:
        return self.intensity

    def get_duration(self) -> int:
        return self.duration

    def set_exercise(self, new_exercise: str) -> None:
        self.exercise = new_exercise

    def set_intensity(self, new_intensity: str) -> None:
        self.intensity = new_intensity

    def set_duration(self, new_duration: int) -> None:
        self.duration = new_duration

    def calories_burned(self) -> int:
        calorie_burn_map = {
            "Low": 4,
            "Moderate": 8,
            "High": 12
        }
        calories_burned = calorie_burn_map[self.intensity] * self.duration
        return calories_burned



#If your code is implemented correctly, the lines below
#will run error-free. They will result in the following
#output to the console:
#240
#360
new_exercise = ExerciseSession("Running", "Low", 60)
print(new_exercise.calories_burned())
new_exercise.set_exercise("Swimming")
new_exercise.set_intensity("High")
new_exercise.set_duration(30)
print(new_exercise.calories_burned())



