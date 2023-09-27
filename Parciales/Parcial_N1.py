
name = input("Ingresar su nombre:  ")

while True: 
 print("MENU DE JUEGOS: ")
 print("1) Juego de numeros. ")
 print("2) Juego de palabras.")
 print ("3) SALIR.")
 opcion = int(input("Ingesar una opcion de juego: "))
 if opcion == 1: 
    if(opcion == 1):

        numero = int(input(f"Por favor {name} ingrese números enteros positivos ó 0 para terminar de ingresar números: "))
        max_numero = 0
        promedio_numero = 0
        contador = 0

        while(numero < 0):
             numero = int(input(f"Por favor {name} ingrese números enteros positivos ó 0 para terminar de ingresar números: "))

        while(numero != 0):

            if(numero < 0):
                numero = int(input(f"{name} el número ingresado no es positivo ingrese otro número entero ó 0 para terminar de ingresar números: "))
                continue
        
            elif(numero % 2 == 0):
                if(numero > max_numero):
                    max_numero = numero
            elif(numero % 2 == 1):
                contador += 1
                promedio_numero += numero

            numero = int(input(f"Por favor {name} otro número entero ó 0 para terminar de ingresar números: "))
        
        if(max_numero == 0 and contador != 0):
            print("------------------------ \n"
                "No se ingresaron números par enteros positivos \n"
                f"El promedio de los números impares positivos fue {promedio_numero/contador}")
        elif(max_numero == 0):
             print("------------------------ \n"
                "No se ingresaron números par enteros positivos \n"
                "No se ingresaron números impar enteros positivos")
        elif(contador == 0):
             print("------------------------ \n"
                f"El mayor número par positivo fue {max_numero} \n"
                "No se ingresaron números impar enteros positivos")            
        else:
            print("------------------------ \n"
                    f"El mayor número par positivo fue {max_numero} \n"
                    f"El promedio de los números impares positivos fue {promedio_numero/contador}")
 elif opcion == 2: 
     frase = input("Ingrese una frase: ").lower()
     vocal = "aeiou"
     contador = 0 
     for letra in frase:
          if letra in vocal:
               contador+=1
     print(f"La frase ingresada: {frase}. Tiene {contador}, vocales.")
 elif opcion == 3:
     print(f"{name}, ha elegido la opcion Salir. Hasta luego. ")
     break
 else:
    print("Eligio una opcion erronea, por favor, ingrese una correcta. ")
