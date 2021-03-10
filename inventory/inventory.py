from logger import logger


class Inventory:
    def __init__(self):
        self.__products = []
        self.__index = 0

    @logger
    def __getitem__(self, position):
        return self.__products[position]

    @logger
    def __delitem__(self, position):
        del self.__products[position]

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index > len(self.__products) - 1:
            raise StopIteration
        index = self.__index
        self.__index += 1
        return self.__products[index]

    @logger
    def add_product(self, product):
        if product.id:
            self.__products.append(product)
        else:
            raise AttributeError("Inventory accepts only Product as a valid item.")

    @logger
    def total(self):
        return sum(p.price for p in self.__products)
