# types of list

a = [1, 2, 3, 4,5]

b = ["apple", "banana","mango"]
c = ["coastal","tcs","hcl"]
print (a)
print (b)
print (c)

a = list((1, 2, 3, 'apple', 4.5))  
print(a)

b = list("coastal")
print(b)

a = [2] * 5
b = [0] * 7

print(a)
print(b)

a = [1, 2]
a.append(3)
print(a)

a = [1, 3]
a.insert(1, 2)
print(a)

a = [1, 2]
a.extend([3, 4])
print(a)

a = [1, 2, 3]
a.remove(2)
print(a)

a = [1, 2, 3]
a.pop()
print(a)

a = [1, 2, 3]
del a[1]
print(a)

a = [1, 2, 3]
a.clear()
print(a)

