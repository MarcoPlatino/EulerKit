import math
import listtools as lt

def generatePermutations(n): #This can only be used with smaller data sets...
    perms = []
    def permHelper(end, start = ""):
        if (len(end) <= 1):
            perms.append(start + end)
        else:
            for i in range(len(end)):
                if (end[i:i+1] in end[0:i]):
                    continue
                permHelper(end[0:i] + end[i+1:], start + end[i:i+1])

    permHelper(n)
    return perms

    

def countPermutations(n):
    if isinstance(n, list) or isinstance(n, str):
        return math.factorial(len(n))
    elif isinstance(n, int):
        return math.factorial(len(str(abs(n))))
    
def permutations_recursive(n:list):
    pass
    #to implement later...
    

        
if __name__ == "__main__":
    print(generatePermutations("123456789"))