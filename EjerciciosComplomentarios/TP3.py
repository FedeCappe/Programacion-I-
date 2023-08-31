# 1-Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
'''
word = input("Ingrese una palabra: ")

for i in range(10):
    print(word)
'''
'''2-Escribir un programa que pregunte al usuario su edad y 
muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).'''
'''
age = int(input("Ingrese su edad: "))
year= 1
for i in range(age):
    print(year)
    year+=1

'''
'''3-Escribir un programa que pida al usuario un número entero positivo y 
muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.'''

number = int(input("Ingresar un numero entero positivo: "))
for i in range(1,number+1):
    if(i%2 != 0):
        print(i,end=", ")

''' 4-Escribir un programa que pida al usuario un número entero positivo y 
muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.'''

number = int(input("Iingrese un numero entero positivo: "))

for i in range(number+1):
    print(number,end=", ")
    number-=1

''' 5-Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y 
    muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.'''

amount = float(input("Ingresar la cantidad a invertir: "))
interest = float(input("Ingrese el interes anual: "))
year = int(input("Ingresar por cuantos años desea invertirlos: "))

for i in range(year): 
    amount += amount*interest/100
    print(i+1,"Capital obtenido: ",round(amount,2))
print("Debido a los intereses que genero, ahora el capital es de: ",amount)