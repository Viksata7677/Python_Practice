from shop2.drink import Drink
from shop2.food import Food
from shop2.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)

    def __repr__(self):
        product_info = {}
        for product in self.products:
            product_info[product.name] = product.quantity
        return f"{'\n'.join(f'{name}: {quantity}' for name, quantity in product_info.items())}"

food = Food("apple")

drink = Drink("water")

repo = ProductRepository()

repo.add(food)

repo.add(drink)

print(repo.products)

print(repo.find("water"))

repo.find("apple").decrease(5)

print(repo)