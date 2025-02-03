# List Comprehension
numbers = [x for x in range(10) if x % 2 == 0]
print("Even numbers:", numbers)

# Dictionary Comprehension
squares = {x: x ** 2 for x in range(5)}
print("Squares dictionary:", squares)

# Set Comprehension
unique_chars = {char for char in "hello world" if char != " "}
print("Unique characters:", unique_chars)

# Generator Comprehension
gen_exp = (x ** 2 for x in range(5))
print("Generator output:", list(gen_exp))  # Convert generator to list for printing
