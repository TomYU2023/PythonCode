# 练习
class Item:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return f"{self.name} (占用面积: {self.area}平方米)"

class Home:
    def __init__(self, area, address):
        self.address = address
        self.area = area
        self.containsItems = []
        print("初始化成功")

    def addItem(self, item):
        self.containsItems.append(item)
        if item.area > self.area:
            print("空间不足")
        else:
            self.area -= item.area
            print("添加addItem成功")

    def __str__(self):
        items_str = "；".join(str(item) for item in self.containsItems)
        return f"房子在{self.address}, 剩余面积为{self.area}，已买家具有：{items_str}"


if __name__ == "__main__":
    
    my_home = Home(120, "北京")
    my_home.addItem(Item("沙发", 20))
    my_home.addItem(Item("餐桌", 30))

    print(my_home)

# 看代码要从输出口开始回溯，一般从下往上看，找到传参的函数和变量，再看函数内部的逻辑