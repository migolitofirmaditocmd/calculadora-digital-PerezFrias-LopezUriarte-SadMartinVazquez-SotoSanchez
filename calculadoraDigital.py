"""
Calculadora Multifuncional Interactiva - Versión Avanzada
Proyecto de Tecnología Digital

Equipo:
- Estudiante 1: [Nombre] - Estructura Principal y Gestión de Datos
- Estudiante 2: [Nombre] - Funciones Matemáticas
- Estudiante 3: [Nombre] - Conversores y Sistema de Historial

Fecha: Febrero 2026
Universidad de Guadalajara - Campus GDL
"""

import os
import csv
from datetime import datetime

# Variable global para almacenar historial (lista de strings)
historial = []

# ============================================
# SECCIÓN 1: FUNCIONES MATEMÁTICAS (Estudiante 2)
# ============================================

def sumar(a, b):
    """
    Suma dos números.

    Args:
        a (float): Primer número.
        b (float): Segundo número.

    Returns:
        list: Lista con la información de la operación en el formato:
            [
                resultado (float),
                titulo (str),
                operacion (str),
                num1 (float),
                num2 (float)
            ]
    """
    resultado = a + b
    return [resultado, "suma", f"{a} + {b}", a, b]


def restar(a, b):
    """
    Resta dos números.

    Args:
        a (float): Primer número.
        b (float): Segundo número.

    Returns:
        list: Lista con la información de la operación en el formato:
            [
                resultado (float),
                titulo (str),
                operacion (str),
                num1 (float),
                num2 (float)
            ]
    """
    resultado = a - b
    return [resultado, "resta", f"{a} - {b}", a, b]


def multiplicar(a, b):
    """
    Multiplica dos números.

    Args:
        a (float): Primer número.
        b (float): Segundo número.

    Returns:
        list: Lista con la información de la operación en el formato:
            [
                resultado (float),
                titulo (str),
                operacion (str),
                num1 (float),
                num2 (float)
            ]
    """
    resultado = a * b
    return [resultado, "multiplicacion", f"{a} * {b}", a, b]


def dividir(a, b):
    """
    Divide dos números.

    Args:
        a (float): Dividendo.
        b (float): Divisor.

    Returns:
        list | str:
            - Lista con la información de la operación si es válida:
                [
                    resultado (float),
                    titulo (str),
                    operacion (str),
                    num1 (float),
                    num2 (float)
                ]
            - Mensaje de error si se intenta dividir entre cero.
    """
    if b == 0:
        return "Error: No se puede dividir entre cero"

    resultado = a / b
    return [resultado, "division", f"{a} / {b}", a, b]


def modulo(a, b):
    """
    Calcula el módulo (residuo) de dos números.

    Args:
        a (float): Dividendo.
        b (float): Divisor.

    Returns:
        list | str:
            - Lista con la información de la operación si es válida:
                [
                    resultado (float),
                    titulo (str),
                    operacion (str),
                    num1 (float),
                    num2 (float)
                ]
            - Mensaje de error si el divisor es cero.
    """
    if b == 0:
        return "Error: No se puede calcular modulo con cero"

    resultado = a % b
    return [resultado, "modulo", f"{a} % {b}", a, b]


def potencia(a, b):
    """
    Calcula a elevado a la potencia b.

    Args:
        a (float): Base.
        b (float): Exponente.

    Returns:
        list: Lista con la información de la operación en el formato:
            [
                resultado (float),
                titulo (str),
                operacion (str),
                num1 (float),
                num2 (float)
            ]
    """
    resultado = a ** b
    return [resultado, "potencia", f"{a} ** {b}", a, b]


# ============================================
# SECCIÓN 2: CONVERSIÓN DE SISTEMAS NUMÉRICOS (Estudiante 2)
# ============================================

def decimal_a_binario(numero):
    """
    Convierte un número decimal entero a binario usando algoritmo manual.

    Args:
        numero (int): Número entero decimal.

    Returns:
        list | str:
            - Lista con el formato:
                [
                    resultado (str),
                    titulo (str),
                    operacion (str),
                    num1 (int),
                    num2 (None)
                ]
            - Mensaje de error si el valor no es entero.
    """
    if not isinstance(numero, int):
        return "Error: El número debe ser entero"

    if numero == 0:
        return ["0", "decimal_a_binario", f"{numero} -> binario", numero, None]

    negativo = numero < 0
    numero = abs(numero)

    resultado = ""
    while numero > 0:
        residuo = numero % 2
        resultado = str(residuo) + resultado
        numero //= 2

    if negativo:
        resultado = "-" + resultado

    return [resultado, "decimal_a_binario", f"{resultado}", numero, None]



