class Book:
    def __init__(self, t, p):
        self.title = t
        self.price = p
    def printPrice(self, num):
        print(self.title+':', num, '册', self.price*num, '日元')

class ColorBook(Book):   # 超类
    color = '紫'
    def printPrice(self, num):
        # print(self.title + ':', num, '册', self.price * num, '日元')
        super(ColorBook, self).printPrice(num) # 如上调用超类的方法
        print(self.color)

book2 = ColorBook('绘卷', 1680)
book2.printPrice(2)