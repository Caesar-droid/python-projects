from car import Car
from electric_car import ElectricCar as EC
my_new_car=Car('audi','a4',2019)
print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading=23
# my_new_car.read_odometer()
my_bettle=Car('volkswagen','bettle',2019)
print(my_bettle.get_descriptive_name())
my_tesla=EC('tesla','roaster',2019)
print(my_tesla.get_descriptive_name())

