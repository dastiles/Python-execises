# charles madhuku @stiles
"""
Write a program that asks the user to enter two numbers(you’ll probably want to use separate input
statements for that). Then print out the result of adding those two numbers.

"""

try:
    num1 = float(input('first number to add: '))
    num2 = float(input('first number to add: '))
    print(f'Total: {num1 + num2}')
except:
    print('invalid numbers')
