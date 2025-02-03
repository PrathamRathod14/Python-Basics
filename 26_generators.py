# Using generators
def generator_example():
    for i in range(3):
        yield i

for value in generator_example():
    print(value)