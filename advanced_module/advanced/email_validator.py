class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


command = input()
valid_domains = ('.com', '.bg', '.net', '.or')
while command != "End":

    if '@' not in command:
        raise MustContainAtSymbolError("Email must contain @")

    name, domain = command.split('@')

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if not command.endswith(valid_domains):
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
    command = input()
