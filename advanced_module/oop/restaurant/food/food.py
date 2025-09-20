from advanced_module.oop.restaurant.product import Product


class Food(Product):
    def __init__(self, name, price, grams):
        super().__init__(name, price)
        self.__grams = grams

    @property
    def __grams(self):
        return self.grams

    @__grams.setter
    def __grams(self, value):
        if not value:
            raise ValueError("Enter grams")
        self.grams = value
