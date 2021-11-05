class Fruit():
    taste = '好吃!'
    def __init__(self):
            self.name = '水果'
            self.weight = 0
            self.color = '?'

    def printData(self):
        print('{}:颜色={}重量={}g'.format(self.name, self.color, self.weight))

class Apple(Fruit):
    def __init__(self, name, weight, color):
        self.name = name
        self.weight = weight
        self.color = color

    @classmethod
    def printTaste(cls):
        print('甜甜的' + cls.taste)

class Orange(Fruit):
    def __init__(self, weight):
        self.name = '橙子'
        self.weight = weight
        self.color = '橙色'

    @classmethod
    def printTaste(cls):
        print('酸酸的' + cls.taste)

fruit = Fruit()
fruit.printData()

red_apple = Apple(name='红苹果', weight=280, color='红')
red_apple.printData()
Apple.printTaste()

green_apple = Apple(name='青苹果', weight=280, color='青')
green_apple.printData()
Apple.printTaste()

orange = Orange(160)
orange.printData()
orange.printTaste()