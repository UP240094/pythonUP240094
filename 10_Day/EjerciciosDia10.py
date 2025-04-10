##1. Iterate 0 to 10 using for loop, do the same using while loop.

print('Exercise 1 Level 1: Iterate from 0 to 10 using a for loop, do the same using a while loop.')

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number)

number = 0
while number <= 10:
    print(number)
    number += 1

##2. Iterate 10 to 0 using for loop, do the same using while loop.

print('Exercise 2 Level 1: Iterate from 10 to 0 using a for loop, do the same using a while loop.')

for number in range(10, -1, -1):
    print(number)

number = 10
while number >= 0:
    print(number)
    number -= 1

##3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
#   ```py
#     #
#     ##
#     ###
#     ####
#     #####
#     ######
#     #######
#   ```

print('''Exercise 3 Level 1: 
    Write a loop that makes seven calls to print(), so we get the following triangle in the output:
''')

triangle = '#'

for i in range(1, 8):
    print(triangle * i)

##4. Use nested loops to create the following:

#   ```sh
#   # # # # # # # #
#   # # # # # # # #
#   # # # # # # # #
#   # # # # # # # #
#   # # # # # # # #
#   # # # # # # # #
#   # # # # # # # #
#   # # # # # # # #
#   ```

print('''Exercise 4 Level 1:
    Use nested loops to create the following:
''')

row = '# '
for i in range(8):
    print(row * 8)

    ##5. Print the following pattern:
#   ```sh
#   0 x 0 = 0
#   1 x 1 = 1
#   2 x 2 = 4
#   3 x 3 = 9
#   4 x 4 = 16
#   5 x 5 = 25
#   6 x 6 = 36
#   7 x 7 = 49
#   8 x 8 = 64
#   9 x 9 = 81
#   10 x 10 = 100
#   ```

print('''Exercise 5 Level 1:
    Print the following pattern:
''')

num = 0
while num < 11:
    print('{} x {} = {}'.format(num, num, num * num))
    num += 1

##6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

print('''Exercise 6 Level 1:
      Iterate through the list, ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
      using a for loop and print out the items.
''')

languages = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']

for language in languages:
    print(language)

   ##7. Use for loop to iterate from 0 to 100 and print only even numbers

print('''Exercise 7 Level 1:
      Use a for loop to iterate from 0 to 100 and print only even numbers.
''')

for num in range(0, 101, 2):
    print(num) 

    ##8. Use for loop to iterate from 0 to 100 and print only odd numbers

print('''Exercise 8 Level 1:
      Use a for loop to iterate from 0 to 100 and print only odd numbers.
''')

num = 1
while num < 101:
    print(num)
    num += 2

### Exercises: Level 2

##1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.

##   ```sh
#   The sum of all numbers is 5050.
#   ```

print('''Exercise 1 Level 2: 
      Use a for loop to iterate from 0 to 100 and print the sum of all numbers.
''')

total_sum = 0
for i in range(101):
    total_sum += i
print('The sum of all numbers is:', total_sum)

##2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

##   ```sh
#   The sum of all evens is 2550. And the sum of all odds is 2500.
#   ```

print('''Exercise 2 Level 2:
      Use a for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
''')

even_numbers = []
odd_numbers = []

for i in range(101):
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)

print('Even numbers:', even_numbers)
print('The sum of all even numbers from 0 to 100 is:', sum(even_numbers))
print('Odd numbers:', odd_numbers)
print('The sum of all odd numbers from 0 to 100 is:', sum(odd_numbers))

#3. Go to the data folder and use the [countries_data.py]
# (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file. 
# 3.1. What are the total number of languages in the data
# 3.2. Find the ten most spoken languages from the data
# 3.3. Find the 10 most populated countries in the world

##Level 3

##
from countries_1 import countries_1

paisesland=[countries for countries in countries_1 if 'land' in countries]
print(paisesland)

##
fruits = ['banana', 'orange', 'mango', 'lemon']
conteo=-1
for i in fruits:
    print(fruits[conteo])
    conteo=conteo -1


##
from countries_data import countries_data_1

all_languages = set()
for country in countries_data_1:
    all_languages.update(country['languages'])
total_languages = len(all_languages)
print("Total number of languages:", total_languages)


##
language_count = {}
for country in countries_data_1:
    for language in country['languages']:
        language_count[language] = language_count.get(language, 0) + 1

most_spoken_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)[:10]
print("Ten most spoken languages:")
for language, count in most_spoken_languages:
    print(f"{language}: {count}")

most_populated_countries = sorted(countries_data_1, key=lambda x: x['population'], reverse=True)[:10]
print("Ten most populated countries:")
for country in most_populated_countries:
    print(f"{country['name']}: {country['population']}")

print("Revisado") #Explicame como funciona la funcion lambda, (no se trabaja en este modulo)