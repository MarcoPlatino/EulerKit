import listtools as lt

def containSameDigits(x, y):
    xList = lt.numberToList(x)
    yList = lt.numberToList(y)


    
    if not len(xList) == len(yList):
        return False

    xFreq = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in xList:
        xFreq[i] += 1
        
    yFreq = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in yList:
        yFreq[i] += 1

    return xFreq == yFreq
