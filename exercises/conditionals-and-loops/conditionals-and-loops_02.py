# Exercise 2: Print the Pattern

# Write a program to print the following number pattern using a loop:

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

number = 5

for j in range(1, number + 1):
    line = ""
    for i in range(1, j + 1):
        line = line + str(i) + " "

    print(line)

print("-----------------")

j = 1
while j <= number:
    i = 1
    line = ""
    while i <= j:
        line = line + str(i) + " "
        i = i + 1

    print(line)
    
    j = j + 1