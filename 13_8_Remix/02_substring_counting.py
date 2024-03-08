a = input()
b = input()
count = 0
sub_len = len(a)

for i in range(len(b)):
    if b[i: i + sub_len] == a:
        count += 1

print(count)