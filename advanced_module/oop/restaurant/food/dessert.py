from advanced_module.oop.restaurant.food.food import Food


class Dessert(Food):
    def __init__(self, name, price, calories: float):
        super().__init__(name, price)
        self.__calories = calories

    @property
    def calories(self):
        return self.__calories

    @calories.setter
    def calories(self, value):
        self.__calories = value
