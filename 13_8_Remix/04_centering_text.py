width = int(input())

while True:
    centering = input()
    word_len = len(centering)
    periods = (width - word_len) // 2
    unbalanced_right_side = periods

    if ((width - word_len) % 2) != 0:
        periods += 1
    if centering == 'END':
        break

    print('.' * periods + centering + '.' * unbalanced_right_side)