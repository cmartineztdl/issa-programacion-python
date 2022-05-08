# Exercise 6: Number of Digits in a Number

# Write a program to count the total number of digits in a number using a while loop.

# For example, the number is `75869`, so the output should be `5`.

number = 758695

i = 1
total = 0
while True:
    total = total + 9 * pow(10, i - 1)
    if(number < total):
        print("Digits:", i)
        break
    i = i +1