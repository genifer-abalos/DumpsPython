class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"__str__ = The car has a color {self.color} with {self.mileage} kms of mileage"

    def __repr__(self):
        return f"__repr__ = The car has a color {self.color} with {self.mileage} kms of mileage"


my_car = Car('White', 1000)
print(my_car)       # automatically assumes the str dunder
#or
print(str(my_car))


print(my_car.__repr__())
#or
print(repr(my_car))