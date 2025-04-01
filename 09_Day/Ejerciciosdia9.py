##1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: 
# You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.
# Output:
#    ```sh
#    Enter your age: 30
#    You are old enough to learn to drive.
#    Output:
#    Enter your age: 15
#    You need 3 more years to learn to drive.
#    ```

my_age = int(input("Enter your age: "))
if my_age >= 18:
    print("You are old enough to learn to drive.")

else:
    print("You need  3 more years to learn to drive.")

 ##2. Compare the values of my_age and your_age using if … else. 
 # Who is older (me or you)? Use input(“Enter your age: ”)
# to get the age as input.
#  You can use a nested condition to print 'year' 
# for 1 year difference 
# in age, 'years' for bigger differences, 
# and a custom text if my_age = your_age. Output:
#    ```sh
#    Enter your age: 30
#    You are 5 years older than me.
#    ```
print("My age is", my_age)
your_age = int(input("Enter your age: "))
if my_age > your_age:
    print("You are", my_age - your_age, "years older than me.")
elif my_age < your_age:
    print("You are", your_age - my_age, "years older than me.")
else:
    print("We are the same age.")

 #3. Get two numbers from the user using input prompt.
#  If a is greater than b return a is greater than b,
#  if a is less b return a is smaller than b,
#  else a is equal to b. Output:
#```sh
#Enter number one: 4
#Enter number two: 3
#4 is greater than 3
#```
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))
if a > b:
    print(a, "is greater than", b)
elif a < b:
    print(a, "is smaller than", b)
else:
    print(a, "is equal to", b)

 ### Exercises: Level 2

##1. Write a code which gives grade to students according to theirs scores:

#        ```sh
#        80-100, A
#        70-89, B
#        60-69, C
#        50-59, D
#        0-49, F
#        ```
Grade_Alumno = int(input("Enter your grade: "))
if Grade_Alumno >= 80 and Grade_Alumno <= 100:
    print("you got an A")
elif Grade_Alumno >= 70 and Grade_Alumno <= 89:
    print("you got a B")
elif Grade_Alumno >= 60 and Grade_Alumno <= 69:
    print("you got a C")
elif Grade_Alumno >= 50 and Grade_Alumno <= 59:
    print("you got a D")
elif Grade_Alumno >= 0 and Grade_Alumno <= 49:
    print("you got a F")
else:
    print("Invalid grade")   

    #   1. Check if the season is Autumn, Winter, Spring or Summer.
    #  If the user input is:
#    September, October or November, the season is Autumn.
#    December, January or February, the season is Winter.
#    March, April or May, the season is Spring
#    June, July or August, the season is Summer

Autumn = {'September', 'Septiembre', 'October', 'Octubre', 'November', 'Noviembre'}
Winter = {'Dicember', 'Diciembre', 'January', 'Enero', 'February', 'Febrero'}
Spring = {'March', 'Marzo', 'April', 'Abril', 'May', 'Mayo'}
Summer = {'June', 'Junio', 'July', 'Julio', 'Agust', 'Agosto'}

month = input("Enter the month: ")
if month in Autumn:
    print("The season is Autumn")
elif month in Winter:
    print("The season is Winter")
elif month in Spring:
    print("The season is Spring")
elif month in Summer:
    print("The season is Summer")
else:
    print("Invalid month")

#2. The following list contains some fruits:
 #    ```sh
#    fruits = ['banana', 'orange', 'mango', 'lemon']
#    ```
#   If a fruit doesn't exist in the list 
# add the fruit to the list and print the modified list. 
# If the fruit exists
#  print('That fruit already exist in the list')

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter a fruit: ")
if fruit in fruits:
    print('That fruit already exists in the list')
else:
    fruits.append(fruit)
    print('The fruit has been added to the list', fruits)

### Exercises: Level 3

#   1. Here we have a person  dictionary. Feel free to modify it!

#```py
#        person={
#    'first_name': 'Asabeneh',
#    'last_name': 'Yetayeh',
#    'age': 250,
#    'country': 'Finland',
#    'is_marred': True,
#    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#    'address': {
#        'street': 'Space street',
#        'zipcode': '02210'
#    }
#    }
#```

#   * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
#   * Check if the person dictionary has skills key, if so check if the person has 
#     'Python' skill and print out the result.
#   * If a person skills has only JavaScript and React, print('He is a front end developer'), 
#     if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
#     if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
#     else print('unknown title') - for more accurate results more conditions can be nested!
#   * If the person is married and if he lives in Finland, print the information in the following format:

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

print(person)

print('problem 1: Guet the keys in the middle')

midskillskeys = len(person.get('skills'))//2

print('The skills in the middle are ', person['skills'][midskillskeys])

# Problem 2: Check if the person has Python as a skill
print('Problem 2: Check if the person has Python as a skill')

if 'Python' in person['skills']:
    print('Yes, the person has Python as a skill:', person['skills'])
else:
    print('The person does not have Python as a skill.')

# Problem 3: Determine the developer type based on skills
print('Problem 3: Determine the developer type based on skills')

front_end_dev = 'JavaScript' in person['skills'] and 'React' in person['skills']
back_end_dev = 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']
full_stack_dev = 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']

if front_end_dev == True and len(person['skills']) == 2 :
    print("El programador es un (Front end developer)")
elif back_end_dev == True and len(person['skills']) == 3:
    print('El programador es un (Backend developer)')
elif full_stack_dev == True:
    print('El programador es un (Fullstack developer)')
else:
    print('unknown title')

# Problem 4: Check if the person is married and lives in Finland
print('Problem 4: Check if the person is married and lives in Finland')

if person['is_married'] == True and 'Finland' in person['country']:
    print('''
     Asabeneh Yetayeh lives in finland, he is married
    ''')
else:
    print('Una de las condiciones no coinciden')