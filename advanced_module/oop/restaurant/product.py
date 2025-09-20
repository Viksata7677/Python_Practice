class Product:
    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Enter name!")
        self.__name = value

    @property
    def __price(self):
        return self.price

    @__price.setter
    def __price(self, value):
        if not value:
            raise ValueError("Enter price!")
        self.price = value
