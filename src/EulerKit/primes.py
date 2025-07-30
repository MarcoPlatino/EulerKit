#My custom library for various functions that I use a lot when I am solving problems on project Euler
#Currently I have functions for everything from a loading screen - For when I am running something somewhat inefficient and need to indicate that something is happening
# I also seem to always be trying to generate a large amount of prime numbers, so I included files for generating a list of primes,
# and also included function to generate file of primes, because then I will be able to pre-generate primes.
import math



def makePrimeList(x:int, y:int) -> list:
    sieve = [True] * (y + 1)
    sieve[0] = sieve[1] = False
    for start in range(2, int(math.sqrt(y)) + 1):
        if sieve[start]:
            for multiple in range(start * start, y + 1, start):
                sieve[multiple] = False
        # print(start)
    return [num for num in range(x, y + 1) if sieve[num]]

def makePrimeFile(x:int, y:int, path:str = "/home/marco/1MillionPrimes.txt") -> str:
    sieve = [True] * (y + 1)
    sieve[0] = sieve[1] = False
    for start in range(2, int(math.sqrt(y)) + 1):
        if sieve[start]:
            for multiple in range(start * start, y + 1, start):
                sieve[multiple] = False
    primes = [num for num in range(x, y + 1) if sieve[num]]

    with open(path, "w") as f:
        for i in primes:
            f.write(f"{i}\n")
    
    return path

def isPrime(number):
    if number <= 1:
        return False
    for i in range(2, int((number ** 0.5))):
        if number % i == 0:
            return False
    return True

def findPrimeFactors(n: int, type:str = "set"):
    type = type.lower()
    if type == "set":
        if n == 1:
            return set()
        elif n % 2 == 0:
            return {2} | findPrimeFactors(n//2)
        else:
            d = 3
            limit = int(n**0.5)
            while d <= limit:
                if n % d == 0:
                    return {d} | findPrimeFactors(n//d)
                d += 2
            return {n}
    elif type == "list":
        if n == 1:
            return []
        elif n % 2 == 0:
            return [2] + findPrimeFactors(n//2, "list")
        else:
            d = 3
            limit = int(n**0.5)
            while d <= limit:
                if n % d == 0:
                    return [d] + findPrimeFactors(n//d, "list")
                d += 2
            return [n]
    else:
        return "Invalid Type"
