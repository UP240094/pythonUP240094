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
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries_dict = [{'country': country.upper(), 'city': capital.upper()} for sublist in countries for (country, capital) in sublist]
print("The list of dictionaries is:", countries_dict)

# Exercise 6: Change the following list of lists to a list of concatenated strings.
print("Exercise 6:")
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
names_concatenated = [' '.join([name[0].upper(), name[1].upper()]) for sublist in names for name in sublist]
print("The list of concatenated strings is:", names_concatenated)

# Exercise 7: Write a lambda function which can solve a slope or y-intercept of linear functions.
print("Exercise 7:")
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else None
y_intercept = lambda x, y, m: y - m * x if m is not None else None
print(f"The slope is: {slope(2, 3, 4, 7)}")
print(f"The y-intercept is: {y_intercept(2, 3, slope(2, 3, 4, 7))}")
print(f"The y-intercept is: {y_intercept(4, 7, slope(2, 3, 4, 7))}")
print(f"The y-intercept is: {y_intercept(0, 0, slope(2, 3, 4, 7))}")
print(f"The y-intercept is: {y_intercept(2, 3, slope(2, 3, 4, 7))}")