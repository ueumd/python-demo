class Car():
 def __init__(self, make, model, year):
     """初始化描述汽车的属性"""
     self.make = make
     self.model = model
     self.year = year
     self.odometer_reading = 0

 def get_descriptive_name(self):
     """返回整洁的描述性名称"""
     long_name = str(self.year) + ' ' + self.make + ' ' + self.model
     return long_name.title()