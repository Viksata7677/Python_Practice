class Cup:
    def __init__(self, size: int, total_quantity: int):
        self.size = size
        self.total_quantity = total_quantity

    def fill(self, quantity):
        if self.total_quantity + quantity <= self.size:
            self.total_quantity += quantity

    def status(self):
        return self.size - self.total_quantity


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())