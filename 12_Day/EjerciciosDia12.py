## Level 1 Exercises
print("Level 1 Exercises:")

# Exercise 1: Write a function which generates a six-digit/character random_user_id.
print("Exercise 1:")
import random
import string

def generate_random_user_id():
    characters = string.ascii_letters + string.digits
    user_id = ''.join(random.choice(characters) for _ in range(6))
    return user_id

print("The random user ID is:", generate_random_user_id())

# Exercise 2: Modify the previous task. Declare a function named user_id_gen_by_user.
# It doesn’t take any parameters but takes two inputs using input().
# One input is the number of characters, and the second input is the number of IDs to generate.
print("Exercise 2:")

def user_id_gen_by_user():
    num_chars = int(input("Enter the number of characters for the user ID: "))
    num_ids = int(input("Enter the number of user IDs to generate: "))
    characters = string.ascii_letters + string.digits
    user_ids = []
    for _ in range(num_ids):
        user_id = ''.join(random.choice(characters) for _ in range(num_chars))
        user_ids.append(user_id)
    return user_ids

print("The random user IDs are:", user_id_gen_by_user())

# Exercise 3: Write a function named rgb_color_gen. It will generate RGB colors (3 values ranging from 0 to 255 each).
print("Exercise 3:")

def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

print("The RGB color is:", rgb_color_gen())

## Level 2 Exercises
print("Level 2 Exercises:")

# Exercise 1: Write a function list_of_hexa_colors which returns any number of hexadecimal colors in a list.
# (Six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f).
print("Exercise 1:")

def list_of_hexa_colors(num_colors):
    hex_colors = []
    for _ in range(num_colors):
        color = '#{:06X}'.format(random.randint(0, 0xFFFFFF))
        hex_colors.append(color)
    return hex_colors

print("The list of hexadecimal colors is:", list_of_hexa_colors(5))

# Exercise 2: Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
print("Exercise 2:")

def list_of_rgb_colors(num_colors):
    rgb_colors = []
    for i in range(num_colors):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        rgb_colors.append(color)
    return rgb_colors

print("The list of RGB colors is:", list_of_rgb_colors(5))

# Exercise 3: Write a function generate_colors which can generate any number of hexa or RGB colors.
print("Exercise 3:")

def generate_colors(num_colors, color_type):
    colors = []
    if color_type == 'hexa':
        for i in range(num_colors):
            color = '#{:06X}'.format(random.randint(0, 0xFFFFFF))
            colors.append(color)
    elif color_type == 'rgb':
        for i in range(num_colors):
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            colors.append(color)
    return colors

print("The generated colors (hexa) are:", generate_colors(5, 'hexa'))
print("The generated colors (RGB) are:", generate_colors(5, 'rgb'))

## Level 3 Exercises
print("Level 3 Exercises:")

# Exercise 1: Call your function shuffle_list, it takes a list as a parameter and returns a shuffled list.
print("Exercise 1:")

def shuffle_list(lst):
    shuffled = lst[:]
    random.shuffle(shuffled)
    return shuffled

# Example usage:
print("The shuffled list is:", shuffle_list([1, 2, 3, 4, 5]))

# Exercise 2: Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
print("Exercise 2:")

def unique_random_numbers():
    return random.sample(range(10), 7)

print("The random numbers in a range of 0-9 are:", unique_random_numbers())