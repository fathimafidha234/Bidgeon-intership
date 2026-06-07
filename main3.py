class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
    def drive(self, km):
        self.odometer += km
    def get_info(self):
        print("Make:", self.make)
        print("Model:", self.model)
        print("Year:", self.year)
        print("Odometer:", self.odometer, "km")
car1 = Car("Toyota", "Corolla", 2023)
car1.get_info()
car1.drive(150)
print("\nAfter driving:")
car1.get_info()