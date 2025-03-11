
#Write a script that prompts the user to enter base and height of 
#the triangle and calculate an area of this triangle (area = 0.5 x b x h

#Ejercicio 1
# Declare your age as an integer variable
edad = 19
print("tu edad es: ", edad)

#Ejercicio 2
# Declare your name as a floa variable
altura = 1.70  
print("tu altura es: ", altura)

#Ejercicio 3
# Declare a complex number variable
numero = 3j
print("tu numero complejo es: ", numero)

#Ejercicio 4
# Declare a script that prompts the user to enter 
# base and height of the triangle and calculate an area of this triangle
base = float(input("Ingrese la base del triangulo: "))
altura = float(input("Ingrese la altura del triangulo: "))
area = 0.5 * base * altura
print("El area del triangulo es: ", area)
# Este ejercicio da la base de un triangulo y la altura y calcula el area del triangulo

# Ejercicio 5
# Write a script that prompts the user to enter side a, side b, and side c of the triangle.
#  Calculate the perimeter of the triangle (perimeter = a + b + c).
a = float(input("Ingrese el lado a del triangulo: "))
b = float(input("Ingrese el lado b del triangulo: "))
c = float(input("Ingrese el lado c del triangulo: "))
perimetro = a + b + c
print("El perimetro del triangulo es: ", perimetro)
# Este ejercicio pide los lados de un triangulo y calcula el perimetro del triangulo

# Ejercicio 6
#Get length and width of a rectangle using prompt. Calculate its area
area = 0.5 * base * altura
base = float(input("Ingrese la base del triangulo: "))
altura = float(input("Ingrese la altura del triangulo: "))
print("El area del triangulo es: ", area)
perimetro = a + b + c
a = float(input("Ingrese el lado a del triangulo: "))
b = float(input("Ingrese el lado b del triangulo"))
c = float (input("Ingrese el lado c del triangulo"))
print("El perimetro del triangulo es: ", perimetro)
# Este ejercicio pide la base y la altura de un triangulo y calcula el area del triangulo

# Ejercicio 7
# #Get radius of a circle using prompt. Calculate the area
print("Calcula el area y la circunferencia de un circulo")
radio = float(input("Ingrese el radio del circulo: "))
pi = 3.14
area = pi * radio ** 2
circunferencia = 2 * pi * radio
print("El area del circulo es: ", area)
print("La circunferencia del circulo es: ", circunferencia)
# Este ejercicio pide el radio de un circulo y calcula el area y la circunferencia del circulo

# Ejercicio 8
#Calculate the slope
print("")
print("Interaccion de la pendiente:")
m = 2
intY = -2     
intX = intY / m 
print("La pendiente de la ecuacion es: ", m)
print("La interacción es de: ", intX) 
# Este ejercicio calcula la pendiente de una ecuacion

#Ejercicio 9
##Find the slope and Euclidean distance between point
print("")
x1 = 2
x2 = 6
y1 = 2
y2 = 10
dist = ((x2 - x1)**2 + (y2-y1)**2)**0.5
print("La distancia entre los dos puntos es: ", dist)
slope = (y2 - y1) / (x2 - x1)
print("The slope is: ", slope)
# Este ejercicio calcula la pendiente y la distancia euclidiana entre dos puntos

#Ejercicio 10
#Compare the slopes in tasks 8 and 9
print("")
Compare = m <= slope
print("La diferencia entre las pendientes es de: ", Compare)
# Este ejercicio compara las pendientes de dos ecuaciones

##Calculate the value of y (y = x^2 + 6x + 9). 
# Try to use different x values and figure out at 
# what x value y is going to be 0.
print("")
x = int(input("Ingresa el valor de X "))
y = (x**2 + (6 * x) + 9) 
print("Y= ", y)

##Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print("")
python = str(55)
dragon = str(3)

comp = python == dragon
print(len(python))
print(len(dragon))
print("La comparación de los numeros fue: ", comp)

##Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("")

on = ("python" and "dragon")
if  "dragon" in on:
    print("on is in dragon and python")


##I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print("")
course = ("I hope this course is not full of jargon")
if "jargon" in course:
    print("jargon is in the sentence")
else :
    print("no")

##There is no 'on' in both dragon and python
print("")
promt=("pyth" and "drag")
if "on" in promt:
    print("on is in the sentence")
else: 
    print("on isn´t in these sentences")

##Find the length of the text python and convert the value to float and convert it to string
print("")
print("Una prueba de longitud con la funcion len")
text = str(float("654864643215"))
len(text)
print("La longitud de la frase es de: ", len(text))

##Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
print("")
par = int(input("Ingresa un numero: "))
par = (par % 2)
if par > 0:
 print("Es numero inpar")

else:
    print("Es numero par")


##Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print("")
floDiv = 7 // 3
intPi = int(2.7)
comDiv = floDiv == intPi

print("El resultado de la division es:", comDiv)

##Check if type of '10' is equal to type of 10
print("")
ty1 = type("10")
ty2 = type(10)
comTy = ty1 == ty2
print("Los tipos de las unidades son iguales? ", comTy)

##Check if int('9.8') is equal to 10
print("")
typ1 = int(float("9.8"))
typ2 = 10
comTyp = typ1 == typ2
print("Los tipos de las unidades son iguales? ", comTyp)

##Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
print("")
hours = int(input("Ingresa las horas que trabajaste: "))
rate = int(input("Ingresa el valor de la tarifa por hora: "))
salario = hours * rate
print("Tu salario es de ", "|", salario, "|" )

##Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
años = int(input("Cuantos anos tienes? "))
segundo = (365 * (3600*24))
total = (años * segundo)
print("Tu tienes un total de:", total, "segundos")

##Write a Python script that displays the following table
for i in range(1, 6):  # Genera números del 1 al 5
    print(f"{i:<7} {1:<11} {i:<11} {i**2:<11} {i**3:<11}")

for i in range(1, 6):  # Números del 1 al 5
    print(i, 1, i, i**2, i**3)


