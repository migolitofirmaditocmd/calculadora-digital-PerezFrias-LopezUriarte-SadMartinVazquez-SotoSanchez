import os
import csv
from datetime import datetime

historial = []

def factorial(numero):
    resultado = 1
    for i in range(1,numero+1):
        resultado *= i
    return resultado

def grados_a_radianes(grados):
    pi = 3.14159
    return grados*(pi/180)

def seno_aproximado(x_radianes, precision=10):
    # x_radianes es el valor
    # precision es cuántas veces se repetirá el bucle (más es mejor)
    resultado = 0
    for i in range(precision):
        # Aquí va la lógica de la serie de Taylor
        pass
    return resultado
def calculadora_cientifica():
    pass


print(factorial(numero=5))