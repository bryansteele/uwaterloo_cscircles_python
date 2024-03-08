S = input()

for i in range(0, len(S)):
    if S[i] == '+':
        a = int(S[0:i])
        b = int(S[(i + 1):len(S)])
        print(a + b)