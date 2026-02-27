import os
import csv
from datetime import datetime

historial = []

def sumar(a, b):
    return [a + b, "suma",f"{a}+{b}",a,b]

def mostrar_historial():

    global historial

    # TODO: Implementar
    # 1. Verificar .gitkeep historial está vacío
    # 2. Si está vacío, mostrar mensaje
    # 3. Si no, iterar sobre historial y mostrar cada operación numerada

    pass


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