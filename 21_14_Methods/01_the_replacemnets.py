def replace(list, X, Y):
    while X in list:
        a = 0
        for i in list:
            pos = (len(list)+ a) - ((len(list)))
            if i == X:
                list.insert(pos, Y)
                list.remove(X)
                a += 1 
            elif list.count(X) == 0:
                break
            else:
                a += 1
                continue