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

def calcular_seno_aproximado(grad,precision=10):
    # x_radianes es el valor
    # precision es cuántas veces se repetirá el bucle (más es mejor)
    x_radianes = grados_a_radianes(grad)
    seno_aproximado = 0
    for n in range(precision):
        potencia = 2 * n + 1
        termino = ((-1) ** n) * (x_radianes ** potencia) / factorial(potencia)
        seno_aproximado += termino

    return seno_aproximado

def calcular_coseno_aproximado(grad,precision=10):
    # x_radianes es el valor
    # precision es cuántas veces se repetirá el bucle (más es mejor)
    x_radianes = grados_a_radianes(grad)
    coseno_aproximado = 0
    for n in range(precision):
        potencia = 2 * n
        termino = ((-1) ** n) * (x_radianes ** potencia) / factorial(potencia)
        coseno_aproximado += termino

    return coseno_aproximado

def calcular_tangente_aproximada(grad):
    coseno = calcular_coseno_aproximado(grad)
    if abs(coseno) < 1e-10:
        return "Indefinida"
    return calcular_seno_aproximado(grad)/coseno

def calculadora_cientifica():
    booleano = True
    while booleano:
        usuario = str(input("¿Que es lo que quiere calcular(seno/coseno/tangente/N para salir)?: ").lower())
        if usuario == "seno":
            grados_usuario = float(input("Ingrese los grados a evaluar: "))
            print(f"Resultado: {calcular_seno_aproximado(grad=grados_usuario)}")
        elif usuario == "coseno":
            grados_usuario = float(input("Ingrese los grados a evaluar: "))
            print(f"Resultado: {calcular_coseno_aproximado(grad=grados_usuario)}")
        elif usuario == "tangente":
            grados_usuario = float(input("Ingrese los grados a evaluar: "))
            print(f"Resultado: {calcular_tangente_aproximada(grad=grados_usuario)}")
        elif usuario == "n":
            print("Saliendo...")
            booleano = False
        else:
            print("Error.Input invalido")


calculadora_cientifica()