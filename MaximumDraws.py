#!/bin/python3
#Importamos librerias
import math
import os
import random
import re
import sys
#Declaramos la funcion.
def maximumDraws(n): #Recibe como parametro la variable n
    return n + 1 #Devuelve n + 1 ya que 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = maximumDraws(n)

        fptr.write(str(result) + '\n')

    fptr.close()
