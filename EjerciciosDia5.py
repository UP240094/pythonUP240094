
##1. Declare an empty list

emptylist = list()
print(emptylist)

##2. Declare a list with more than 5 items

schoolsupplieslist = ['pen', 'pencil', 'backpack', 'book', 'pencil colors', 'pencil sharpener']
print(schoolsupplieslist)

##3. Find the length of your list

print('Numero de utiles escolares: ', len(schoolsupplieslist))

##4. Get the first item, the middle item and the last item of the list

firstitem = schoolsupplieslist[0]
midleitem = schoolsupplieslist[3]
lastitem = schoolsupplieslist[-1]
print('''
Primer item de la lista {}
Item de enmedio de la lista {}
Ultimo item de la lista {} 
'''.format(firstitem, midleitem, lastitem))

##5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_types = ['Leonardo', '19', '1.89', 'Single', 'Aguascalientes city']
print(mixed_data_types)

##6. Declare a list variable named it_companies and assign initial values Facebook, Google, 
# Microsoft, Apple, IBM, Oracle and Amazon.

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

##7. Print the list using _print()_

print(it_companies)

##8. Print the number of companies in the list

print('La cantidad de compañias en la lista de de: ', len(it_companies))

##9. Print the first, middle and last company

print('Ejercicio 9 nivel 1')

firstcompany = it_companies[0]
getmid = len(it_companies)//2
midcomp = it_companies[getmid]
lastcompany = it_companies[-1]
print('''
Primer compañia de la lista {}
La compañia de enmedio de la lista {}
Ultima compañia de la lista {} 
'''.format(firstcompany, midcomp, lastcompany))

##10. Print the list after modifying one of the companies

del it_companies[2]
print(it_companies)

##11. Add an IT company to it_companies

it_companies.append('Nvidia')
print(it_companies)

##12. Insert an IT company in the middle of the companies list

it_companies.insert(getmid ,'Intel')
print(it_companies)

##13. Change one of the it_companies names to uppercase (IBM excluded!)

del it_companies[0]
it_companies.insert(0, 'FACEBOOK')
print(it_companies)

##14. Join the it_companies with a string '#;&nbsp; '

it_companies.append ('#;&nbsp; ')
print(it_companies)

##15. Check if a certain company exists in the it_companies list.

does_nvidia = 'Nvidia' in it_companies
print('Esta la empresa Nvidia en la lista de It companies verdadero o falso: ', does_nvidia)

##16. Sort the list using sort() method

it_companies.sort()
print(it_companies)

##17. Reverse the list in descending order using reverse() method

it_companies.sort(reverse=True)
print(it_companies)

##18. Slice out the first 3 companies from the list

minusthreefcomp = it_companies[3:-1]
print(minusthreefcomp)

##19. Slice out the last 3 companies from the list

minusthreelcomp = it_companies[0:-4]
print(minusthreelcomp)

##20. Slice out the middle IT company or companies from the list

sliceoutmidcomp = it_companies[4]
it_companies.remove(sliceoutmidcomp)
print(it_companies)

##21. Remove the first IT company from the list

firstcomp = it_companies[0]
it_companies.remove(firstcomp)
print(it_companies)

##22. Remove the middle IT company or companies from the list

print('22. Remove the middle IT company or companies from the list')

midcomp = it_companies[3]
it_companies.remove(midcomp)
print(it_companies)

##23. Remove the last IT company from the list

lastcomp = it_companies[-1]
it_companies.remove(lastcomp)
print(it_companies)

##24. Remove all IT companies from the list

it_companies.clear()
print(it_companies)

##25. Destroy the IT companies list

it_companies.clear()
print(it_companies)

##26. Join the following lists:
#
#    ```py
#    front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
#    back_end = ['Node','Express', 'MongoDB']
#    ```

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
back_and_front_end = front_end + back_end
print(back_and_front_end)

##27. After joining the lists in question 26. Copy the joined list and assign it to a variable
#  full_stack, then insert Python and SQL after Redux.

full_stack = ['Python', 'SQL', 'Redux']
stack_end = back_and_front_end + full_stack
print(stack_end)

### Exercises: Level 2

#1. The following is a list of 10 students ages:
#```sh
#ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#```

#- Sort the list and find the min and max age
#- Add the min age and the max age again to the list
#- Find the median age (one middle item or two middle items divided by two)
#- Find the average age (sum of all items divided by their number )
#- Find the range of the ages (max minus min)
#- Compare the value of (min - average) and (max - average), use _abs()_ method

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort
print(ages)
lower_age = min(ages)
max_age = max(ages)

median_age = ages[4:5]
average_age = sum(ages) / len(ages)
range_ages = lower_age, max_age

dif_min_avg = abs(lower_age - average_age)
dif_max_avg = abs(max_age - average_age)

print('''
{}
Edad minima de la lista {} Edad maxima de la lista {}
      
Mediana de la lista     {}
Promedio de la edad     {}
Rango de edad           {}
      
Promedio absoluto de edad restando el minimo {}
Promedio absoluto de edad restando el maximo {}

Comparacion de valores absolutos como minimo y maximo:
El valor absoluto minimo es mayor que el maximo: {}
El valor absoluto maximo es mayor que el maximo: {}
'''.format(ages, lower_age, max_age, median_age, average_age, range_ages, dif_min_avg, dif_max_avg, dif_min_avg > dif_max_avg, dif_max_avg > dif_min_avg))