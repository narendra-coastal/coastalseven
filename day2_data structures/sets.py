# example for sets
# Creating a set
numbers = {1, 2, 3, 4}

print(numbers)


a = {10, 20, 30}
b = {40,50, 60} 
print(a)
print(b)
print(type(a))
print(type(b))

# Duplicate Values are Removed
# Duplicates are removed automatically

data = {1, 2, 2, 3, 4, 4, 5, 5 ,5, 6, 6}

print(data)
 
# Common Set Operations 

# adding element
courses = {"python", "java", "html", "node.js"}

courses.add("AI/ML")

print(courses)

# removing Elements
#Use remove() or discard()

ourses = {"python", "java", "html", "node.js"}

courses.remove("java")

print(courses)

# intersection of set
a = {1, 2, 3}
b = {2, 3, 4}
i = a.intersection(b)
print(i)

# clearing a set
s = {1, 2, 3}
s.clear()
print(s)



