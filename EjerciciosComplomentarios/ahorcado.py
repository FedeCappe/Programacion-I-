import random

#Crear una lista de palabras: 
words = ["auto","camioneta","cancha","futbol","hinchada","computadora","teclado","mouse","monitor","celular"]
#Le indico la cantidad maxima de fallos: 
max_failed = 6

#Creo la funcion para que busque una palabra al azar y la oculte con "_" : 

def search_random_word():
     random_word = random.choice(words)
     secret_word = "_"*len(random_word)
     return random_word,secret_word 

#Creo la funcion para remplazar la letra encontrada y en la posiciones que se encuntran: 

def replace_letter(original,secret,letter):
     amount = original.count(letter)
     inicio = 0 
     for i in range(amount):
          position = original.find(letter,inicio)
          secret = secret[:position]+letter+secret[position+1:]
          inicio = position+1
     return secret

#Creo la funcion con las reglas del juego: 

def ahorcado():
     print (f"Bienvenido al juego del AHORCADO. Podes fallar {max_failed} veces. ")
     input("Presione ENTER para iniciar el juego...")
     original, secret = search_random_word() 
     fallos = 0 
     while secret != original and fallos < max_failed:
          print(f"Palabra: {secret}")
          letter = input("Ingrese una letra a adivinar: ").lower()
          if letter in original:
               secret = replace_letter(original, secret, letter)
               print("Muy bien, adivinaste una letra!!!! ")
          else:
               print("Incorrecto, la letra ingresada no se encuentra en la palabra que desea desifrar. ")
               fallos+=1
               print(f"La cantidad de fallos que llevas: {fallos}")
          input("Presione ENTER para seguir jugando...")
     if secret == original: 
           print(f"Felicidades, la palabra adivinada es:  {secret}")
     else: 
          print(f"Incorrecto, usted no ha desifrado la palabra. La palabra era: {original}")
          print("Muchas gracias por haber jugado. Saludoss !! ")
     

def main():
     ahorcado()

if __name__ == '__main__':
    main()