def decimal_a_hexadecimal(numero):
    """
    Convierte un número decimal entero a hexadecimal.

    Args:
        numero (int): Número entero decimal.

    Returns:
        list | str:
            - Lista con el formato:
                [
                    resultado (str),
                    titulo (str),
                    operacion (str),
                    num1 (int),
                    num2 (None)
                ]
            - Mensaje de error si el valor no es entero.
    """
    if not isinstance(numero, int):
        return "Error: El número debe ser entero"

    if numero == 0:
        return ["0", "decimal_a_hexadecimal", f"{numero} -> hexadecimal", numero, None]

    digitos_hex = "0123456789ABCDEF"
    negativo = numero < 0
    numero = abs(numero)

    resultado = ""
    while numero > 0:
        residuo = numero % 16
        resultado = digitos_hex[residuo] + resultado
        numero //= 16

    if negativo:
        resultado = "-" + resultado

    return [resultado, "decimal_a_hexadecimal", f"{resultado}", numero, None]


def binario_a_decimal(binario):
    """
    Convierte un número binario (string) a decimal.

    Args:
        binario (str): Cadena con ceros y unos.

    Returns:
        list | str:
            - Lista con el formato:
                [
                    resultado (int),
                    titulo (str),
                    operacion (str),
                    num1 (str),
                    num2 (None)
                ]
            - Mensaje de error si contiene caracteres inválidos.
    """
    binario = str(binario).strip()

    if not all(c in "01" for c in binario):
        return "Error: El número binario solo puede contener 0 y 1"

    decimal = 0
    binario_inv = binario[::-1]

    for i in range(len(binario_inv)):
        digito = int(binario_inv[i])
        decimal += digito * (2 ** i)

    return [decimal, "binario_a_decimal", f"{binario}", binario, None]


def hexadecimal_a_decimal(hexadecimal):
    """
    Convierte un número hexadecimal (string) a decimal.

    Args:
        hexadecimal (str): Cadena hexadecimal.

    Returns:
        list | str:
            - Lista con el formato:
                [
                    resultado (int),
                    titulo (str),
                    operacion (str),
                    num1 (str),
                    num2 (None)
                ]
            - Mensaje de error si contiene caracteres inválidos.
    """
    hexadecimal = str(hexadecimal).upper().strip()
    digitos_hex = "0123456789ABCDEF"

    decimal = 0
    hex_inv = hexadecimal[::-1]

    for i in range(len(hex_inv)):
        caracter = hex_inv[i]

        if caracter not in digitos_hex:
            return f"Error: Carácter inválido '{caracter}' en número hexadecimal"

        valor = digitos_hex.index(caracter)
        decimal += valor * (16 ** i)

    return [decimal, "hexadecimal_a_decimal", f"{hexadecimal}", hexadecimal, None]


# ============================================
# SECCIÓN 3: CONVERSIÓN DE UNIDADES (COMPLETADO)
# ============================================

def bytes_a_kilobytes(bytes_val):
    """
    Convierte bytes a kilobytes.

    Args:
        bytes_val (float): Cantidad en bytes.

    Returns:
        list:
            [
                resultado (float),
                titulo (str),
                operacion (str),
                num1 (float),
                num2 (None)
            ]
    """
    resultado = bytes_val / 1024
    return [resultado, "bytes_a_kilobytes", f"{bytes_val} / 1024", bytes_val, None]


def kilobytes_a_megabytes(kilobytes):
    """
    Convierte kilobytes a megabytes.

    Args:
        kilobytes (float): Cantidad en kilobytes.

    Returns:
        list:
            [
                resultado (float),
                titulo (str),
                operacion (str),
                num1 (float),
                num2 (None)
            ]
    """
    resultado = kilobytes / 1024
    return [resultado, "kilobytes_a_megabytes", f"{kilobytes} / 1024", kilobytes, None]


