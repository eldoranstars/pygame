class Dog():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")

    def update_age(self, newage):
        self.age += newage

class ElectroDog(Dog):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.battery_size = 70

    def describe_battery_size(self):
        print('bat.size: ' + str(self.battery_size))


my_dog = ElectroDog('Bob', 6)
my_dog.describe_battery_size()