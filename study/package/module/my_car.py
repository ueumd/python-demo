"""
从一个模块中导入多个类
从car.py 文件导入 Car 和 ElectricCar类
"""
from car import Car, ElectricCar

# 导入整个模埠
import car

audi = Car("audi", "a8", 2023)
print(audi.get_descriptive_name()) # 2023 Audi A8


tesla = ElectricCar('tesla', 'model s', 2023)
print(tesla.get_descriptive_name()) # 2023 Tesla Model S

tesla.battery.describe_battery()
tesla.battery.get_range()


# 模块名.类名
my_beetle = car.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())