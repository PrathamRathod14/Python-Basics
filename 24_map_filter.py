# Using map() and filter()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Squared numbers:", squared)
print("Even numbers:", even_numbers)
