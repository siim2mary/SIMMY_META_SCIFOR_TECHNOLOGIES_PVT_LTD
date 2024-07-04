def square_numbers(numbers):
    # Use map and lambda to square each number in the list
    squared_numbers = list(map(lambda x: x ** 2, numbers))
    return squared_numbers

# Example usage
numbers = [1, 2, 3, 4, 5]
squared_numbers = square_numbers(numbers)
print(squared_numbers)
print("THE SQUARE OF NOS IS :", squared_numbers)