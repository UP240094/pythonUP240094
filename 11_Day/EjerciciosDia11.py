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

##
def calculate_slope(x1,y1,x2,y2):
    slope=(y2-y1)/(x2-x1)
    return slope
print (calculate_slope(1,2,3,4))

##
def solve_quadratic_eqn(a,b,c):
    x1=(-b+((b**2)-4*a*c)**0.5)/(2*a)
    x2=(-b-((b**2)-4*a*c)**0.5)/(2*a)
    return x1,x2
print (solve_quadratic_eqn(1,2,3))

##
def print_list(lst):
    for i in lst:
        print(i)
print_list([1,2,3,4,5])

##
def reverse_list(lst):
    return lst[::-1]
print (reverse_list([1,2,3,4,5]))

##
def capitalize_list(lista):
    return [i.upper() for i in lista]
print (capitalize_list(['Potato', 'Tomato', 'Mango', 'Milk']))

##
def add_item(food_staff,comida):
    food_staff=['Potato', 'Tomato', 'Mango', 'Milk']
    food_staff.append(comida)
    return food_staff

print(add_item(['Potato', 'Tomato', 'Mango', 'Milk'], 'Pasta'))

##
def sum_num(num1):
    for i in range(num1+1):
        for j in range(num1):
            i=i+j
    return i
print(sum_num(100))

##
def sum_of_odds(num1):
    for i in range(num1+1):
        for j in range(num1):
            if i%2==0 and j%2==0:
                i=i+j
    return i
print(sum_of_odds(100))

##
def sum_of_even(num):
    total = 0
    for i in range(num + 1):
        if i % 2 == 0:
            total += i
    return total

print(sum_of_even(100))

##Level 2
##
def even_and_odds(nums):
    even = 0
    odd = 0
    for i in range(nums+1):
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return 'The number of evens are: ', even, 'The number of odds are: ', odd
print(even_and_odds(100))

##
def factorial(fac):
    numb=1
    for i in range(1,fac+1):
        numb=i*numb
    return numb
print (factorial(5))

##
def is_empty(lst):
    if len(lst) == 0:
        return True
print (is_empty([]))

##
def calc_mean(nums):
    total_media=0
    for i in nums:
        total_media=total_media+i
        prom=total_media/len(nums)
    return prom
print (calc_mean([3,2,4,1,5,5,5,7]))

def calc_mediana(nums):
    mediana=nums[int(len(nums)/2)]
    return mediana
print (calc_mediana([3,2,4,1,5,5,5,7]))

def calc_moda(nums):
    from collections import Counter
    calc_mode=Counter(nums)
    return calc_mode.most_common(1)
print(calc_moda([3,2,4,1,5,5,5,7]))

def calc_rango(nums):
    nums.sort()
    range1=nums[0]
    range2=nums[int(len(nums)-1)]
    j=range(range1, range2)
    return j
print(calc_rango([3,2,4,1,5,5,5,7]))

def calc_varianza(nums):
    var = sum(nums) / len(nums)
    var_res = sum((i - var) ** 2 for i in nums) / len(nums)
    return var_res
print(calc_varianza([3,2,4,1,5,5,5,7]))

def calc_std(nums):
    var = sum(nums) / len(nums)
    var_res = sum((i - var) ** 2 for i in nums) / len(nums)
    std=var_res**0.5
    return std
print(calc_std([3,2,4,1,5,5,5,7]))

##Level 3
##
def is_prime(num):
    for i in range(2, int(num**0.5)+1):
        if (num%i)==0:
            print(num,' no es primo')
        else:
            print(num,' es primo')
    return ''
print(is_prime(5))

##
def unique(lst):
    return len(set(lst))==len(lst)
print(unique([3,2,4,1,5,5,5,7]))

##
def same(lista):
    list = iter(lista)
    tipo = type(next(list))
    if all((type(x) is tipo) for x in list): 
        print(True)
    else:
        print(False)
    return ''
print(same([1,2,3,4,'true']))

print("Revisado")