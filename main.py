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


<<<<<<< HEAD
calculadora_cientifica()
=======
def limpiar_historial():
    """
    Limpia el historial de operaciones.
    """
    global historial

    # TODO: Implementar
    # Vaciar la lista historial
    pass


# ============================================
# SECCIÓN 5: GESTIÓN DE ARCHIVOS (Estudiante 1)
# ============================================

def actualizar_historial(operacion):
    """
        Actualiza la variable global `historial` agregando un registro de operación.

        Esta función recibe una lista con los datos de una operación matemática ya
        calculada, genera la marca de tiempo actual y construye un diccionario con
        la información necesaria para el historial. Posteriormente, añade dicho
        diccionario a la lista global `historial`.

        Formato esperado del argumento `operacion`:
            [
                resultado,   # valor numérico resultante
                titulo,      # nombre de la operación (str)
                expresion,   # representación textual de la operación (str)
                num1,        # primer operando (numérico)
                num2         # segundo operando (numérico)
            ]

        El diccionario agregado al historial contiene:
            - "titulo": nombre de la operación.
            - "resultado": resultado numérico.
            - "operacion": expresión textual.
            - "num1": primer operando.
            - "num2": segundo operando.
            - "fecha": fecha y hora en formato "YYYY-MM-DD HH:MM:SS".

        Efectos secundarios:
            Modifica la lista global `historial` añadiendo un nuevo registro.

        Requisitos:
            - La variable global `historial` debe existir y ser una lista.
            - El módulo `datetime` debe estar importado.

        Args:
            operacion (list): Lista con los datos de la operación en el orden
                [resultado, titulo, expresion, num1, num2].

        Returns:
            None
        """
    global historial
    ahora = datetime.now()
    datos_a_guardar = {"titulo": operacion[1],
                       "resultado": operacion[0],
                       "operacion": operacion[2],
                       "num1": operacion[3],
                       "num2": operacion[4],
                       "fecha": ahora.strftime("%Y-%m-%d %H:%M:%S")}
    historial.append(datos_a_guardar)

def guardar_historial_archivo():
    """
    Guarda el historial en los archivos datos.csv e historial.txt
    """

    # TODO: Implementar
    # 1. Crear carpeta "datos" .gitkeep no existe (usar os.makedirs())
    # 2. Abrir archivo "datos/historial.txt" en modo escritura ("w")
    # 3. Escribir cada línea del historial al archivo
    # 4. Cerrar archivo

    # Ejemplo:
    # if not os.path.exists("datos"):
    #     os.makedirs("datos")
    #
    # with open("datos/historial.txt", "w") as archivo:
    #     for linea in historial:
    #         archivo.write(linea + "\n")

    pass


def cargar_historial_archivo():
    """
    Carga el historial desde el archivo datos/historial.txt
    """
    # TODO: Implementar
    # 1. Verificar .gitkeep el archivo existe (os.path.exists())
    # 2. Si existe:
    #    - Abrir archivo en modo lectura ("r")
    #    - Leer todas las líneas
    #    - Agregar cada línea (sin \n) a la lista historial
    # 3. Si no existe, no hacer nada

    pass

actualizar_historial()
actualizar_historial()
actualizar_historial()
guardar_historial_archivo()


#codigo de temperaturas 

def convertir_temperatura():
    print("--- Conversor de Temperatura ---")
    print("1. Celsius a Fahrenheit/Kelvin")
    print("2. Fahrenheit a Celsius/Kelvin")
    print("3. Kelvin a Celsius/Fahrenheit")
    print("4. Salir")

    while True:
        opción = input("\nSelecciona una opción (1-4): ")

        if opción == '4':
            print("¡Hasta luego!")
            break

        if opcion in ['1', '2', '3']:
            try:
                temp = float(input("Ingresa el valor de la temperatura: "))
            except ValueError:
                print("Error: Ingresa un número.")
                continue

            if opción == '1': # C -> F, K
                f = (temp * 9/5) + 32
                k = temp + 273.15
                print(f"Resultado: {temp}°C equivale a {f:.2f}°F y {k:.2f}K")
            
            elif opcion == '2': # F -> C, K
                c = (temp - 32) * 5/9
                k = c + 273.15
                print(f"Resultado: {temp}°F equivale a {c:.2f}°C y {k:.2f}K")
            
            elif opción == '3': # K -> C, F
                c = temp - 273.15
                f = (c * 9/5) + 32
                print(f"Resultado: {temp}K equivale a {c:.2f}°C y {f:.2f}°F")
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    convertir_temperatura() 
