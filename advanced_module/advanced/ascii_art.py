from pyfiglet import figlet_format

def print_art(message):
    acii_art = figlet_format(message)
    print(acii_art)

print_art('Hello World!')