def megabytes_a_gigabytes(megabytes):
    """
    Convierte megabytes a gigabytes.

    Args:
        megabytes (float): Cantidad en megabytes.

    Returns:
        list:
            [
                resultado (float),
                titulo (str),
                operacion (str),
                num1 (float),
                num2 (None)
            ]
    """
    resultado = megabytes / 1024
    return [resultado, "megabytes_a_gigabytes", f"{megabytes} / 1024", megabytes, None]

def gigabytes_a_megabytes(gigabytes):
    """
    Convierte gigabytes a megabytes.

    Args:
        gigabytes (float): Cantidad en gigabytes.

    Returns:
        list:
            [
                resultado (float),
                titulo (str),
                operacion (str),
                num1 (float),
                num2 (None)
            ]
    """
    resultado = gigabytes * 1024
    return [resultado, "gigabytes_a_megabytes", f"{gigabytes} * 1024", gigabytes, None]

def megabytes_a_kilobytes(megabytes):
    """
    Convierte megabytes a kilobytes.

    Args:
        megabytes (float): Cantidad en megabytes.

    Returns:
        list:
            [
                resultado (float),
                titulo (str),
                operacion (str),
                num1 (float),
                num2 (None)
            ]
    """
    resultado = megabytes * 1024
    return [resultado, "megabytes_a_kilobytes", f"{megabytes} * 1024", megabytes, None]

def kilobytes_a_bytes(kilobytes):
    """
    Convierte kilobytes a bytes.

    Args:
        kilobytes (float): Cantidad en kilobytes.

    Returns:
        list:
            [
                resultado (float),
                titulo (str),
                operacion (str),
                num1 (float),
                num2 (None)
            ]
    """
    resultado = kilobytes * 1024
    return [resultado, "kilobytes_a_bytes", f"{kilobytes} * 1024", kilobytes, None]


# ============================================
# SECCIÓN 4: CALCULADORA CIENTIFICA
# ============================================

def factorial(numero):
    """
    Calcula el factorial de un número entero no negativo.

    Parámetros:
        numero (int): Número entero del cual se desea calcular el factorial.

    Retorna:
        int: Resultado del factorial de 'numero'.

    Nota:
        El factorial de 0 es 1 por definición matemática.
    """
    resultado = 1
    for i in range(1,numero+1):
        resultado *= i
    return resultado

def grados_a_radianes(grados):
    """
    Convierte un ángulo en grados a radianes.

    Parámetros:
        grados (float): Ángulo expresado en grados.

    Retorna:
        float: Ángulo convertido a radianes.
    """
    pi = 3.14159
    return grados*(pi/180)

def calcular_seno_aproximado(grad,precision=10):
    """
    Calcula una aproximación del seno usando la serie de Taylor.

    Parámetros:
        grad (float): Ángulo en grados.
        precision (int, opcional): Número de términos de la serie de Taylor.
                                    Mayor valor implica mayor precisión.
                                    Por defecto es 10.

    Retorna:
        float: Aproximación del seno del ángulo dado.
    """
    x_radianes = grados_a_radianes(grad)
    seno_aproximado = 0
    for n in range(precision):
        potencia = 2 * n + 1
        termino = ((-1) ** n) * (x_radianes ** potencia) / factorial(potencia)
        seno_aproximado += termino

    return seno_aproximado

def calcular_coseno_aproximado(grad,precision=10):
    """
    Calcula una aproximación del coseno usando la serie de Taylor.

    Parámetros:
        grad (float): Ángulo en grados.
        precision (int, opcional): Número de términos de la serie de Taylor.
                                    Mayor valor implica mayor precisión.
                                    Por defecto es 10.

    Retorna:
        float: Aproximación del coseno del ángulo dado.
    """
    
    x_radianes = grados_a_radianes(grad)
    coseno_aproximado = 0
    for n in range(precision):
        potencia = 2 * n
        termino = ((-1) ** n) * (x_radianes ** potencia) / factorial(potencia)
        coseno_aproximado += termino

    return coseno_aproximado

def calcular_tangente_aproximada(grad):
    """
    Calcula una aproximación de la tangente como el cociente
    entre seno y coseno aproximados.

    Parámetros:
        grad (float): Ángulo en grados.

    Retorna:
        float | str: Valor aproximado de la tangente.
                     Retorna "Indefinida" si el coseno es cercano a 0.
    """
    if grad % 180 == 90:
        return "Indefinida"

    coseno = calcular_coseno_aproximado(grad)
    if abs(coseno) < 1e-10:
        return "Indefinida"
    return calcular_seno_aproximado(grad)/coseno

