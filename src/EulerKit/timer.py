import time

def timeFunction(func):
    def wrapper(*args, **kwargs):
        startTime = time.time()
        func(*args, **kwargs)
        endTime = time.time()
        print(f'Function: {func.__name__} executed in {(endTime - startTime):.4f} milliseconds')
    return wrapper

if __name__ == "__main__":
    import math

    @timeFunction
    def slow_prime_check(n):
        primes = []
        for num in range(2, n):
            is_prime = True
            for i in range(2, int(math.sqrt(num)) + 1):
                # Unnecessary extra checks for no good reason
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)

    slow_prime_check(500000)
