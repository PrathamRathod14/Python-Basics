# Using lambda functions

# 1. Basic Lambda Function
square = lambda x: x * x
print("Square of 5:", square(5))

# 2. Lambda with Multiple Parameters
add = lambda x, y: x + y
print("Sum of 5 and 3:", add(5, 3))

# 3. Lambda Inside a Function
def multiplier(n):
    return lambda x: x * n

double = multiplier(2)
triple = multiplier(3)
print("Double of 4:", double(4))
print("Triple of 4:", triple(4))

# 4. Lambda with List Sorting
points = [(2, 3), (1, 2), (5, 1), (3, 4)]
points.sort(key=lambda point: point[1])
print("Points sorted by second element:", points)

# 5. Lambda with Map
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print("Squared numbers using map:", squared_numbers)

# 6. Lambda with Filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using filter:", even_numbers)

# 7. Lambda with Reduce
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print("Product of numbers using reduce:", product)

# 8. Lambda with Conditional Logic
max_of_two = lambda x, y: x if x > y else y
print("Max of 10 and 20:", max_of_two(10, 20))

# 9. Lambda with List Comprehension
cubed_numbers = [(lambda x: x ** 3)(n) for n in range(1, 6)]
print("Cubed numbers using list comprehension:", cubed_numbers)

# 10. Lambda for String Operations
capitalize_words = lambda s: " ".join([word.capitalize() for word in s.split()])
sentence = "hello world from python"
print("Capitalized sentence:", capitalize_words(sentence))
