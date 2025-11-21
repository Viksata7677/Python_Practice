from advanced_module.oop.computer_store.computer_types.computer import Computer


class DesktopComputer(Computer):
    processors = {
        "AMD Ryzen 9 5950X": 900,
        "Intel Core i9-11900H": 1050,
        "Apple M1 Pro": 1200
    }
    max_ram = 128

    def __init__(self, manufacturer, model):
        super().__init__(manufacturer, model)
        self.processor = None
        self.ram = None
        self.price = 0

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.processors:
            raise ValueError(f"{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")

        if ram > self.max_ram:
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")

        self.processor = processor
        processor_price = self.processors[processor]
        self.ram = ram
        ram_power = ram.bit_length() - 1
        ram_price = ram_power * 100
        self.price = processor_price + ram_price

        return f"Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$."