from advanced_module.oop.restaurant.food.food import Food


class Dessert(Food):
    def __init__(self, name, price, calories: float):
        super().__init__(name, price)
        self.__calories = calories

    @property
    def __calories(self):
        return self.calories

    @__calories.setter
    def __calories(self, value):
        self.__calories = value

