# 05-exercise-04
# 1. Create a program that gets the factorial of a number.
# - 5! = 5 × 4 × 3 × 2 × 1 = 120
# - 7! = 7 x 6 x 5 × 4 × 3 × 2 × 1 = 5040

total = 1
for i in range(1, 5 + 1):
    total = total * i

print("Result 1:", total)

total = 1
for i in range(1, 7 + 1):
    total = total * i

print("Result 2:", total)
