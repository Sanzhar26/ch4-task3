class Car():
    def __init__(self,mark,model,year):
        self.mark = mark
        self.model = model
        self.year = year
        self.odometer = 0
        self.fuel = 70
    
    def __add_distance(self, km):
        self.odometer += km
    
    def __subtract_fuel(self, km):
        self.fuel -= km/10
    
    def drive(self, km):
        if (self.fuel - km/10) >= 0:
            self.__add_distance(km)
            self.__subtract_fuel(km)
            print("Let's drive!")
        else:
            print("Need more fuel, please, fill more")

car1 = Car("Toyota", "Camry", "2015")
print(car1.mark,car1.model,car1.year)
car1.drive(150)
print(car1.odometer)
print(car1.fuel)