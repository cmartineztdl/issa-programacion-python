# 05-exercise-03
# 1. Create a program that prints the sum of all numbers in a range.
# - 1->10, result: 55 (1+2+3+4+5+6+7+8+9+10)
# - 3->20, result: 207
# - 67->100, result: 2839

total = 0
for i in range(10):
    total = total + i

print("Result 1:", total)

total = 0
for i in range(3, 20 + 1):
    total = total + i

print("Result 2:", total)

total = 0
for i in range(67, 100 + 1):
    total = total + i

print("Result 3:", total)