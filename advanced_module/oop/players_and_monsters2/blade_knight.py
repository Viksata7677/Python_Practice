from players_and_monsters2.dark_knight import DarkKnight
from players_and_monsters2.elf import Elf
from players_and_monsters2.hero import Hero


class BladeKnight(DarkKnight):
    pass

hero = Hero("H", 4)

print(hero.username)

print(hero.level)

print(str(hero))

elf = Elf("E", 4)

print(str(elf))

print(elf.__class__.__bases__[0].__name__)

print(elf.username)

print(elf.level)