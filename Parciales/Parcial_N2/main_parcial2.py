from funciones_parcial import *


def main():
    
    # Leemos la matriz 6x6 desde el teclado ingresada por el usuario
    dna = []
    for i in range(6):
        dna_str = input(("Ingrese una cadena que contenga (ATCG): ").strip()).upper()
    # Verificamos si la matriz ingresada por el usuario es válida
        while len (dna_str) != 6:
            dna_str = input("Cadena incorrecta, ingrese una valida: ").upper()
            num_aux=0
            if len (dna_str) == 6:
                while num_aux == 0:
                    for letter in dna_str: 
                        if not (letter == 'A' or letter == 'G' or letter == 'C' or letter == 'T'):
                            dna_str = input("Cadena con caracteres incorrectos, ingrese una valida: ").upper()
                            num_aux=1
        dna.append(dna_str)
    for str in dna:
        for letter in str: 
            print(letter, end= " ")
        print("")

    # Llamamos a la función is_mutant para verificar si la matriz ingresada representa a un mutante

    '''dna =["ATAAGA",
           "AAGTGC",
           "ATATTT",
           "GCACGG",
           "GCGTCA",
           "TCACTG"]      #(NO mutante.-)
           '''
    '''dna =  [ "AAAAAA", 
             "ACAAGC",
             "AATTAC", 
             "GTTACA",
             "CTCTTA", 
             "ACCCCT"] #(Si mutante)
             '''

    if is_mutant(dna):
        print("El humano es mutante.")
        print("Matriz ingresada: ",dna)
    else:
        print("El humano no es mutante.")
        print("Matriz ingresada: ",dna)

if __name__ == "__main__":
    main() 
    


