#!/bin/python3
#Importamos librerias
import math
import os
import random
import re
import sys
#Declaramos la funcion.
def maximumDraws(n): #Recibe como parametro la variable n
    return n + 1 #Devuelve n + 1 ya que si sacamos un calcetin de un color, aun debemos sacar otro para que sea el par completo.

if __name__ == '__main__': #Ejecuta el script directamente 
    fptr = open(os.environ['OUTPUT_PATH'], 'w') #Abre el archivo que le asigna la pagina Hackerrank para darle los valores de entrada.

    t = int(input().strip()) #Lee el numero de de casos prueba.

    for t_itr in range(t): #Ciclo for para iterar sobre los casos de prueba que esta dentro del rango de la variable t.
        n = int(input().strip()) #Lee el numero de colores de calcetines (n) para el caso de prueba actual.

        result = maximumDraws(n) #Se llama a la funcion para obtener el resultado.

        fptr.write(str(result) + '\n') #Escribe los valores de salida en el archivo que maneja Hackerrank automaticamente.

    fptr.close() #Se cierra el archivo
