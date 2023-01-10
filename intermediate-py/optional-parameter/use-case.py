
class car(object):
    def __init__(self, make, model, year, condition='New', kms=0):  # let's set condition default to new, and kms=0
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms

    def display(self, show_all=True):
        if show_all:
            print(f"CAR = {self.make} {self.model} from {self.year}; {self.condition}, {self.kms}")
        else:
            print(f"CAR = {self.make} {self.model} from {self.year}")


gen_car = car('Make', 'Model', 1997, 'Young', 1_000_000)
gen_car.display(show_all=True)

uno_car = car('Toyota', 'Fortuner', 2012)
uno_car.display(True)

dos_car = car('Suzuki', 'X', 2020)
dos_car.display()