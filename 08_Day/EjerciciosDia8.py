#Create an empty dictionary called dog
dog = {}
print(dog)

#Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Chuby'
dog['color'] = 'Brown'
dog['breed'] = 'Sharpei'
dog['legs'] = 4
dog['age'] = 7
print(dog)

#Create a student dictionary and add first_name, last_name,
#gender, age, marital status, skills, 
#country, city and address as keys for the dictionary
student ={
 'first_name': 'Omar',
 'last_name': 'Mendoza',
 'Gender' : 'Men',
 'age' : 19,
 'marital status' : 'Single',
 'skills' : ['DJ'],
 'country' : 'Mexico',
 'city' : 'Aguascalientes',
 'address' : 'Trojes de San Cristobal'
}
print(student)

#Get the length of the student dictionary
print(len(student))

#Get the value of skills and check the data type, it should be a list
print(student['skills'])

#mopdify the skills values by adding one or two skills

