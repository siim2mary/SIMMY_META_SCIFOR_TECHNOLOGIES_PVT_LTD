def cube_numbers(numbers):
    # Use map and lambda to cube each number in the list
    cubed_numbers = list(map(lambda x: x ** 3, numbers))
    return cubed_numbers

# Example usage
numbers = [2, 3, 4, 5, 6]
cubed_numbers = cube_numbers(numbers)
print(cubed_numbers)
