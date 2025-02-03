import json

# Sample dictionary
data = {
    "name": "Alice",
    "age": 25,
    "city": "Berlin"
}

# Writing JSON to a file
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

# Reading JSON from a file
with open("data.json", "r") as file:
    loaded_data = json.load(file)

print("Loaded JSON:", loaded_data)
