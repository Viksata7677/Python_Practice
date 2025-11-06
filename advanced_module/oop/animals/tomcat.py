from advanced_module.oop.animals.cat import Cat
from advanced_module.oop.animals.dog import Dog
from advanced_module.oop.animals.kitten import Kitten


class Tomcat(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, gender="Male")

    def make_sound(self):
        return "Hiss"


kitten = Kitten("Kiki", 1)

print(kitten.make_sound())

print(kitten)

cat = Cat("Johnny", 7, "Male")

print(cat.make_sound())

print(cat)