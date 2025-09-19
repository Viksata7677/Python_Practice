from advanced_module.oop.wild_cat_zoo.caretaker import Caretaker
from advanced_module.oop.wild_cat_zoo.cheetah import Cheetah
from advanced_module.oop.wild_cat_zoo.keeper import Keeper
from advanced_module.oop.wild_cat_zoo.lion import Lion
from advanced_module.oop.wild_cat_zoo.tiger import Tiger
from advanced_module.oop.wild_cat_zoo.vet import Vet


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        price = int(price)
        if len(self.animals) < self.__animal_capacity and self.__budget < price:
            return 'Not enough budget'

        if self.__budget >= price and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        else:
            return 'Not enough space for animal'



    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f'{worker.name} the {worker.__class__.__name__} hired successfully'
        else:
            return 'Not enough space for worker'

    def fire_worker(self, worker_name):
        for pos, x in enumerate(self.workers):
            if x.name == worker_name:
                del self.workers[pos]
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        sum_salaries = sum(worker.salary for worker in self.workers)
        if self.__budget >= sum_salaries:
            self.__budget -= sum_salaries
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'
        else:
            return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        money_for_animals = sum(animal.money_for_care for animal in self.animals)
        if self.__budget >= money_for_animals:
            self.__budget -= money_for_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        else:
            return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        info = {"Cheetah": [], "Tiger": [], "Lion": []}
        [info[x.__class__.__name__].append(str(x)) for x in self.animals]
        output = [f"You have {len(self.animals)} animals",
                  f"----- {len(info['Lion'])} Lions:", *info['Lion'],
                  f"----- {len(info['Tiger'])} Tigers:", *info['Tiger'],
                  f"----- {len(info['Cheetah'])} Cheetahs:", *info['Cheetah']]
        return "\n".join(output)

    def workers_status(self):
        info = {"Caretaker": [], "Vet": [], "Keeper": []}
        [info[x.__class__.__name__].append(str(x)) for x in self.workers]
        output = [f"You have {len(self.workers)} workers",
                  f"----- {len(info['Keeper'])} Keepers", *info["Keeper"],
                  f"----- {len(info['Caretaker'])} Caretakers", *info["Caretaker"],
                  f"----- {len(info['Vet'])} Vets", *info["Vet"]]
        return "\n".join(output)






zoo = Zoo("Zootopia", 3000, 5, 8)


# Animals creation

animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1),

Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1),

Lion("Nala", "Female", 4)]


# Animal prices

prices = [200, 190, 204, 156, 211, 140]


# Workers creation

workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95),

Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140),

Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]


# Adding all animals

for i in range(len(animals)):

    animal = animals[i]

    price = prices[i]

    print(zoo.add_animal(animal, price))


# Adding all workers

for worker in workers:

    print(zoo.hire_worker(worker)) # Tending animals

print(zoo.tend_animals())
print(zoo.pay_workers())
print(zoo.fire_worker("Adam"))
print(zoo.animals_status())
print(zoo.workers_status())