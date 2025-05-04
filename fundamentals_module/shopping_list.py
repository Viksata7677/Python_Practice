initial_list = input().split('!')
command = input()

while command != "Go Shopping!":
    parts = command.split()
    if parts[0] == 'Urgent':
        item = parts[1]
        if item not in initial_list:
            initial_list.insert(0, item)
    elif parts[0] == 'Unnecessary':
        item = parts[1]
        if item in initial_list:
            initial_list.remove(item)
    elif parts[0] == 'Correct':
        old_item = parts[1]
        new_item = parts[2]
        if old_item in initial_list:
            index = initial_list.index(old_item)
            initial_list[index] = new_item
    elif parts[0] == 'Rearrange':
        item = parts[1]
        if item in initial_list:
            initial_list.remove(item)
            initial_list.append(item)

    command = input()


print(f"{', '.join(initial_list)}")