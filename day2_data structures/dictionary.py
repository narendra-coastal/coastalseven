# examples of dictionaries
# creating a dictionary
employe = {
    "name": "Rahul",
    "age": 22,
    "role": "developer"
}

print(employe)

# accessing values
employe = {
    "name": "narendra",
    "age": 25
}

print(employe["name"])
print(employe["age"])

#adding new items
employe = {
    "name": "nani",
    "age": 20
}

employe["city"] = "Hyderabad"

print(employe)

# updating values
employe = {
    "name": "sai",
    "age": 25
}

employe["age"] = 26

print(employe)

# removing item
employe = { 
    "name": "hari",
    "age": 25
}
employe.pop("age")
print(employe)

# nested dictionary
students = {
    "student1": {
        "name": "Rahul",
        "age": 20
    },
    "student2": {
        "name": "Priya",
        "age": 22
    }
}

print(students["student2"]["name"])