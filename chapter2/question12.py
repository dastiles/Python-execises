"""
Write a program that uses a loop and an input statement to ask the user to enter 10 numbers. After
each number is entered, print out the square of that number.

    """


for i in range(10):
    try:
        num = int(input('Enter number: '))
        print(num*num)
    except:
        print("Invalid input")


# charles madhuku @stiles
