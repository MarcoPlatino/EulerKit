import listtools as lt

def containSameDigits(x, y):
    xList = lt.numberToList(x)
    yList = lt.numberToList(y)

    if not len(xList) == len(yList):
        return False
    
    for i in xList:
        if i in yList:
            continue
        return False
    
    return True
