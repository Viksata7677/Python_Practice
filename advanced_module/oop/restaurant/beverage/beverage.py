from advanced_module.oop.restaurant.product import Product


class Beverage(Product):
    def __init__(self, name, price, milliliters):
        super().__init__(name, price)
        self.__milliliters = milliliters

    @property
    def __milliliters(self):
        return self.milliliters

    @__milliliters.setter
    def __milliliters(self, value):
        if not value:
            raise ValueError("Enter milliliters")
        self.milliliters = value
