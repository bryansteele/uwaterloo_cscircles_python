def prod(L):
    product = 1
    for i in range(0, len(L)):
         product *= L[i]
    return product