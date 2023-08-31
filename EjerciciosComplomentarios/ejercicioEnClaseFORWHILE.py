abecedario = "abcdefghijklmnñopqrstuvwxyz"
corrimiento = int(input("Ingrese el numero que desea correr la letra: "))

for i in range(5):
    mensaje = input("Ingrese el mensaje: ").lower()
    mensaje_Incriptado = " "
    for letra in mensaje: 
        if letra in mensaje: 
            indice = abecedario.find(letra)
            indice = (indice + corrimiento )%27
            mensaje_Incriptado += abecedario[indice]
        else: 
            mensaje_Incriptado += letra
    print(mensaje_Incriptado)
    
    '''2.Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 
    0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene.
    Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.'''

num = int(input("Ingrese un numero entero: "))
totalPares = 0
totalImpares = 0

while num!=0:
   pares=0
   impares=0
   while num!=0:   
     digito=num%10
     if (digito%2==0):
       pares+=1
       totalPares+=1
     else:
       impares+=1
       totalImpares+=1
     num=num//10
   #print("El número ingresado tiene ",pares," digitos pares y ",impares," digitos impares")
   num=int(input("Ingrese otro numero: "))
print("Total de dígitos pares:", totalPares)
print("Total de dígitos impares:", totalImpares)