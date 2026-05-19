# comprehensions in Python
#[expression for item in iterable if condition]

# example square of numbers
numbers = [1, 2, 3, 4, 5]

squares = [x*x for x in numbers]

print(squares)

# example even numbers
evens = [x for x in range(10) if x % 2 == 0]

print(evens)