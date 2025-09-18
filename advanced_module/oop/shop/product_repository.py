from advanced_module.oop.shop.drink import Drink
from advanced_module.oop.shop.food import Food
from advanced_module.oop.shop.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name):
        self.products.remove(product_name)

    def __repr__(self):
        return "\n".join([f"{product.name}: {product.quantity}" for product in self.products])

food = Food("apple")

drink = Drink("water")

repo = ProductRepository()

repo.add(food)

repo.add(drink)

print(repo.products)

print(repo.find("water"))

repo.find("apple").decrease(5)

print(repo)