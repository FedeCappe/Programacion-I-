from random import *

#Ejercicio 1
def count_digits(n):
    if len(str(n))==1:
        return 1
    return 1+count_digits(n//10)
numero = int(input("Ingrese un número positivo: "))
while True and numero != 0:
 
 if numero > 0:
     print("El número tiene", count_digits(numero), "dígito(s).")
 else: 
     print ("Numero entero POSITIVO INCORRECTO. ") 
     break
 numero = int(input("Ingrese un número positivo: "))
 
#Ejercicio 2
def es_potencia(n, b):
    if n == b :
        return True
    elif n<b:
        return False
    return es_potencia(n-b,b)

n = int(input("Ingrese un número n: "))
b = int(input("Ingrese un número b: "))

if es_potencia(n, b):
    print(f"{n} es una potencia de {b}.")
else:  
    print(f"{n} no es una potencia de {b}.")

#Ejercicio 3
def encontrar_posiciones(a, b):
    posiciones = []
    index = a.find(b)
    
    while index != -1:
        posiciones.append(index)
        index = a.find(b, index + 1)
    
    return posiciones


cadena_a = "Un tete a tete con tete"
cadena_b = "te"

posiciones = encontrar_posiciones(cadena_a, cadena_b)
print(f"Las posiciones de '{cadena_b}' en '{cadena_a}' son: {posiciones}")

#Ejercicio 4
def par(n):
    if n == 0:
        return True  
    else:
        return impar(n - 1)
def impar(n):
    if n == 0:
        return False  
    else:
        return par(n - 1)

numero = int(input("Ingrese un numero: "))
if par(numero):
    print(f"{numero} es un número par.")
else:
    print(f"{numero} es un número impar.")

#EJERCICIO 5
def max_list_num(array, i, max_num):
    if((len(array)-1) >= i):

        if(array[i] > max_num):
            max_num = array[i]
        
        return max_list_num(array, i+1, max_num)
    
    else:
        return max_num
array = []

for i in range(10):
    num = int(randint(0,10))
    array.append(num)

print(f"La lista es: {array}")

print(f"El número mas grande de la lista es: {max_list_num(array, 0, 0)}")

#Ejercicio 6
def repeat_num_list(array, num_repeats):
    if not array:
        return []

    current_element = array[0]
    repeated_elements = [current_element] * num_repeats

    return repeated_elements + repeat_num_list(array[1:], num_repeats)
array = []

num = int(input("Ingrese la cantidad de elementos que va a tener el arreglo: "))
repeat_num = int(input("Ingrese la cantidad de veces que desea que se repitan los números: "))

for i in range(num):
    num = int(randint(0,6))
    array.append(num)

print(f"El array original es: {array}")

print(f"El array con los números repetidos es: {repeat_num_list(array, repeat_num)}")

#Ejercicio 7
def sum_recursiv(n,p):
    if (n>1):
     return (p*n) + sum_recursiv(n-1,p)
    elif(n <=0):
        return"n no puede valer ni ser menor a 0"
    elif n == 1: 
       return p
num1 = int(input("Ingrese p, como número entero: "))
num2 = int(input("Ingrese n, como número entero: "))
print("K vale: ",sum_recursiv(num2,num1))

#Ejercicio 8
def calcular_valor_pascal(fil, column):
    if column == 0 or column==fil:
        return 1
    else:
        return calcular_valor_pascal(fil - 1, column - 1) + calcular_valor_pascal(fil - 1, column)
fil_in = int(input("Ingrese el número de fila: "))
colum_in = int(input("Ingresa el número de la columna: "))
while fil_in <0 and colum_in<0:
    fil_in = int(input("Ingrese el número de fila (No puede valor menos de 0): "))
    colum_in = int(input("Ingresa el número de la columna (No puede valor menos de 0): "))
print("El valor en la piramide de pascal es: ", calcular_valor_pascal(fil_in,colum_in))

#Ejercicio 9
def combinations(char,n,built_chain=""):
    if n==0:
        print(built_chain)
        return  
    else:
        for i in char:
            combinations(char,n-1,built_chain+i)
list_characters=["&","?","#","%","!"]
number=3
combinations(list_characters,number)
#Ejercicio 10
def sheet_measurement(n):
    if n==0:
        return(841,1189)
    previous_width, previous_length = sheet_measurement(n-1)
    if n % 2 == 1:
        return (previous_length, previous_width // 2)
    else:
        return (previous_width // 2, previous_length)
number=1
while True:
    number=int(input("Ingrese un numero mayor que 0: "))
    if number>0:
        break
    
width, length = sheet_measurement(number)
print(f'Ancho de A{number}: {width} mm, Largo de A{number}: {length} mm')

