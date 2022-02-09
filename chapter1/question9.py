# charles madhuku @sttiles

"""
Write a program that asks the user to enter a number. Store that number in a variable. Add 2 to that
number, store the result in the same variable, and then print out the value of that variable.

"""

try:
    num = int(input('enter num: '))

    num = num + 2
    print(num)

except:
    print('invalid numbers')
