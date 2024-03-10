def isPalindrome(S):
    a = int((len(S)) / 2)
    if S[0:a] == S[:a-1:-1] and len(S) % 2 == 0:
        return True
    elif S[0:a] == S[:a:-1] and len(S) % 2 != 0:
        return True
    else:
        return False



# OR



def isPalindrome(S):
    if str(S) == str(S)[::-1]:
    else:
        return False