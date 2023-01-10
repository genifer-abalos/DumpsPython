# Static and Class methods
# WITH MY NOTES

class Person():
    population = 50

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Class method
    # you can call it in any instance of a class
    # Person.get_population()
    # you don't need to create an object of the class to call a class method
    # this can access anything that is public within the class
    # cls.population
    # population is defined within the class
    # can add additional parameters as well

    @classmethod
    def get_population(cls):    # cls stands for class
        return cls.population

    # Static method
    # you can also call it in any instance of a class
    # Person.is_minor(18)
    # Person.what_legal_age()
    # the only difference with a class method is, it can be called without a cls parameter
    # you don't need self and cls
    # # this CAN'T access anything within the class
    # it can be without a parameter or with parameter

    @staticmethod
    def is_minor(age):
        return age <= 18

    @staticmethod
    def what_legal_age():   # static method with no parameter
        return 18

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


gen = Person("Genifer", 25)
gen.display()
print(gen.get_population())     # without @classmethod, you need to create a gen object first before calling get_population()
print(Person.get_population())  # this will not work without the @classmethod annotation
# print(gen.is_minor())
print(Person.is_minor(18))
print(Person.what_legal_age())
