# charles madhuku @stiles

"""
Write a program that asks the user to enter a distance in kilometers and then prints out how far that
distance is in miles. There are 0.621371 miles in one kilometer.

"""


try:
    distanceInkilometres = float(
        input(' Please  enter distance in kilometres: '))
    miles = distanceInkilometres * 0.621371
    print(f'{miles} miles')
except:
    print('enter valid values')
    exit()
