# 封装特性
'''
1. 封装性：封装了类的属性和方法，使得类的使用者可以无需了解类的内部实现，只通过调用类的方法来使用类的功能。
2. 私有性：私有属性和方法只能在类的内部使用，外部无法访问。
3. 继承性：继承了基类的属性和方法，使得派生类可以继承基类的功能，并添加新的功能。
'''

# 基类 Vehicle
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand  # 品牌
        self.model = model  # 型号

    def display_info(self):
        return f"This is a {self.brand} {self.model}."

# 派生类 Car
class Car(Vehicle): # 继承自基类 Vehicle
    '''
    说明：继承自基类 Vehicle，添加了属性 horsepower 和方法 display_info()
    '''
    def __init__(self, brand, model, horsepower):
        super().__init__(brand, model) # super() 调用基类的构造函数，表示继承基类的属性和方法
        self.horsepower = horsepower  

    def display_info(self):
        return f"{super().display_info()} It has {self.horsepower} horsepower."

# 派生类 Bike
class Bike(Vehicle): # 继承自基类 Vehicle
    '''
    说明：继承自基类 Vehicle，添加了属性 type 和方法 display_info()
    '''
    def __init__(self, brand, model, type):
        super().__init__(brand, model)
        self.type = type  # 自行车类型，如山地车等

    def display_info(self):
        return f"{super().display_info()} It is a {self.type} bike."

# 多态性的实现
def print_vehicle_info(vehicle):
    print(vehicle.display_info())

# 创建不同的交通工具实例
my_car = Car("Tesla", "Model S", 539)
my_bike = Bike("Giant", "Escape 2", "city")

# 使用同一个函数展示不同的交通工具信息
print_vehicle_info(my_car)
print_vehicle_info(my_bike)

# __doc__ 属性: 获取类的文档字符串
print(Car.__doc__)
print(Bike.__doc__)

# __name__ 属性: 获取类的名称
print(Car.__name__)
print(Bike.__name__)

# __module__ 属性: 获取类的模块名称
print(Car.__module__)
print(Bike.__module__)