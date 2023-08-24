import math
#Pedirle al usuario que igrese la fecha actual: 
fechaActual = str(input ("Ingresar la fecha actual en el siguiente formato: (dia,DD/MM) "))
#Buscar que dias y numeros ingreso el usuario: 
diaIngresado = (fechaActual.split(',')[0]).lower()
numeroDia = int((fechaActual.split(',')[1].split('/')[0])) 
numeroMes = int((fechaActual.split(',')[1]).split('/')[1])

if(diaIngresado== "lunes" or diaIngresado == "martes" or diaIngresado == "miercoles"
  or diaIngresado == "jueves" or diaIngresado == "viernes"):
    if(numeroDia >= 1 and numeroDia <= 31):
        if(numeroMes >= 1 and numeroMes <= 12):
            if(diaIngresado == "lunes" or diaIngresado == "martes" or diaIngresado == "miercoles"):
                examen = input ("¿Hubo examen? SI/NO :")
                examen= examen.lower()
                if(examen == "si"):
                    aprobados = int(input("Ingresar el numero de aprobados: "))
                    desaprobados = int(input("Ingresar el numero de cuantos desaprobaron: "))
                    porcentajeAprobados = 100*aprobados/(aprobados+desaprobados)

                    print(f"El porcentaje de alumnos aprobados es de: {porcentajeAprobados}%")
                elif(examen == "no"):
                      print("Ese día NO hubo examen. ")
                else: 
                    print("Se produjo un error. ")
            elif(diaIngresado == "jueves"):
                asistencia = int(input("Ingresar el porcentaje de los que asistieron: "))
                if(asistencia>50):
                 print("Asistió la mayoria. ")
                else: 
                    print("NO asistio la mayoria. ")
            elif(diaIngresado == "viernes"):
                if((numeroDia == 1 and numeroMes == 1) or numeroMes == 7):
                    print("Comienzo de nuevo ciclo. ")
                alumnosIngresantes = int(input("Ingresar la cantidad de almunos nuevos: "))
                arancel = int(input("Ingresar la cantidad de arancel por alumno: "))
                print(f"El ingreso total es de: ${alumnosIngresantes*arancel}")