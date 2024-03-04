a = input()
b = list(a)
b[0], b[len(b) -1] = b[len(b) -1], b[0]
c = ''.join(b)
print(c)