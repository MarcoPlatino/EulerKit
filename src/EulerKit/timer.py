import time

def timer(func): #You can add this as a decorator when defining functions if you want to measure the time it takes to execute.
    def wrapper(*args, **kwargs):
        startTime = time.time()
        func(*args, **kwargs)
        endTime = time.time()
        print(f'Function \"{func.__name__}\" executed in {(endTime - startTime):.4f} milliseconds')
    return wrapper

class programTimer():
    def __init__(self, verboseOutput = True):
        self.startTime = None
        self.endTime = None
        self.timeElapsed = 0.0
        self.verboseOutput = verboseOutput
        self.finished = False
    
    def start(self):
        self.startTime = time.time
        self.endTime = None
    
    def end(self, handleValue = ""):
        self.finished = True
        self.endTime = time.time
        self.timeElapsed = self.endTime - self.startTime
        match handleValue:
            case "return":
                return self.timeElapsed
            case "print":
                print(self.timeElapsed)
            case "":
                pass

    def __enter__(self):
        self.startTime = time.time()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.endTime = time.time()
        self.timeElapsed = self.endTime - self.startTime

    def __str__(self): #Also __enter__ and __exit__ methods to be added
        if not self.finished:
            if self.verboseOutput: 
                return(f'Time Elapsed: {(time.time - self.startTime):.4f} milliseconds')
            return time.time - self.startTime
        else:
            if self.verboseOutput:
                return(f'Time Elapsed: {(self.timeElapsed):.4f} milliseconds')
            return self.timeElapsed

        
    


if __name__ == "__main__":
    import math

    @timer
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
