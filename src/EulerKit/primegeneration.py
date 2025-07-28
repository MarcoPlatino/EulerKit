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

    with open("path", "w") as f:
        for i in primes:
            f.write(f"{i}\n")
    
    return path
