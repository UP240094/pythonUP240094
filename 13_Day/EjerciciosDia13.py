# Level 1 Exercises
print("Level 1 Exercises:")

# Exercise 1: Filter only negative and zero in the list using list comprehension
print("Exercise 1:")
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [num for num in numbers if num <= 0]
print("The list with only negatives and zero is:", negative_and_zero)

# Exercise 2: Flatten the following list of lists of lists to a one-dimensional list.
print("Exercise 2:")
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [num for sublist1 in list_of_lists for sublist2 in sublist1 for num in sublist2]
print("The one-dimensional list is:", flattened_list)

# Exercise 3: Using list comprehension, create the following list of tuples.
print("Exercise 3:")
tuples_list = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print("The list of tuples is:", tuples_list)

# Exercise 4: Flatten the following list to a new list:
print("Exercise 4:")
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries = [[country.upper(), country[:3].upper(), capital.upper()] for sublist in countries for (country, capital) in sublist]
print("The new list is:", flattened_countries)

# Exercise 5: Change the following list to a list of dictionaries.
print("Exercise 5:")