"""
Write a program that asks the user to enter a height and then draws a box like the one below that is 10 asterisks wide and as tall as specified by the user.

"""
try:
    numberOfTimes = int(input('Enter a number: '))

    for i in range(numberOfTimes):
        print('**********')

except:
    print('Enter valid input')


# charles madhuku @stiles
