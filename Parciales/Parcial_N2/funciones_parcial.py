

    # Funcion para recorrer las diagonales
def diagonal_secuence(matriz):
        secuence = []
        aux = []
        x=0

        for i in range(0,6):
            aux.append(matriz [x][i])
            x+=1
        secuence.append(aux)
        aux = []
        x = 1 
        for i in range(0,5):
            aux.append(matriz[i][x])
            x += 1
        secuence.append(aux)
        aux = []

        x = 2

        for i in range(0,4):
            aux.append(matriz[i][x])
            x += 1
        secuence.append(aux)
        aux = []
        x = 0
        for i in range (1,6):

            aux.append(matriz[i][x])
            x += 1
        secuence.append(aux)
        aux = []
        x = 0 
        for i in range (2,6):

            aux.append(matriz[i][x])
            x += 1
        secuence.append(aux)
        aux = []
        x = 5
     #En el siguiente for invertimos la diagonal
        for i in range(0,6):
            aux.append(matriz[x][i])
            x-=1
        secuence.append(aux)
        aux = []
        x = 4
        
        for i in range(0,5):
            aux.append(matriz[x][i])
            x-=1
        secuence.append(aux)
        aux = []

        x = 3 
        for i in range(0,4):
            aux.append(matriz[x][i])
            x-=1
        secuence.append(aux)
        aux = []

        x = 5 
        for i in range(1,6):
            aux.append(matriz[x][i])
            x-=1
        secuence.append(aux)
        aux = []   
        x = 5 
        for i in range(2,6):
            aux.append(matriz[x][i])
            x-=1
        secuence.append(aux)
        aux = []        
        
        return secuence
def is_mutant(dna):
    mutant = 0
    # Convirtiendo el arreglo en una matriz 6x6
    matriz = [list(str) for str in dna]

    # Verificando las secuencias horizontales y verticales

    for fila in matriz:
        for columna in range(len(fila) - 3):
            if fila[columna] == fila[columna + 1] == fila[columna + 2] == fila[columna + 3]:
                mutant += 1
                break

    for fila in range(len(matriz) - 3):
        for columna in range(len(matriz[0])):
            if matriz[fila][columna] == matriz[fila + 1][columna] == matriz[fila + 2][columna] == matriz[fila + 3][columna]:
                mutant +=1
                break
    diagonal = diagonal_secuence(dna)
    
    for lis in diagonal:
        for i in range(0,len(lis) -3):
            if  lis[i+1] == lis[i+2] == lis[i+3] == lis[i]:
                mutant +=1
                break
    print(mutant)
    if mutant >= 2:
        return True
