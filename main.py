"""
NAME: main.py
AUTHOR: Roger Aragon
DATE MODIFIED: 2/26/2019
DESCRIPTION: Inputs two numbers, outputs various calculations using them
EMAIL: aragonr87056@student.vvc.edu
"""

import math

num1 = int(input('Enter first number: \n'))
num2 = int(input('Enter second  number: \n'))

print('The sum is: ',num1 + num2)
print('The diffrence is: ',num1 - num2)
print('The product is: ',num1 * num2)
print('The average is: ',(num1 + num2) /2)
print('The distance is: ',math.fabs(num1 - num2))
print('The maximum is: ',max(num1,num2))
print('The minimum is: ',min(num1,num2))



