shirina = int(input())
duljina = int(input())
pieces = shirina * duljina

while pieces > 0:
    command = input()
    if command == 'STOP' and pieces > 0:
        print(f'{pieces} pieces are left.')
        break
    else:
        broi_parcheta = int(command)
        pieces -= broi_parcheta

if pieces <= 0:
    print(f'No more cake left! You need {abs(pieces)} pieces more.')