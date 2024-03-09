letter = input()

if letter >= 'A' and letter <= 'Z':

    print(int(ord(letter)) -64)

else:

    print('invalid')