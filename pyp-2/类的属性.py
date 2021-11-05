class Book:
    def __init__(self, t, p):
        self.title = t
        self.__price = p

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, p):
        self.__price = p

    @price.deleter
    def price(self):
        self.__price = 0
    # price = property(fget=getPrice, fset=setPrice, fdel=delPrice, doc='价格的属性')

book1 = Book('绘卷', 1680)
book1.Price = 2000
print(book1.price)
del(book1.price)