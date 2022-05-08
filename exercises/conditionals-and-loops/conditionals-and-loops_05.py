# Exercise 5: Display Numbers from a List

# Write a program to display only those numbers from a list that satisfy the following conditions:

# - The number must be divisible by five
# - If the number is greater than 150, then skip it and move to the next number
# - If the number is greater than 500, then stop the loop

# Given:
# numbers = [12, 75, 150, 180, 145, 525, 50]

# Expected output:
# 75
# 150
# 145

numbers = [12, 75, 150, 180, 145, 525, 50]

for number in numbers:
    if number % 5 == 0 and number <= 150:
        print(number)
    if number > 500:
        break