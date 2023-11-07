from motocicleta import Motocicleta


moto_one = Motocicleta('azul','ad330',10,2,"","",2022,200,500,'Encendido')
print("El color de la moto es: ",moto_one.color)
print("La patente es: ",moto_one.patent)
print("La cantidad de litros que tiene el tanque es de: ",moto_one.fuel_liters)
print("Tiene ",moto_one.numers_whels, " ruedas.")
print("Año fabricacion: ",moto_one.date_manugacturing)
print("Velocidad max: ",moto_one.speed_tip)
print("El peso de la moto es: ",moto_one.weight)
print("La moto esta: ",moto_one.engine)

print("----Preguntamos marca y modelo de la moto---------")

moto_one.__brand = input("Ingrese la marca de la Moto: ")
moto_one.model = input("Ingrese el modelo de la moto: ")
print("La marca de la moto es: ",moto_one.__brand)
print("El modelo de la moto es: ",moto_one.model)


print("----------------Añadimos una segunda moto-------------------")

moto_two = Motocicleta('roja','ad330',10,2,"","",2022,250,650,'Encendido')
print("El color de la moto es: ",moto_two.color)
print("La patente es: ",moto_two.patent)
print("La cantidad de litros que tiene el tanque es de: ",moto_two.fuel_liters)
print("Tiene ",moto_two.numers_whels, " ruedas.")
print("Año fabricacion: ",moto_two.date_manugacturing)
print("Velocidad max: ",moto_two.speed_tip)
print("El peso de la moto es: ",moto_two.weight)
print("La moto esta: ",moto_two.engine)

print("----Preguntamos marca y modelo de la moto---------")

moto_two.__brand = input("Ingrese la marca de la Moto: ")
moto_two.model = input("Ingrese el modelo de la moto: ")
print("La marca de la moto es: ",moto_two.__brand)
print("El modelo de la moto es: ",moto_two.model)



moto_one.encender_engine() #Enciendo la moto.
moto_two.encender_engine()

moto_one.apagar_engine() #Apago la moto.
moto_one.apagar_engine()


moto_one.precio = 1500000  #Le añado un precio a la moto.
print(f"El valor de la moto: Marca: {moto_one.__brand}, Modelo: {moto_one.model} es de: ${moto_one.precio}")  #Mostramos el precio de la moto.

print("Precio de la moto uno: ",moto_one.consultar_precio())
print("Precio de la moto uno: ",moto_two.consultar_precio())  #Aca arroja "None", porque no le hemos definido un precio.


