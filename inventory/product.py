class Product:
    def __init__(self, name: str, price: float, amount: int):
        self.__id = id(self)
        self.__name = name
        self.__price = price
        self.__amount = amount

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def amount(self):
        return self.__amount

    def __repr__(self):
        return (
            f"Product(name={self.__name}, price={self.__price}, amount={self.__amount})"
        )
