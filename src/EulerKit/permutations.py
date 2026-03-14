import math
import listtools as lt


    

def countPermutations(n):
    if isinstance(n, list) or isinstance(n, str):
        return math.factorial(len(n))
    elif isinstance(n, int):
        return math.factorial(len(str(abs(n))))
    
def permutations_recursive(n:list):
    pass
    #to implement later...
    

        
if __name__ == "__main__":
    # permutations_basic(123)