class Book:
    title = '绘卷'
    price = 1680
    def printPrice(self, num):
        print(self.title+':', num, '册', self.price*num, '日元')

book1 = Book()
book1.printPrice(2)