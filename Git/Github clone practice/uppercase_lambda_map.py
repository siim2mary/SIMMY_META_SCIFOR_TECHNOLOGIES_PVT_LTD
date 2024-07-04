def convert_to_uppercase(strings):
    # Use map and lambda to convert each string to uppercase
    uppercase_strings = list(map(lambda x: x.upper(), strings))
    return uppercase_strings

# Example usage
strings = ["hello", "world", "python", "lambda", "map"]
uppercase_strings = convert_to_uppercase(strings)
print(uppercase_strings)
print("The result is:", uppercase_strings)