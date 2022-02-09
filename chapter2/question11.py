"""Write a program that asks the user to enter a number and then prints out the letter A that many times,
all on the same line.
    """

try:
    num = int(input('Enter number: '))
    for i in range(num):
        print('A', end='')

except:
    print('Invalid input')


# charles madhuku @stiles