#Ejercicio 1
class Persona:
    
    def __init__(self):
        self.__nombre=None
        self.__edad=0
        self.__dni=0

    #Getter
    @property 
    def nombre(self):
        return self.__nombre
    @property 
    def edad(self):
        return self.__edad
    @property 
    def dni(self):
        return self.__dni

    #Setter
    @nombre.setter 
    def nombre(self, new_nombre):
        self.__nombre = new_nombre

    @edad.setter 
    def edad(self, new_edad):
        self.__edad = new_edad

    @dni.setter 
    def dni(self, new_dni):
        self.__dni = new_dni

    def Mostrar(self):
        print(f"El nombre es: {self.__nombre}")
        print(f"La edad es: {self.__edad}")
        print(f"El DNI es: {self.__dni}")

    def EsMayorEdad(self):
        if self.edad>=18:
            return True
        else:
            return False

#Ejercicio 2
class Cuenta:
    def __init__(self):
        self.__titular= ""
        self.__cantidad=0.0

    #Getter
    @property 
    def titular(self):
        return self.__titular
    
    @property 
    def cantidad(self):
        return self.__cantidad
    
    
    #Setter
    @titular.setter 
    def titular(self, new_titular):
        self.__titular = new_titular

    
    @cantidad.setter 
    def cantidad(self, new_cantidad):
        self.__cantidad = new_cantidad


    def Mostrar(self):
        print(f"El titular de la cuenta es: {self.__titular}")
        print(f"La cantidad de dinero que tine en la cuenta es: {self.__cantidad}")

    def Ingresar(self):
        cant=float(input("Ingrese la cantidad de dinero: "))
        if cant<=0:
            print("No se puede ingresar una cantidad negativa o igual a 0")
        else:
            self.__cantidad+=cant

    def Retirar(self):
        retiro=float(input("Ingrese la cantidad de dinero: "))
        self.__cantidad-=retiro
#Ejercicio 3