def calculadora_cientifica():
    """
    Ejecuta un menú interactivo de calculadora científica básica.

    Permite al usuario calcular:
        - Seno
        - Coseno
        - Tangente

    El usuario puede salir escribiendo 'N'.

    Los cálculos trigonométricos utilizan aproximaciones mediante
    series de Taylor.

    Returns:
        list | None:
            - Lista con la última operación realizada en el formato:
                [
                    resultado (float | str),
                    titulo (str),
                    operacion_str (str),
                    num1 (float),
                    num2 (None)
                ]
            - None si el usuario no realizó ninguna operación antes de salir.
    """
    ultima_operacion = None
    booleano = True

    while booleano:
        usuario = str(input("¿Qué quiere calcular (seno/coseno/tangente/N para salir)?: ").lower())

        if usuario == "seno":
            grados_usuario = float(input("Ingrese los grados a evaluar: "))
            resultado = calcular_seno_aproximado(grad=grados_usuario)
            print(f"Resultado: {resultado}")
            ultima_operacion = [resultado, "seno", f"sen({grados_usuario}°)", grados_usuario, None]
            actualizar_historial(ultima_operacion)

        elif usuario == "coseno":
            grados_usuario = float(input("Ingrese los grados a evaluar: "))
            resultado = calcular_coseno_aproximado(grad=grados_usuario)
            print(f"Resultado: {resultado}")
            ultima_operacion = [resultado, "coseno", f"cos({grados_usuario}°)", grados_usuario, None]
            actualizar_historial(ultima_operacion)

        elif usuario == "tangente":
            grados_usuario = float(input("Ingrese los grados a evaluar: "))
            resultado = calcular_tangente_aproximada(grad=grados_usuario)
            print(f"Resultado: {resultado}")
            ultima_operacion = [resultado, "tangente", f"tan({grados_usuario}°)", grados_usuario, None]
            actualizar_historial(ultima_operacion)

        elif usuario == "n":
            print("Saliendo...")
            booleano = False

        else:
            print("Error. Input inválido")

    return

# ============================================
# SECCIÓN 5: GESTIÓN DE HISTORIAL (Estudiante 3)
# ============================================

def mostrar_historial():
    """
    Muestra el historial de operaciones almacenado en el archivo historial.txt.

    La función realiza los siguientes pasos:
        1. Construye la ruta absoluta hacia la carpeta "datos".
        2. Verifica si el archivo "historial.txt" existe.
        3. Si el archivo existe:
            - Lee todas las líneas del archivo.
            - Si el archivo contiene datos, muestra cada operación numerada.
            - Si el archivo está vacío, muestra un mensaje indicando que no hay registros.
        4. Si el archivo no existe, muestra un mensaje indicando que los datos no están disponibles.

    Retorna:
        None

    Nota:
        El archivo debe encontrarse dentro de la carpeta "datos"
        ubicada en el mismo directorio que el script.
    """
    ruta_base = os.path.dirname(__file__)
    carpeta_datos = os.path.join(ruta_base, "datos")
    ruta_historial = os.path.join(carpeta_datos, "historial.txt")
    if os.path.exists(ruta_historial):
        with open(ruta_historial,mode="r",encoding="UTF-8") as f:
            lista_de_historial = f.readlines()
            if lista_de_historial:
                print("Historial: ")
                for indice,linea in enumerate(lista_de_historial,start=1):
                    print(f"{indice}:{linea.strip()}")
            elif not lista_de_historial:
                print("Historial vacio")
    else:          
        print("Datos no disponibles")


def limpiar_historial():
    """
    Limpia completamente el historial de operaciones.

    Vacía la lista global `historial` en memoria y borra el contenido
    de los archivos `historial.txt` y `datos.csv` dentro de la carpeta `datos`.

    Esto asegura que el historial no reaparezca al reiniciar el programa.
    """
    global historial
    historial = []
    ruta_base = os.path.dirname(__file__)
    carpeta_datos = os.path.join(ruta_base, "datos")
    ruta_historial = os.path.join(carpeta_datos, "historial.txt")
    ruta_csv = os.path.join(carpeta_datos, "datos.csv")
    open(ruta_historial, "w", encoding="utf-8").close()
    open(ruta_csv, "w", encoding="utf-8").close()

