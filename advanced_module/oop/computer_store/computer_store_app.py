from advanced_module.oop.computer_store.computer_types.desktop_computer import DesktopComputer
from advanced_module.oop.computer_store.computer_types.laptop import Laptop


class ComputerStoreApp:
    def __init__(self):
        self.warehouse = []
        self.profits = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in ["Desktop Computer", "Laptop"]:
            raise ValueError("Not a valid type computer!")

        if type_computer == "Desktop Computer":
            computer = DesktopComputer(manufacturer, model)
        else:
            computer = Laptop(manufacturer, model)

        configuration = computer.configure_computer(processor, ram)
        self.warehouse.append(computer)

        self.profits += computer.price
        return configuration

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        for computer in self.warehouse:
            if computer.price <= client_budget and computer.processor == wanted_processor and computer.ram >= wanted_ram:
                profit = client_budget - computer.price
                self.warehouse.remove(computer)
                self.profits += profit
                return (f"{computer.manufacturer} {computer.model} "
                        f"with {computer.processor} and {computer.ram}GB RAM "
                        f"sold for {client_budget}$.")

        raise Exception("Sorry, we don't have a computer for you.")




computer_store = ComputerStoreApp()

print(computer_store.build_computer("Laptop", "Apple", "Macbook", "Apple M1 Pro", 64))

print(computer_store.sell_computer(10000, "Apple M1 Pro", 32))