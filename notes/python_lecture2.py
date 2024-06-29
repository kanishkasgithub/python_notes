# -*- coding: utf-8 -*-
"""python lecture2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1O7Ie-5iopJqfxqJxbog_5ODHs5sdX0MM

Topics covered:

1.   Operators in python
2.   If-else statement
3.   Modules
4.   Loops

# 1. Operators in python

1. Arithmetic Operators
2. Relational Operators
3. Logical Operators
4. Bitwise Operators
5. Assignment Operators
6. Membership Operators
"""

# Arithmetic operators
print(5+2)
print(5-2)
print(5*2)
print(5/2)
print(5//2) # integer division
print(5%2)
print(5**2)

# Relational operators
print(5>2)
print(5<2)
print(5>=2)
print(5<=2)
print(5==2)
print(5!=2)

# Logical operators
print(True and False)
print(True or False)
print(not True)

print(1 and 0)
print(1 or 0)
print(not 1)

# Bitwise operators - operates on binary values
# bitwise and
print(2 & 3)          # 10 & 11 = 10 -> 2

# bitwise or
print(2 | 3)          # 10 | 11 = 11 -> 3

# bitwise xor
print(2 ^ 3)          # 10 ^ 11 = 01 -> 1

#bitwise not
print(~2)
print(~3)

# bitwise right shift
print(5 >> 2)         # 101 >> 2 = 001 -> 1

# bitwise left shift
print(5 << 2)         # 101 << 2 = 10100 -> 20

"""[Refer for more on Bitwise operators](https://www.geeksforgeeks.org/python-bitwise-operators/)"""

# Assignment operators
a = 5
a += 2  # a = a + 2
print(a)
a -= 2
print(a)
a *= 2
print(a)
a /= 2
print(a)

# a++ ++a  -> not supported in python
x = 'hello'
x += 'world'
print(x)

# Membership operators - case sensitive
print('h' in 'hello')
print('h' not in 'hello')

print(4 in [1,2,3,4])

# Program - Find the sum of a 3 digit number entered by the user
num = int(input('Enter 3-digit number: '))
fdigit = num % 10
sdigit = (num // 10)%10
tdigit = num // 100
print(fdigit+sdigit+tdigit)

# Program - Find the sum of a 3 digit number entered by the user
num = input('Enter 3-digit number: ')
print(int(num[0])+int(num[1])+int(num[2]))

# Program - Find the sum of a n-digit number entered by the user
num = input('Enter a number: ')
sum = 0
for i in num:
  sum += int(i)
print(sum)

"""# 2. If-else in python

syntax:
```
if condition:
  # if - code
elif condition:
  # elif - code
else:
  # else - code
```
"""

# login program and indentation
# email -> nitish.campusx@gmail.com
# password -> 1234

email = input('Enter email: ')
password = input('Enter password: ')

if email == 'nitish.campusx@gmail.com' and password == '1234':
  print('Welcome')
else:
  print('Incorrect details')

# if-elif-else and nested if-else
email = input('Enter email: ')
password = input('Enter password: ')

if email == 'nitish.campusx@gmail.com' and password == '1234':
  print('Welcome')
elif email == 'nitish.campusx@gmail.com':
    password = input('Incorrect password, Enter again: ')
    if password == '1234':
      print('Welcome')
    else:
      print('Incorrect password')
else:
  print('Incorrect details')

# if-else examples
# 1. Find the min of 3 given numbers
# 2. Menu Driven Program

# Program: Find the minimum of 3 given numbers
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
num3 = int(input('Enter third number: '))
if num1<num2 and num1<num3:
  print(num1, 'is minimum')
elif num2<num3:
  print(num2, 'is minimum')
else:
  print(num3, 'is minimum')

# Program: Menu Driven Calculator
fnum = int(input('Enter first number: '))
snum = int(input('Enter second number: '))
op = input('Enter operator: ')

if op == '+':
  print(fnum+snum)
elif op == '-':
  print(fnum-snum)
elif op == '*':
  print(fnum*snum)
else:
  print(fnum/snum)

# Program: atm code
menu = input("""
Hi! how can I help you.
1. Enter 1 for pin change
2. Enter 2 for balance check
3. Enter 3 for withdraw
4. Enter 4 for exit
""")

if menu == '1':
  print('pin change')
elif menu == '2':
  print('balance')
elif menu == '3':
  print('withdraw')
else:
  print('exit')

"""# 3. Modules

Module is a file which contains functions, classes and variables. Grouping related code into a module makes the code easier to understand and use. Code reuseability.

Few examples of module:
1.   math
2.   keyword
3.   random
4.   datetime
"""

# math
import math

print(math.factorial(5))
print(math.floor(3.7))

# keyword
import keyword

print(keyword.kwlist)

keyword.softkwlist

# random
import random

print(random.randint(1,10))

# datetime
import datetime

print(datetime.datetime.now())

help('math')

# to get list of all modules
help('modules')

"""# 4. Loops in python

- Need for loops - to execute a block of code repeatedly. Avoid code redundancy.
- While Loop

```
while loop syntax:
while <condtion>:
    loop - statement

while else loop syntax:
while <condition>:
    loop - statement
else:
    else - statement
```
- For Loop

```
for loop syntax:
for i in range:
    loop - statement
```

[Python tutor](https://pythontutor.com/)
"""

# While loop example -> program to print the table
# Program -> Sum of all digits of a given number
# Program -> keep accepting numbers from users till he/she enters a 0 and then find the avg

# while loop
# Program - print table of a number
num = int(input('Enter a number: '))
i = 1
while i<=10:
  print(num,'*',i,'=',num*i)
  i += 1

# while loop with else
x = 1
while x<3:
  print(x)
  x += 1
else:
  print('limit crossed')

# Program - Guessing Game
import random
jp_num = random.randint(1,100)
guess = int(input('Guess a number between 1 and 100: '))
count = 1
while guess != jp_num:
  if guess > jp_num:
    print('Incorrect, guess lower')
  else:
    print('Incorrect, guess higher')
  count += 1
  guess = int(input('Guess a number between 1 and 100: '))
else:
  print('You guessed it in',count,'attempts')

# for loop

"""range()
```
range(stop) -> range object
range(start, stop[, step]) -> range object
```
 Return an object that produces a sequence of integers from start (inclusive) to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1. start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3. These are exactly the valid indices for a list of 4 elements. When step is given, it specifies the increment (or decrement).

range(1, 10, 3) produces 1, 4, 7.
"""

help('range')

for i in range(1,10,2):
  print(i)

for i in 'Delhi':
  print(i)

for i in range(10,0,-1):
  print(i)

for i in [1,2,3,4,5]:
  print(i)

# for loop programs

# Program - print table of a number
num = int(input('Enter a number: '))
for i in range(1,11):
  print(num,'*',i,'=',num*i)

"""### Program - The current population of a town is 10000. The population of the town is increasing at the rate of 10% per year. You have to write a program to find out the population at the end of each of the last 10 years."""

population = 10000
for i in range(1,11):
  population = population//1.1
  print('Population of last',i,'year(s) is', population)

curr_pop = 10000

for i in range(10,0,-1):
  print(i,curr_pop)
  curr_pop //= 1.1

"""#### Explanation :



To calculate the population for each year with a 10% increase, you can use a simpler equation based on the previous year's population. Let's assume the population of the previous year is represented by variable x.

The equation can be written as:

> Current Year Population = x * 1.1

In this equation, the current year's population is equal to the previous year's population multiplied by 1.1, representing a 10% increase.

To find the population of the previous year (x), we can rearrange the equation as follows:

> x = Current Year Population / 1.1

Using this simplified equation, if you have the current year's population (e.g., 10,000), you can divide it by 1.1 to calculate the population of the previous year.

This equation allows you to calculate the population for each year, assuming you know the population of the current year and want to find the population of the previous year.
"""