a = input()

if a < 'Z':
    a = ord(a) + 1
    print(chr(a))
else:
    print('A')