import random

#EJERCICIO EN CLASE 1
def recursive_mouse(minutes_counter):

    option = random.randint(1, 3)

    if(option == 3):
        return minutes_counter+7

    elif(option == 1):
        return recursive_mouse(minutes_counter+5)
    
    elif(option == 2):
        return recursive_mouse(minutes_counter+3)
    
#EJERCICIO EN CLASE 2
def f(n):
    s = str(n)
    if (len(s) <= 1):
        return s
    return s[-1] + f(int(s[:-1]))
