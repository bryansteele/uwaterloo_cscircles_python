n = int(input())

for x in range(1, n + 1):
    for y in range(1, n + 1):
        if x * y == n:
            print(f"{x} times {y} equals {n}")