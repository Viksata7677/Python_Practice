def age_assignment(*names, **letter_age):
    result = []

    for letter, age in letter_age.items():
        for name in names:
            if name[0] == letter:
                result.append(f"{name} is {age} years old.")

    return "\n".join(sorted(result))

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))