# ============================================
# SECCIÓN 6: CONVERSOR DE TEMPERATURA (COMPLETADO)
# ============================================
def convertir_temperatura():
    """
    Ejecuta un menú interactivo de conversión de temperaturas.

    Permite convertir:
        1. Celsius a Fahrenheit y Kelvin
        2. Fahrenheit a Celsius y Kelvin
        3. Kelvin a Celsius y Fahrenheit

    El usuario puede salir escribiendo '4'.

    Returns:
        list | None:
            - Lista con la última conversión realizada en el formato:
                [
                    resultado (str),
                    titulo (str),
                    operacion_str (str),
                    num1 (float),
                    num2 (None)
                ]
            - None si el usuario sale sin realizar ninguna conversión.
    """
    print("--- Conversor de Temperatura ---")
    print("1. Celsius a Fahrenheit/Kelvin")
    print("2. Fahrenheit a Celsius/Kelvin")
    print("3. Kelvin a Celsius/Fahrenheit")
    print("4. Salir")

    ultima_conversion = None

    while True:
        opcion = input("\nSelecciona una opción (1-4): ")

        if opcion == '4':
            print("¡Hasta luego!")
            break

        if opcion in ['1', '2', '3']:
            try:
                temp = float(input("Ingresa el valor de la temperatura: "))
            except ValueError:
                print("Error: Ingresa un número.")
                continue

            if opcion == '1':  # C -> F, K
                f = (temp * 9/5) + 32
                k = temp + 273.15
                resultado_str = f"{temp}°C = {f:.2f}°F, {k:.2f}K"
                print(f"Resultado: {resultado_str}")
                ultima_conversion = [resultado_str, "Celsius_a_F_K", f"C({temp}°) -> F/K", temp, None]

            elif opcion == '2':  # F -> C, K
                c = (temp - 32) * 5/9
                k = c + 273.15
                resultado_str = f"{temp}°F = {c:.2f}°C, {k:.2f}K"
                print(f"Resultado: {resultado_str}")
                ultima_conversion = [resultado_str, "Fahrenheit_a_C_K", f"F({temp}°) -> C/K", temp, None]

            elif opcion == '3':  # K -> C, F
                c = temp - 273.15
                f = (c * 9/5) + 32
                resultado_str = f"{temp}K = {c:.2f}°C, {f:.2f}°F"
                print(f"Resultado: {resultado_str}")
                ultima_conversion = [resultado_str, "Kelvin_a_C_F", f"K({temp}) -> C/F", temp, None]

        else:
            print("Opción no válida. Intenta de nuevo.")

    return ultima_conversion
