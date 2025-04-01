#Find the length of the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 
                'Apple', 'IBM', 'Oracle', 'Amazon', 'AMD'}
print(len(it_companies))

#Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

#Insert multiple IT companies at 
# once to the set it_companies
it_companies.update(['Nvidia', 'Intel', 'AMD'])
print(it_companies)

#Remove one of the companies from the set it_companies
it_companies.remove('AMD')
print(it_companies)

#What is the difference between remove and discard
it_companies.discard ('Mazda')

#Join A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
C = A.union(B)
print(C)

#Find A intersection B
D = A.intersection(B)
print(D)

#Is A subset of B
E = A.issubset(B)
print(E)

#Are A and B disjoint sets
F = A.isdisjoint(B)
print(F)

#Join A with B and B with A
G = A.union(B)
H = B.union(A)

#Delete the sets completely
del it_companies


#Exercises: Level 3
#Convert the ages to a set and compare the 
#length of the list and the set, which one is bigger?
age = [22, 19, 24, 25, 26, 24, 25, 24]
age_set = set(age)
print(len(age))

#Explain the difference between the following data types: 
# string, list, tuple and set

nombre='Oscar'
lista=['Oscar', 'Luis', 'Maria']
tupla=('Oscar', 'Luis', 'Maria')
set={'Oscar', 'Luis', 'Maria'}

#I am a teacher and I love to inspire and teach people. 
# How many unique words have been used in the sentence? 
# Use the split methods and set to get the unique words

oracion = 'I am a teacher and I love to inspire and teach people.'.split()
L1 = []
count = 0

for item in oracion:
    if item not in L1:
        L1.append(item)
        count += 1
print(count)

print("Revisado")