# charles madhuku @stiles

"""
The Body Mass Index, BMI, is calculated as
BMI = 703w /h*2 

where w is the person’s weight in pounds and h is the person’s height in inches. Write a program that
asks the user for their height their weight and prints out their BMI. [Note: one way to compute h2 is
as h * h.]

"""

try:
    weight = float(input('Please enter your weight: '))
    height = float(input('Please enter your height: '))

    bmi = (weight)/(height*height)
    print(f'BMI: {bmi}')
except:
    print('invalid inputs')