# ============================================
# SECCIÓN 7: GESTIÓN DE ARCHIVOS (COMPLETADO)
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
    Persiste el historial de operaciones en archivos TXT y CSV dentro del proyecto.

    Esta función toma la lista global `historial` y la guarda en dos formatos
    dentro de la carpeta `datos` ubicada en el directorio del programa:

    1. historial.txt es la versión legible para string
       Formato: fecha | titulo: operacion = resultado

    2. datos.csv es la versión estructurada para análisis y manipulación de datos
       Columnas: fecha, titulo, num1, num2, resultado

    Si la carpeta `datos` no existe, se crea automáticamente. Los archivos se
    sobrescriben completamente con el contenido actual del historial.

    Manejo de errores:
        - Si ocurre un error al guardar en la carpeta `datos`, la función intenta
          guardar los archivos en la carpeta base del programa.
        - Si también falla la ubicación alternativa, se muestra un mensaje de
          error crítico sin detener el programa.

    Globales:
        historial (list[dict]): Lista de operaciones registradas durante la sesión.

    Returns:
        None

    Efectos secundarios:
        - Crea la carpeta `datos` si no existe.
        - Sobrescribe los archivos:
            datos/historial.txt
            datos/datos.csv
        - Puede crear archivos alternativos en la carpeta del programa si la
          carpeta `datos` no es accesible.
        - Muestra mensajes en consola si ocurre un error de escritura.
    """
    global historial

    ruta_base = os.path.dirname(__file__)
    carpeta_datos = os.path.join(ruta_base, "datos")
    os.makedirs(carpeta_datos, exist_ok=True)
    ruta_historial = os.path.join(ruta_base, "datos", "historial.txt")
    ruta_csv = os.path.join(ruta_base, "datos", "datos.csv")
    try:
        guardar_archivos(ruta_historial, ruta_csv)
    except OSError as e:
        print("No se pudo guardar en carpeta datos:", e)
        print("Intentando guardar en carpeta del programa...")
        try:
            ruta_historial_alt = os.path.join(ruta_base, "historial.txt")
            ruta_csv_alt = os.path.join(ruta_base, "datos.csv")

            guardar_archivos(ruta_historial_alt, ruta_csv_alt)

            print("Historial guardado en ubicación alternativa")

        except OSError as e2:
            print("Error crítico: no se pudo guardar el historial")
            print(e2)

def guardar_archivos(ruta_historial, ruta_csv):
    """
        Guarda el contenido del historial en rutas específicas de TXT y CSV.

        Esta función auxiliar escribe la lista global `historial` en dos archivos:
        un archivo de texto legible y un archivo CSV estructurado. Se utiliza
        internamente por `guardar_historial_archivo` para permitir reutilización
        y manejo de ubicaciones alternativas de guardado.

        Formatos generados:
            TXT:
                fecha | titulo: operacion = resultado

            CSV:
                Columnas: fecha, titulo, operacion, num1, num2, resultado

        Globals:
            historial (list[dict]): Lista de registros de operaciones.

        Args:
            ruta_historial (str): Ruta completa del archivo TXT destino.
            ruta_csv (str): Ruta completa del archivo CSV destino.

        Returns:
            None

        Raises:
            OSError: Si ocurre un error de escritura o acceso a los archivos.

        Side Effects:
            - Sobrescribe los archivos indicados.
            - Persiste en disco el contenido actual del historial.
        """
    global historial

    with open(ruta_historial, mode="w", encoding="utf-8") as f:
        for dato in historial:
            f.write(f"{dato['fecha']} | {dato['titulo']}: "
                    f"{dato['operacion']} = {dato['resultado']}\n")
    with open(ruta_csv, mode="w", encoding="utf-8", newline="") as f:
        campos = "fecha", "titulo","operacion", "num1", "num2", "resultado"
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        for dato in historial:
            escritor.writerow(dato)

def cargar_historial_archivo():
    """
    Carga el historial de operaciones desde el archivo CSV.

    Verifica si el archivo `datos.csv` existe dentro de la carpeta `datos`.
    Si existe, lee cada fila como diccionario y la agrega a la lista global
    `historial`. Si el archivo no existe, la función no realiza ninguna acción.

    Esto evita errores si el historial aún no ha sido creado.
    """
    global historial
    ruta_base = os.path.dirname(__file__)
    carpeta_datos = os.path.join(ruta_base, "datos")
    os.makedirs(carpeta_datos, exist_ok=True)
    ruta_csv = os.path.join(ruta_base, "datos", "datos.csv")
    if not os.path.exists(ruta_csv):
        return
    try:
        with open(ruta_csv, mode="r", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            historial.clear()
            for fila in lector:
                historial.append(fila)

    except Exception as e:
        print(f"Error al cargar el historial: {e}")


# ============================================
# SECCIÓN 8: VALIDACIÓN (Estudiante 1)
# ============================================

def validar_numero(mensaje):
    """
    Solicita y valida un número flotante al usuario.
    """
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("❌ Error: Ingrese un número válido (ej: 10 o 10.5).")


def validar_numero_entero(mensaje):
    """
    Solicita y valida un número entero al usuario.
    """
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("❌ Error: Debe ingresar un número entero.")

# ============================================
# SECCIÓN 9: MENÚS (Estudiante 1)
# ============================================

def mostrar_menu_principal():
    print("\n" + "═" * 60)
    print("   CALCULADORA MULTIFUNCIONAL v2.0".center(60))
    print("═" * 60)
    print("1. Calculadora Básica (Aritmética)")
    print("2. Calculadora Científica (Trigonometría)")
    print("3. Conversor de Unidades de Datos (Bytes/GB)")
    print("4. Calculadora de Sistemas Numéricos (Bin/Hex)")
    print("5. Conversor de Temperatura (C/F/K)")
    print("6. Ver Historial")
    print("7. Limpiar Historial")
    print("8. Salir")
    print("-" * 60)


def menu_calculadora_basica():
    while True:
        print("\n--- 🧮 CALCULADORA BÁSICA ---")
        print("1. Sumar | 2. Restar | 3. Multiplicar | 4. Dividir")
        print("5. Módulo | 6. Potencia | 7. Volver")

        opc = input("\nSeleccione operación: ")
        if opc == "7": break

        if opc in ["1", "2", "3", "4", "5", "6"]:
            n1 = validar_numero("Primer número: ")
            n2 = validar_numero("Segundo número: ")

            if opc == "1":
                res = sumar(n1, n2)
            elif opc == "2":
                res = restar(n1, n2)
            elif opc == "3":
                res = multiplicar(n1, n2)
            elif opc == "4":
                res = dividir(n1, n2)
            elif opc == "5":
                res = modulo(n1, n2)
            elif opc == "6":
                res = potencia(n1, n2)

            if isinstance(res, str):  # Manejo de errores (división por cero)
                print(f"❌ {res}")
            else:
                print(f"✅ Resultado: {res[0]}")
                actualizar_historial(res)
        else:
            print("❌ Opción no válida.")


def menu_conversor_unidades():
    while True:
        print("\n--- 💾 CONVERSOR DE UNIDADES ---")
        print("1. B a KB   | 2. KB a MB  | 3. MB a GB")
        print("4. GB a MB  | 5. MB a KB  | 6. KB a B   | 7. Volver")

        opc = input("\nSeleccione opción: ")
        if opc == "7": break

        if opc in ["1", "2", "3", "4", "5", "6"]:
            val = validar_numero("Cantidad a convertir: ")
            if opc == "1":
                res = bytes_a_kilobytes(val)
            elif opc == "2":
                res = kilobytes_a_megabytes(val)
            elif opc == "3":
                res = megabytes_a_gigabytes(val)
            elif opc == "4":
                res = gigabytes_a_megabytes(val)
            elif opc == "5":
                res = megabytes_a_kilobytes(val)
            elif opc == "6":
                res = kilobytes_a_bytes(val)

            print(f"✅ Resultado: {res[0]}")
            actualizar_historial(res)


def menu_sistemas_numericos():
    while True:
        print("\n--- 🔢 SISTEMAS NUMÉRICOS ---")
        print("1. Decimal a Binario    | 2. Decimal a Hexadecimal")
        print("3. Binario a Decimal    | 4. Hexadecimal a Decimal")
        print("5. Volver")

        opc = input("\nSeleccione opción: ")
        if opc == "5": break

        if opc in ["1", "2"]:
            n = validar_numero_entero("Ingrese número decimal: ")
            res = decimal_a_binario(n) if opc == "1" else decimal_a_hexadecimal(n)
        elif opc == "3":
            n = input("Ingrese número binario: ")
            res = binario_a_decimal(n)
        elif opc == "4":
            n = input("Ingrese número hexadecimal: ")
            res = hexadecimal_a_decimal(n)
        else:
            continue

        if isinstance(res, str):
            print(f"❌ {res}")
        else:
            print(f"✅ Resultado: {res[0]}")
            actualizar_historial(res)


# ============================================
# PROGRAMA PRINCIPAL (MAIN)
# ============================================

def main():
    # Inicialización
    cargar_historial_archivo()

    while True:
        mostrar_menu_principal()
        opcion = input("\nSeleccione una opción (1-8): ")

        if opcion == "1":
            menu_calculadora_basica()
        elif opcion == "2":
            # Redirige al menú interno de la sección científica
            res = calculadora_cientifica()
            if res: actualizar_historial(res)
        elif opcion == "3":
            menu_conversor_unidades()
        elif opcion == "4":
            menu_sistemas_numericos()
        elif opcion == "5":
            # Redirige al menú interno de temperatura
            res = convertir_temperatura()
            if res: actualizar_historial(res)
        elif opcion == "6":
            mostrar_historial()
        elif opcion == "7":
            confirmar = input("¿Seguro que desea borrar todo? (s/n): ")
            if confirmar.lower() == 's':
                limpiar_historial()
                print("✅ Historial borrado.")
        elif opcion == "8":
            print("\n💾 Guardando datos...")
            guardar_historial_archivo()
            print("👋 ¡Gracias por usar la calculadora! Saliendo...")
            break
        else:
            print("❌ Opción inválida.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
