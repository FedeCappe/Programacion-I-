from clases_tp9 import Cuenta
from clases_tp9 import Persona
#Ejercicio 1
person1 = Persona()
ingresar_nombre=input("Ingrese su nombre: ")
person1.nombre= ingresar_nombre
ingresar_dni=input("Ingrese su dni (sin puntos): ")
while len(ingresar_dni)<7 or len(ingresar_dni)>8:
    print("El dni debe ser valido.")
    ingresar_dni=input("Ingrese otra vez su dni(sin puntos): ")
person1.dni=ingresar_dni
ingresar_edad=int(input("Ingrese su edad: "))
person1.edad=ingresar_edad

person1.Mostrar()
print(person1.EsMayorEdad())

#Ejercicio 2
miCuenta=Cuenta()
ingresar_titular=input("Ingrese el nombre del titular ed la cuenta: ")
miCuenta.titular= ingresar_titular
op=" "
while op!="4":
    op=input("Eliga una opcion:\n 1)Mostrar datos\n 2)Depositar\n 3)Retirar\n 4)Salir\n Opcion: ")
    if op=="1":
        miCuenta.Mostrar()
    elif op=="2":
        miCuenta.Ingresar()
    elif op=="3":
        miCuenta.Retirar()
    elif op=="4":
        print("Saliendo...")
        break
    else:
        print("Opcion incorrecta")

#Ejercicio 3
