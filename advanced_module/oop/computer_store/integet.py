from math import floor


class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return f'value in not float'
        return cls(floor(float_value))

    @classmethod
    def from_roman(cls, roman: str):
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        total = 0
        prev = 0

        for char in reversed(roman):
            current = roman_map[char]
            if current < prev:
                total -= current
            else:
                total += current
            prev = current

        return cls(total)

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return 'wrong type'
        return cls(int(value))


first_num = Integer(10)

print(first_num.value)


second_num = Integer.from_roman("IV")

print(second_num.value)


print(Integer.from_float("2.6"))

print(Integer.from_string(2.6))