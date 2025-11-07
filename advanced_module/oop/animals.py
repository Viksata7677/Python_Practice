from abc import ABC


class Animal(ABC):

    def make_sound(self):
        pass


class Cat(Animal):

    def make_sound(self):
        print("Meow")


class Dog(Animal):

    def make_sound(self):
        print("woof-woof")


class Chicken(Animal):

    def make_sound(self):
        print('cluck cluck')


def animal_sound(animals: list):
    for animal in animals:
        animal.make_sound()


animals = [Cat(), Dog(), Chicken()]
animal_sound(animals)



