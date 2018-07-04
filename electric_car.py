class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):

        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):

        self.odometer_reading += miles

class ElectricCar(Car):

    def __init__(self, make, model, year, battery=None):
        # self.power = power
        super().__init__(make, model, year)

        self.battery = battery

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()


my_tesla = ElectricCar('tesla', 'model s', 2017)
print(my_tesla.get_descriptive_name())

my_bmw = ElectricCar('bmw', 'model s', 2013)
print(my_bmw.get_descriptive_name())


class Battery:
    def __init__(self, battery_size=85):
        """sadsad"""
        self.battery_size = battery_size

    def describe_battery(self):

        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):

        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."

        print(message)

    def upgrade_battery(self, range):
        if range != 270:
            self.battery_size == 85


battery = Battery()
my_el_tesla = ElectricCar('electesla', 'model s', 1980, battery=battery)
my_el_tesla.battery.get_range()
my_el_tesla.battery.upgrade_battery(240)
my_el_tesla.battery.get_range()
