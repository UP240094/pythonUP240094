## Level 1 Exercises
print("Level 1 Exercises:")

# Exercise 1: Explain the difference between map, filter, and reduce.
print("Exercise 1:")
print("The difference between map, filter, and reduce is:")
# map: applies a function to each element of a list and returns a new list with the transformed values.
# It is used to modify elements.
# Example:
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print("Original list:", numbers)
print("List of squares:", squares)

# filter: filters the elements of a list based on a condition, returning only those that meet the criteria.
# It is used to select specific elements.
# Example:
numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Original list:", numbers)
print("List of even numbers:", evens)

# reduce: applies a cumulative operation on the elements of a list, reducing it to a single value.
# It is used to calculate aggregated results.
# Example:
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print("Original list:", numbers)
print("Product of the list:", product)

# Exercise 2: Explain the difference between higher-order function, closure, and decorator.
print("Exercise 2:")
print("The difference between higher-order function, closure, and decorator is:")
# Higher-order function: functions that take other functions as arguments or return a function as a result.
# They are used to write more flexible and reusable code.
# Example:
def apply_function(func, value):
    return func(value)
double = lambda x: x * 2
result = apply_function(double, 5)
print("Result of applying the double function:", result)

# Closure: a function that remembers the environment in which it was created, even when executed outside that environment.
# It is used to maintain states without using global variables.
# Example:
def create_multiplier(factor):
    def multiplier(number):
        return number * factor
    return multiplier
multiply_by_3 = create_multiplier(3)
print("Result of the closure:", multiply_by_3(5))

# Decorator: a function that modifies the behavior of another function without changing its code.
# It is widely used to extend functionalities in Python.
# Example:
def decorator(func):
    def new_function():
        print("Before executing the function")
        func()
        print("After executing the function")
    return new_function

@decorator
def greet():
    print("Hello!")

# Exercise 3: Define a call function before map, filter, or reduce, see examples.
print("Exercise 3:")
print("Example of using a call function before map, filter, or reduce:")

# map:
# Example:
names = ['Sandra', 'Aaron', 'Sofia', 'Janize', 'Vanessa']

def change_to_upper(name):
    return name.upper()
names_upper_cased = map(change_to_upper, names)
print("The example used with map is:", list(names_upper_cased))

# filter:
# Example:
def starts_with_s(name):
    return name.lower().startswith('s')
names_starting_with_s = filter(starts_with_s, names)
print("The example used with filter is:", list(names_starting_with_s))

# reduce:
# Example:
numbers_str = ['10', '20', '30', '40', '50']
def add_two_nums(x, y):
    return int(x) + int(y)
total = reduce(add_two_nums, numbers_str)
print("The example used with reduce is:", total)

# Exercise 4: Use for loop to print each country in the countries list.
print("Exercise 4:")
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
for country in countries:
    print("The countries in this list are:", country)

# Exercise 5: Use for to print each name in the names list.
print("Exercise 5:")
names = ['Sandra', 'Aaron', 'Sofia', 'Janize', 'Vanessa']
for name in names:
    print("The names in this list are:", name)

