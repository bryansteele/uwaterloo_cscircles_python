a = ord(' ')

for i in range(0, 6):
    print('chr:'+' ', end=' ')
    for j in range(a, a + 16):
        print(chr(j) + '  ', end=' ')
    print()
    print('asc:', end=' ')
    for k in range(a, a + 16):
        if k >= 100:
            print(str(k), end=' ')
        else:
            print(str(k) + ' ', end=' ')
    print()
    a += 16