from electric_car import ElectricCar
from electric_car import Battery

"""
from electric_car import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
"""
battery = Battery()
new_my_el_car = ElectricCar('hz', 'r', 2011, battery=battery)
print(new_my_el_car.get_descriptive_name())


new_my_el_car.battery.get_range()
new_my_el_car.battery.upgrade_battery(240)
new_my_el_car.battery.get_range()