# Exercise 6: Use for to print each number in the numbers list.
print("Exercise 6:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print("The numbers in this list are:", number)

## Level 2 Exercises
print("Level 2 Exercises:")

# Exercise 1: Use map to create a new list by changing each country to uppercase in the countries list.
print("Exercise 1:")
countries_upper = map(lambda country: country.upper(), countries)
print("The countries in uppercase are:", list(countries_upper))

# Exercise 2: Use map to create a new list by changing each number to its square in the numbers list.
print("Exercise 2:")
numbers_squared = map(lambda number: number ** 2, numbers)
print("The numbers squared are:", list(numbers_squared))

# Exercise 3: Use map to change each name to uppercase in the names list.
print("Exercise 3:")
names_upper = map(lambda name: name.upper(), names)
print("The names in uppercase are:", list(names_upper))

# Exercise 4: Use filter to filter out countries containing 'land'.
print("Exercise 4:")
countries_with_land = filter(lambda country: 'land' in country, countries)
print("The countries containing 'land' are:", list(countries_with_land))

# Exercise 5: Use filter to filter out countries having exactly six characters.
print("Exercise 5:")
countries_with_six_characters = filter(lambda country: len(country) == 6, countries)
print("The countries with six characters are:", list(countries_with_six_characters))

# Exercise 6: Use filter to filter out countries containing six letters and more in the country list.
print("Exercise 6:")
countries_with_six_letters_or_more = filter(lambda country: len(country) >= 6, countries)
print("The countries with six letters or more are:", list(countries_with_six_letters_or_more))

# Exercise 7: Use filter to filter out countries starting with 'E'.
print("Exercise 7:")
countries_starting_with_e = filter(lambda country: country.startswith('E'), countries)
print("The countries starting with 'E' are:", list(countries_starting_with_e))

# Exercise 8: Chain two or more list iterators (e.g., arr.map(callback).filter(callback).reduce(callback)).
print("Exercise 8:")
result = reduce(
    lambda x, y: x + y,
    filter(
        lambda x: x % 2 == 0,
        map(
            lambda x: x ** 2,
            numbers
        )
    )
)
print("The result of chaining map, filter, and reduce is:", result)

# Exercise 9: Declare a function called get_string_lists which takes a list as a parameter
# and then returns a list containing only string items.
print("Exercise 9:")
def get_string_lists(lst):
    return list(filter(lambda x: isinstance(x, str), lst))
mixed_list = [1, 'hello', 3.14, 'world', True, 'Python']
string_list = get_string_lists(mixed_list)
print("The list of only strings is:", string_list)

# Exercise 10: Use reduce to sum all the numbers in the numbers list.
print("Exercise 10:")
total_sum = reduce(lambda x, y: x + y, numbers)
print("The sum of all the numbers is:", total_sum)

# Exercise 11: Use reduce to concatenate all the countries and produce this sentence:
# Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries.
print("Exercise 11:")
sentence = reduce(
    lambda x, y: f"{x}, {y}" if y != countries[-1] else f"{x}, and {y}",
    countries) + " are north European countries."
print(sentence)

# Exercise 12: Declare a function called categorize_countries that returns a list of countries with some common pattern.
print("Exercise 12:")
def categorize_countries(pattern):
    return list(filter(lambda country: pattern in country, countries))
pattern = 'land'
categorized_countries = categorize_countries(pattern)
print(f"The countries containing '{pattern}' are:", categorized_countries)

# Exercise 13: Create a function returning a dictionary, where keys stand for starting letters of countries,
# and values are the number of country names starting with that letter.
print("Exercise 13:")
def count_countries_by_letter(countries):
    country_count = {}
    for country in countries:
        first_letter = country[0].upper()
        country_count[first_letter] = country_count.get(first_letter, 0) + 1
    return country_count
country_count_by_letter = count_countries_by_letter(countries)
print("The count of countries by starting letter is:", country_count_by_letter)

# Exercise 14: Declare a get_first_ten_countries function.
# It returns a list of the first ten countries from the countries.js list in the data folder.
print("Exercise 14:")
import countries_data as c
countries = c.countries_data
def get_first_ten_countries(lst):
    return lst[:10]
print("The first 10 countries are:", get_first_ten_countries(countries))

# Exercise 15: Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
print("Exercise 15:")
def get_last_ten_countries(lst):
    return lst[-10:]
print("The last 10 countries are:", get_last_ten_countries(countries))

## Level 3 Exercises
print("Level 3 Exercises:")

# Exercise 1: Use the countries_data.py file and follow the tasks below:
print("Exercise 1:")
import countries_data as cd
countries = cd.countries_data

# Exercise 3.1: Sort countries by name, by capital, by population.
print("Exercise 3.1:")

# Sort by name:
sorted_by_name = sorted(countries, key=lambda x: x["name"])
print("Sorted by name:")
for country in sorted_by_name:
    print(country["name"])

# Sort by capital:
print("Sorted by capital:")
sorted_by_capital = sorted(countries, key=lambda x: x["capital"])
for country in sorted_by_capital:
    print(country["capital"])

# Sort by population:
print("Sorted by population:")
sorted_by_population = sorted(countries, key=lambda x: x["population"])
for country in sorted_by_population:
    print(country['name'], "Population:", country['population'])

# Exercise 3.2: Sort out the ten most spoken languages by location.
print("Exercise 3.2:")
sorted_languages = sorted(countries, key=lambda x: x["population"], reverse=True)
print("The 10 most spoken languages by location:")
top_10_spoken = sorted_languages[:10]
for language in top_10_spoken:
    print(language['languages'], ({language['name']}), "spoken by:", language['population'], "total population")

# Exercise 3.3: Sort out the ten most populated countries.
print("Exercise 3.3:")
sorted_countries = sorted(countries, key=lambda x: x["population"], reverse=True)
top_10_populated = sorted_countries[:10]
print("The 10 most populated countries are:")
for country in top_10_populated:
    print(country["name"], country["population"])