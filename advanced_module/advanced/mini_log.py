with open('logs.txt', 'r') as logs, open('info.txt', 'w') as info, open('warnings.txt', 'w') as warnings, open('errors.txt', 'w') as errors:
    for line in logs:
        line = line.strip()
        if not line:
            continue

        if line.startswith('[INFO]'):
            info.write(line + '\n')
        elif line.startswith('[ERROR]'):
            errors.write(line + '\n')
        elif line.startswith('[WARNING]'):
            warnings.write(line + '\n')
