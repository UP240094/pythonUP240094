##Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
T="thirty_"
D="days_"
F="of_"
P="python_"
TDFP=(T+D+F+P)
print(TDFP)

##Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'
C="Coding_"
fo="For_"
A="All_"
CfoA= C+fo+A
print (CfoA)

##Declare a variable named company and assign it to an initial value "Coding For All".
company=CfoA
print(company)

##Print the length of the company string using len() method and print().
print(len(company))

##Change all the characters to uppercase letters using upper() method.
print(company.swapcase())

##Change all the characters to lowercase letters using lower() method.
print(company.swapcase().swapcase())

##Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.swapcase().swapcase().capitalize())

##Cut(slice) out the first word of Coding For All string.
language = company.swapcase().swapcase().capitalize()
Coding=language[0:6]
print(Coding)

##Check if Coding For All string contains a word Coding using the method index, find or other methods.
index=language
if "Coding" in language:
    print("Coding is in Coding for all")

##Replace the word coding in the string 'Coding For All' to Python.
pythonfrase=language.replace("Coding", "Python")

print(pythonfrase)

##Change Python for Everyone to Python for All using the replace method or other methods.
pythonfrase2=pythonfrase.replace("all", "everyone")
print(pythonfrase2)

##Split the string 'Coding For All' using space as the separator (split()) .
print(language.split())

##"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
marca="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(marca.split(', '))

##What is the character at index 0 in the string Coding For All.
print(language[0:1])

##What is the last index of the string Coding For All.
print(language[13:14])

##What character is at index 10 in "Coding For All" string.
print(language[9:10])

##Create an acronym or an abbreviation for the name 'Python For Everyone'.
print(pythonfrase2.strip('ython_for_everyone'), pythonfrase2[7:8], pythonfrase2[11:12])

##Create an acronym or an abbreviation for the name 'Coding For All'.
print(language[0:1], language[7:8], language[11:12])

##Use index to determine the position of the first occurrence of C in Coding For All.
print(language.index('C'))

##Use index to determine the position of the first occurrence of F in Coding For All.
print(language.index('f'))

##Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(language.index('l'))

##Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence="You cannot end a sentence with because because because is a conjuction"
print(sentence.index('because'))

##Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because',30))

##Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.replace('because because because', ''))

##Does ''Coding For All' start with a substring Coding?
print(language.startswith('Coding'))

##Does 'Coding For All' end with a substring coding?
print(language.endswith('coding'))

##'   Coding For All      '  , remove the left and right trailing spaces in the given string.
ej30=" Coding For All "
print(ej30.strip(' '))

##Which one of the following variables return True when we use the method isidentifier():
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

##The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
lista=['Django','Flask','Bottle','Pyramid','Falcon']
print(' '.join(lista))

##Use the new line escape sequence to separate the following sentences
print("I am enjoying this challenge.\nI just wonder what is next.")

##Use a tab escape sequence to write the following lines
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

##Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square.".format(radius, int(area)))

##Make the following using string formatting methods:
a = 8
b = 6

print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))