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