
# 16. Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.

nombre = input ("Ingresar su nombre: ") 
apellido1 = input("Ingrese su primer apellido: ")
apellido2 = input("Ingresar su segundo apelldio: ") 

iniciales = print("La iniciales son: ",nombre[0]," ",apellido1[0]," ", apellido2[0])

'''17.Solicitar al usuario que ingrese su nombre. El nombre se debe almacenar en una variable llamada usuario. 
A continuación mostrar por pantalla: “Ahora estás en la matrix, [nombre del usuario]”.'''

usuario = input ("Ingresar su nombre por favor:  ") 
print("Ahora estas en la matrix,",usuario)


'''18.Hacer un programa que solicite al usuario cuánto costó una cena en un restaurante. A ese valor, 
sumarle un 6.2% en concepto de servicio y un 10% de propina. Imprimir en pantalla el monto final a pagar.'''

precioCena =  float(input("Ingresar que monto le salio la cena: "))

precioFinal = precioCena+(precioCena*0.10)+(precioCena*6.2/100)

print("En el monto final a pagar es de:  ",precioFinal)