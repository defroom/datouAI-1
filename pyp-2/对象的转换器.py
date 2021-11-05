class Book:
    def __init__(self, t, p):
        self.title = t
        self.price = p
    def printPrice(self, num):
        print(self.title+':', num, '册', self.price*num, '日元')

book1 = Book('绘卷', 1680)
book1.printPrice(3)

book2 = Book('词典', 2000)
book2.printPrice(2)