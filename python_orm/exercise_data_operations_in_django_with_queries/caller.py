import os
from pydoc import describe

import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom, Character


# Create queries within functions


def create_pet(name: str, species: str):
    pet = Pet.objects.create(name=name, species=species)
    return f"{pet.name} is a very cute {pet.species}!"


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    artifact = Artifact()
    artifact.name = name
    artifact.origin = origin
    artifact.age = age
    artifact.description = description
    artifact.is_magical = is_magical

    artifact.save()

    return f"The artifact {artifact.name} is {artifact.age} years old!"


def rename_artifact(artifact: Artifact, new_name: str):
    if artifact.is_magical and artifact.age > 250:
        artifact.name = new_name
        artifact.save()


def delete_all_artifacts():
    Artifact.objects.all().delete()


def show_all_locations():
    result = []
    locations = Location.objects.all().order_by('-id')

    for location in locations:
        result.append(f'{location.name} has a population of {location.population}!')

    return '\n'.join(result)


def new_capital():
    location = Location.objects.first()
    location.is_capital = True
    location.save()


def get_capitals():
    capitals = Location.objects.filter(is_capital=True)
    return capitals.values('name')


def delete_first_location():
    location = Location.objects.first()
    location.delete()


def apply_discount():
    cars = Car.objects.all()

    for car in cars:
        percentage_off = sum(int(digit) for digit in str(car.year))
        discount = float(car.price) * (percentage_off / 100)
        car.price_with_discount = float(car.price) - discount
        car.save()


def get_recent_cars():
    cars_after_2020 = Car.objects.filter(year__gt=2020)
    return cars_after_2020.values('model', 'price_with_discount')


def delete_last_car():
    Car.objects.last().delete()


def show_unfinished_tasks():
    unfinished_tasks = Task.objects.filter(is_finished=False)

    return '\n'.join(
        f"Task - {ut.title} needs to be done until {ut.due_date}!" for ut in unfinished_tasks)


def complete_odd_tasks():
    tasks = Task.objects.all()
    for task in tasks:
        if task.id % 2 == 1:
            task.is_finished = True

        Task.objects.bulk_update(tasks, ['is_finished'])


def encode_and_replace(text: str, task_title: str):
    decoded_text = ''.join(chr(ord(symbol) - 3) for symbol in text)
    Task.objects.filter(title=task_title).update(description=decoded_text)


def get_deluxe_rooms():
    deluxe_rooms = HotelRoom.objects.filter(room_type='Deluxe')

    return '\n'.join(f"Deluxe room with number {dr.room_number} costs {dr.price_per_night}$ per night!"
            for dr in deluxe_rooms if dr.id % 2 == 0)


def increase_room_capacity():
    rooms = HotelRoom.objects.all().order_by('id')

    previous_room_capacity = None

    for room in rooms:
        if not room.is_reserved:
            continue

        if previous_room_capacity is not None:
            room.capacity += previous_room_capacity
        else:
            room.capacity += room.id

        previous_room_capacity = room.capacity

    HotelRoom.objects.bulk_update(rooms, ['capacity'])


def reserve_first_room():
    first_room = HotelRoom.objects.first()
    first_room.is_reserved = True
    first_room.save()


def delete_last_room():
    last_room = HotelRoom.objects.last()

    if not last_room.is_reserved:
        last_room.delete()


def update_characters():
    for char in Character.objects.all():
        if char.class_name == 'Mage':
            char.level += 3
            char.intelligence -= 7
        elif char.class_name == 'Warrior':
            char.hit_points /= 2
            char.dexterity += 4
        else:
            char.inventory = 'The inventory is empty'

        char.save()


def fuse_characters(first_character: Character, second_character: Character):
    mega_character = Character()
    mega_character.name = f"{first_character.name} {second_character.name}"
    mega_character.class_name = 'Fusion'

    mega_character.level = abs(int((first_character.level + second_character.level) // 2))
    mega_character.strength = abs(int((first_character.strength + second_character.strength) * 1.2))
    mega_character.dexterity = abs(int((first_character.dexterity + second_character.dexterity) * 1.4))
    mega_character.intelligence = abs(int((first_character.intelligence + second_character.intelligence) * 1.5))

    mega_character.hit_points = (first_character.hit_points + second_character.hit_points)
    if first_character.class_name in ['Mage', 'Scout']:
        mega_character.inventory = "Bow of the Elven Lords, Amulet of Eternal Wisdom"
    else:
        mega_character.inventory = "Dragon Scale Armor, Excalibur"
    mega_character.save()

    first_character.delete()
    second_character.delete()


def grand_dexterity():
    characters = Character.objects.all()
    for char in characters:
        char.dexterity = 30

    Character.objects.bulk_update(characters, ['dexterity'])


def grand_intelligence():
    characters = Character.objects.all()
    for char in characters:
        char.intelligence = 40

    Character.objects.bulk_update(characters, ['intelligence'])


def grand_strength():
    characters = Character.objects.all()
    for char in characters:
        char.strength = 50

    Character.objects.bulk_update(characters, ['strength'])


def delete_characters():
    chars_to_delete = Character.objects.filter(inventory='The inventory is empty')

    for char in chars_to_delete:
        char.delete()