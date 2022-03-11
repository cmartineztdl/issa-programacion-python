# Conditionals and Loops Exercises

## Exercise 1: First 10 Natural Numbers

Print First 10 natural numbers using while loop.

Expected result:

```
1
2
3
4
5
6
7
8
9
10
```

## Exercise 2: Print the Pattern

Write a program to print the following number pattern using a loop:

```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

## Exercise 3: Calculate the Sum

Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number.

For example, if the user entered `10` the output should be `55 (1+2+3+4+5+6+7+8+9+10)`.

## Exercise 4: Multiplication table

Write a program to print multiplication table of a given number.

For example, `num = 2` so the output should be:

```
2
4
6
8
10
12
14
16
18
20
```

## Exercise 5: Display Numbers from a List

Write a program to display only those numbers from a list that satisfy the following conditions:

- The number must be divisible by five
- If the number is greater than 150, then skip it and move to the next number
- If the number is greater than 500, then stop the loop

Given:

```
numbers = [12, 75, 150, 180, 145, 525, 50]
```

Expected output:

```
75
150
145
```

## Exercise 6: Number of Digits in a Number

Write a program to count the total number of digits in a number using a while loop.

For example, the number is `75869`, so the output should be `5`.

## Exercise 7: The Reverse Pattern

Write a program to use for loop to print the following reverse number pattern

```
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
```

## Exercise 8: Reverse List

Print list in reverse order using a loop
Given:

```
list1 = [10, 20, 30, 40, 50]
```

Expected output:

```
50
40
30
20
10
```

## Exercise 9: Negative Numbers

Display numbers from -10 to -1 using for loop
Expected output:

```
-10
-9
-8
-7
-6
-5
-4
-3
-2
-1
```

## Exercise 10: loop-else

Use `else` block to display a message "Done" after successful execution of for loop.

For example, the following loop will execute without any error.

Given:

```python
for i in range(5):
    print(i)
```

Expected output:

```
0
1
2
3
4
Done!
```

## Exercise 11: Prime Numbers

Write a program to display all prime numbers within a range.

> Note: A Prime Number is a number that cannot be made by multiplying other whole numbers. A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.

Examples:

6 is not a prime mumber because it can be made by 2×3 = 6
37 is a prime number because no other whole numbers multiply together to make it.
Given:

```python
# range
start = 25
end = 50
```

Expected output:

```
Prime numbers between 25 and 50 are:
29
31
37
41
43
47
```

## Exercise 12: Fibonacci Series

Display Fibonacci series up to 10 terms.
The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it. The first two numbers are 0 and 1.

For example, `0, 1, 1, 2, 3, 5, 8, 13, 21`. The next number in this series above is `13+21 = 34`.

Expected output:

```
Fibonacci sequence:
0  1  1  2  3  5  8  13  21  34
```

## Exercise 13: Factorial

Write a program to use the loop to find the factorial of a given number.

The factorial (symbol: !) means to multiply all whole numbers from the chosen number down to 1.

For example: calculate the factorial of 5

```
5! = 5 × 4 × 3 × 2 × 1 = 120
```

Expected output:

```
120
```

## Exercise 14: Reverse the number

Reverse a given integer number.
Given:

```
76542
```

Expected output:

```
24567
```

## Exercise 15: Odd positions

Use a loop to display elements from a given list present at odd index positions
Given:

```
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
```

Note: list index always starts at 0

Expected output:

```
20 40 60 80 100
```

## Exercise 16: The Cube of the Numbers

Calculate the cube of all numbers from 1 to a given number.
Write a program to rint the cube of all numbers from 1 to a given number.

Given:

```
input_number = 6
```

Expected output:

```
Current Number is : 1  and the cube is 1
Current Number is : 2  and the cube is 8
Current Number is : 3  and the cube is 27
Current Number is : 4  and the cube is 64
Current Number is : 5  and the cube is 125
Current Number is : 6  and the cube is 216
```

## Exercise 17: Find the Sum

Find the sum of the series upto `n` terms.

Write a program to calculate the sum of series up to `n` term. For example, if `n = 5` the series will become `2 + 22 + 222 + 2222 + 22222 = 24690`

Given:

```python
# number of terms
n = 5
```

Expected output:

```
24690
```

## Exercise 18: Print the following pattern

Write a program to print the following start pattern using the for loop.

```
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
```
