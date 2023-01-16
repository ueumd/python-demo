"""
继承
"""

class Car():
     """一次模拟汽车的简单尝试"""
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

     def fill_gas_tank(self):
         print("need a gas tank!")

# 继承Car类
class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):

        """初始化父类"""
        super().__init__(make, model, year)

    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print("This car doesn't need a gas tank!")

tesla = ElectricCar('tsla', 'model s', 2016)
print(tesla.get_descriptive_name())
tesla.fill_gas_tank()