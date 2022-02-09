# charles madhuku @stiles

"""
Write a program that asks the user to enter five numbers(use five input statements). Then print out
those numbers all on the same line, with each number separated from the others by exactly three
spaces. Use the sep optional argument to the print statement to do this.

"""


try:
    num1 = int(input('Enter number: '))
    num2 = int(input('Enter number: '))
    num3 = int(input('Enter number: '))
    num4 = int(input('Enter number: '))
    num5 = int(input('Enter number: '))
    print(num1, num2, num3, num4, num5, sep='   ')
except:
    print('invalid numbers')
