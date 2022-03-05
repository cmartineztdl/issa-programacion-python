# 05-exercise-01
# Go through W3school examples.
# 1. https://www.w3schools.com/python/python_while_loops.asp
# 2. https://www.w3schools.com/python/python_for_loops.asp
# Copy/paste the example code in IDLE and make them work

print("*********")
print("* WHILE *")
print("*********")

print("while")

i = 1
while i < 6:
    print(i)
    i += 1

print()
print("while - break")

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

print()
print("while - continue")

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

print()
print("while - else")

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

print("*******")
print("* FOR *")
print("*******")

print("for - array")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

print()
print("for - string")

for x in "banana":
    print(x)

print()
print("for - break - 1")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

print()
print("for - break - 2")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

print()
print("for - continue")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

print()
print("for - range - 1")

for x in range(6):
    print(x)

print()
print("for - range - 2")

for x in range(2, 6):
    print(x)

print()
print("for - range - 3")

for x in range(2, 30, 3):
    print(x)

print()
print("for - else")

for x in range(6):
    print(x)
else:
    print("Finally finished!")

print()
print("for - else - break")

for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished!")  # Not shown if break

print()
print("for - nested loops")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

print()
print("for - pass")

for x in [0, 1, 2]:
    pass
