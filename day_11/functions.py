def main ():
    num1 = float (input ('num1: '))
    num2 = float (input ('num2: '))
    radius = float (input ('radius: '))
    temp = float (input ('temprature: '))
    mon = input ('what is your month? ')


    print ('The sum of the numbers is ', add_numbers (num1, num2))
    print ('The area of the circle is ', area_circle (radius))
    print ('The temprature converted to degrees farenheit is ', convert_C_to_F (temp))
    print ('The season in your month is ', what_season (mon))

def add_numbers (*num):
    total = 0
    for nums in num:
        total += nums
    return total

def area_circle (r):
    PI = 3.14
    area = PI * r **2
    return area

def convert_C_to_F (c):
    f = (c * 9/5) + 32
    return f 

def what_season (month):
    month = month.lower()
    if month in ('march', 'april', 'may', 'june'):
        season = 'Summer'
    elif month in ('july', 'august', 'september', 'october'):
        season = 'Monsoon'
    elif month in ('november', 'december', 'january', 'february'):
        season = 'Winter'
    else:
        season = 'not a valid month'
    return season

main ()