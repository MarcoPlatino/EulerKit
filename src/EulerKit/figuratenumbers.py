def generateFigurateNumbers(lower:int, upper:int, type:str) -> list:
    numbers = []
    type = type.lower()
    match type:
        case "triangular":
            for i in range(lower, upper + 1):
                numbers.append(i * (i + 1) // 2)
            return numbers
        case "square":
            for i in range(lower, upper + 1):
                numbers.append(i ** 2)
            return numbers
        case "pentagonal":
            for i in range(lower, upper):
                numbers.append(i * ((3 * i) - 1) // 2)
            return numbers
        case "hexagonal":
            for i in range(lower, upper):
                numbers.append(i * ((2 * i) - 1))
            return numbers
        case "heptagonal":
            for i in range(lower, upper):
                numbers.append(i * ((5 * i) - 3) // 2)
            return numbers
        case "octagonal":
            for i in range(lower, upper):
                numbers.append(i * ((3 * i) - 2))
            return numbers
        case "cubic":
            for i in range(lower, upper):
                numbers.append(i ** 3)
            return numbers
        case "tetrahedal":
            for i in range(lower, upper):
                numbers.append(i * (i + 1) * (i + 2) // 6)
            return numbers
        case _:
            return ["Invalid Type"]

# Tests here
# if __name__ == "__main__":
#     print(generateFigurateNumbers(1, 10, "triangular"))
#     print(generateFigurateNumbers(1, 10, "square"))
#     print(generateFigurateNumbers(1, 10, "pentagonal"))
#     print(generateFigurateNumbers(1, 10, "hexagonal"))
#     print(generateFigurateNumbers(1, 10, "heptagonal"))
#     print(generateFigurateNumbers(1, 10, "octagonal"))
#     print(generateFigurateNumbers(1, 10, "cubic"))
#     print(generateFigurateNumbers(1, 10, "tetrahedal"))

