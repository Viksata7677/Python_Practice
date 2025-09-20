from advanced_module.oop.restaurant.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.50

    def __init__(self, name, price, caffeine: float):
        super().__init__(name, price)
        self.__caffeine = caffeine

    @property
    def __caffeine(self):
        return self.caffeine

    @__caffeine.setter
    def __caffeine(self, value):
        if not value:
            raise ValueError("Enter caffeine")
        self.__caffeine = value
