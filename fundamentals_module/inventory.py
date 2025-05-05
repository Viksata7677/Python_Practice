class Inventory:
    def __init__(self, __capacity):
        self.__capacity = __capacity
        self.items = []

    def add_item(self, item):
        if self.__capacity > len(self.items):
            self.items.append(item)
        return "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        items = ", ".join(self.items)
        left_capacity = self.__capacity - len(items)
        if left_capacity < 0:
            left_capacity = 0
        return f"Items: {items}.\nCapacity left: {left_capacity}"

inventory = Inventory(2)

inventory.add_item("potion")

inventory.add_item("sword")

print(inventory.add_item("bottle"))

print(inventory.get_capacity())

print(inventory)