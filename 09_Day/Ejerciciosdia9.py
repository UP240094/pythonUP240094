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
    