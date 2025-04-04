text = input()
loop = [i for i in text if i.lower() not in ['a', 'e', 'i', 'o', 'u']]
print(''.join(loop))