##
def add_two_numbers(a,b):
    num=a + b
    return num
print (add_two_numbers(5,3))

##
def area_circle(r):
    area=3.14*r**2
    return area

print (area_circle(5))

##
def sum_total(*args):
    total=0
    for i in args:
        total=total + i
    return total
print (sum_total(1,2,3,4,5))

##
def temp(C):
    F=(C*9/5)+32
    return F
print (temp(30))

##
def check_season(mes):
    if mes in ['December', 'January', 'February']:
        return 'Winter'
    elif mes in ['March', 'April', 'May']:
        return 'Spring'
    elif mes in ['June', 'July', 'August']:
        return 'Summer'
    elif mes in ['September', 'October', 'November']:
        return 'Autumn'
print (check_season('January'))

