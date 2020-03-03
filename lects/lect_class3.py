class Car:
    wheels = 4  # class variable

    def __init__(self):
        self.mileage = 10  # instance variable
        self.company = "BMW"  # instance variable


c1 = Car()
c2 = Car()

print(c1.company, c1.mileage, c1.wheels)
print(c2.company, c2.mileage, c2.wheels)

Car.wheels = 9
print('After changing the class variable')
print(c1.company, c1.mileage, c1.wheels)
print(c2.company, c2.mileage, c2.wheels)
