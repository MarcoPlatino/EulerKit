def pandigital(number):
    number_str = str(number)
    digits = set(number_str)
    target = set(str(i) for i in range(1, len(number_str) + 1))
    return target == digits