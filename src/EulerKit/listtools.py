def numberToList(number):
    return [int(x) for x in str(number)]

def listToNumber(data, check=False, customErrorMessage = "This data has a string in it"):
    result = 0
    if check:
        for i in data:
            if type(i) == str:
                return customErrorMessage
    for i in data:
        result = result*10 + i
    return result

if __name__ == "__main__":
    print(listToNumber([1, 2, '3', 4], True, ['n','o']))