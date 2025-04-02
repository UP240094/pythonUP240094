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