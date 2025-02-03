# Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello, file handling!")

# Reading from a file
with open("sample.txt", "r") as file:
    content = file.read()
    print("File content:", content)