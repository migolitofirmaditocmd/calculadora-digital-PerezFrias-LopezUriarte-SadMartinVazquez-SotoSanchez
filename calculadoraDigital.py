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
        a (float): Primer número
        b (float): Segundo número

    Returns:
        float: Resultado de la suma
    """
    return a + b


def restar(a, b):
    """
    Resta dos números.

    Args:
        a (float): Primer número
        b (float): Segundo número

    Returns:
        float: Resultado de la resta
    """
    # TODO: Implementar
    pass


def multiplicar(a, b):
    """
    Multiplica dos números.

    Args:
        a (float): Primer número
        b (float): Segundo número

    Returns:
        float: Resultado de la multiplicación
    """
    # TODO: Implementar
    pass


def dividir(a, b):
    """
    Divide dos números.

    Args:
        a (float): Dividendo
        b (float): Divisor

    Returns:
        float: Resultado de la división
        None: Si b es cero

    Raises:
        None: Retorna None en lugar de lanzar excepción
    """
    # TODO: Implementar
    # Verificar que b no sea cero
    # Si b == 0, retornar None
    # Si no, retornar a / b
    pass


def modulo(a, b):
    """
    Calcula el módulo (residuo) de dos números.

    Args:
        a (float): Dividendo
        b (float): Divisor

    Returns:
        float: Residuo de la división
    """
    # TODO: Implementar
    pass


def potencia(a, b):
    """
    Calcula a elevado a la potencia b.

    Args:
        a (float): Base
        b (float): Exponente

    Returns:
        float: Resultado de a^b
    """
    # TODO: Implementar
    pass


# ============================================
# SECCIÓN 2: CONVERSIÓN DE SISTEMAS NUMÉRICOS (Estudiante 2)
# ============================================

def decimal_a_binario(numero):
    """
    Convierte un número decimal a binario usando algoritmo manual.

    Args:
        numero (int): Número decimal

    Returns:
        str: Representación binaria como string
    """
    # TODO: Implementar algoritmo de división sucesiva
    # Algoritmo:
    # 1. Crear string vacío para resultado
    # 2. Mientras numero > 0:
    #    - residuo = numero % 2
    #    - agregar residuo al inicio del string
    #    - numero = numero // 2
    # 3. Retornar el string
    # Caso especial: .gitkeep numero == 0, retornar "0"
    pass


def decimal_a_hexadecimal(numero):
    """
    Convierte un número decimal a hexadecimal.

    Args:
        numero (int): Número decimal

    Returns:
        str: Representación hexadecimal como string
    """
    # TODO: Implementar
    # Pueden usar el método similar a binario
    # Recordar: 10=A, 11=B, 12=C, 13=D, 14=E, 15=F
    pass


def binario_a_decimal(binario):
    """
    Convierte un número binario (string) a decimal.

    Args:
        binario (str): Número binario como string

    Returns:
        int: Número decimal
    """
    # TODO: Implementar
    # Algoritmo:
    # 1. Inicializar decimal = 0
    # 2. Para cada dígito en binario (de derecha a izquierda):
    #    - decimal += dígito * (2 ^ posición)
    # 3. Retornar decimal
    pass


def hexadecimal_a_decimal(hexadecimal):
    """
    Convierte un número hexadecimal (string) a decimal.

    Args:
        hexadecimal (str): Número hexadecimal como string

    Returns:
        int: Número decimal
    """
    # TODO: Implementar
    pass


# ============================================
# SECCIÓN 3: CONVERSIÓN DE UNIDADES (COMPLETADO)
# ============================================

def bytes_a_kilobytes(bytes_val):
    """
    Convierte bytes a kilobytes.

    Args:
        bytes_val (float): Cantidad en bytes

    Returns:
        float: Cantidad en kilobytes
    """
    return bytes_val / 1024


def kilobytes_a_megabytes(kilobytes):
    """
    Convierte kilobytes a megabytes.

    Args:
        kb (float): Cantidad en kilobytes

    Returns:
        float: Cantidad en megabytes
    """
    # TODO: Implementar (1 MB = 1024 KB)
    return kb / 1024


def megabytes_a_gigabytes(megabytes):
    """
    Convierte megabytes a gigabytes.

    Args:
        mb (float): Cantidad en megabytes

    Returns:
        float: Cantidad en gigabytes
    """
    # TODO: Implementar
    return mb / 1024

def gigabytes_a_megabytes(gigabytes):
    """
    Convierte gigabytes a megabytes.

    Args:
        gb (float): Cantidad en gigabytes

    Returns:
        float: Cantidad en megabytes
    """
    return gb * 1024

def megabytes_a_kilobytes(megabytes):
    """
    Convierte megabytes a kilobytes.

    Args:
        mb (float): Cantidad en megabytes

    Returns:
        float: Cantidad en kilobytes
    """
    return mb * 1024

def kilobytes_a_bytes(kilobytes):
    """
    Convierte kilobytes a bytes.

    Args:
        kb (float): Cantidad en kilobytes

    Returns:
        float: Cantidad en bytes
    """
    return kb * 1024


# TODO: Implementar las funciones inversas
# gigabytes_a_megabytes(), megabytes_a_kilobytes(), kilobytes_a_bytes()


# ============================================
# SECCIÓN 4: GESTIÓN DE HISTORIAL (Estudiante 3)
# ============================================

def agregar_al_historial(operacion, num1, num2, resultado):
    """
    Agrega una operación al historial.

    Args:
        operacion (str): Tipo de operación (ej: "Suma", "División")
        num1 (float): Primer número
        num2 (float): Segundo número
        resultado (float): Resultado de la operación
    """
    global historial

    # TODO: Implementar
    # 1. Crear string con formato: "operación: num1 op num2 = resultado"
    # 2. Agregar al final de la lista historial
    # 3. Si historial tiene más de 10 elementos, eliminar el primero

    # Ejemplo de formato:
    # fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # entrada = f"{fecha_hora} | {operacion}: {num1} + {num2} = {resultado}"
    # historial.append(entrada)

    pass


def mostrar_historial():
    """
    Muestra el historial de operaciones.
    """
    global historial

    # TODO: Implementar
    # 1. Verificar .gitkeep historial está vacío
    # 2. Si está vacío, mostrar mensaje
    # 3. Si no, iterar sobre historial y mostrar cada operación numerada

    pass


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
# SECCIÓN 5: GESTIÓN DE ARCHIVOS (COMPLETADO)
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
    with open(ruta_csv,mode="r",encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            historial.append(fila)


# ============================================
# SECCIÓN 6: VALIDACIÓN (Estudiante 1)
# ============================================

def validar_numero(mensaje):
    """
    Solicita y valida un número al usuario.

    Args:
        mensaje (str): Mensaje a mostrar

    Returns:
        float: Número validado
    """
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("❌ Error: Ingrese un número válido.")


def validar_numero_entero(mensaje):
    """
    Solicita y valida un número entero al usuario.

    Args:
        mensaje (str): Mensaje a mostrar

    Returns:
        int: Número entero validado
    """
    # TODO: Implementar similar a validar_numero
    # pero convirtiendo a int en lugar de float
    pass


# ============================================
# SECCIÓN 7: MENÚS (Estudiante 1)
# ============================================

def mostrar_menu_principal():
    """Muestra el menú principal"""
    print("\n" + "="*60)
    print("   CALCULADORA MULTIFUNCIONAL v2.0")
    print("="*60)
    print("\nMENÚ PRINCIPAL:")
    print("1. Calculadora Básica")
    print("2. Conversor de Unidades de Datos")
    print("3. Calculadora de Sistemas Numéricos")
    print("4. Ver Historial")
    print("5. Limpiar Historial")
    print("6. Salir")
    print("-"*60)


def menu_calculadora_basica():
    """Menú y lógica de la calculadora básica"""
    print("\n--- CALCULADORA BÁSICA ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Módulo (residuo)")
    print("6. Potencia")
    print("7. Volver al menú principal")

    opcion = input("\nSeleccione operación: ")

    if opcion == "7":
        return

    # Solicitar números
    num1 = validar_numero("Ingrese el primer número: ")
    num2 = validar_numero("Ingrese el segundo número: ")

    # TODO: Implementar lógica según opción
    # - Si opcion == "1": resultado = sumar(num1, num2)
    # - Si opcion == "2": resultado = restar(num1, num2)
    # - etc.
    # - Mostrar resultado
    # - Llamar a agregar_al_historial()

    pass


def menu_conversor_unidades():
    """Menú y lógica del conversor de unidades"""
    # TODO: Implementar
    pass


def menu_sistemas_numericos():
    """Menú y lógica de conversión de sistemas numéricos"""
    # TODO: Implementar
    pass


# ============================================
# PROGRAMA PRINCIPAL
# ============================================

def main():
    """Función principal del programa"""

    print("╔" + "═"*58 + "╗")
    print("║" + " "*58 + "║")
    print("║" + "  CALCULADORA MULTIFUNCIONAL - Versión Avanzada".center(58) + "║")
    print("║" + " "*58 + "║")
    print("║" + "  Con historial, funciones y persistencia de datos".center(58) + "║")
    print("║" + " "*58 + "║")
    print("╚" + "═"*58 + "╝")

    # Cargar historial al iniciar
    cargar_historial_archivo()
    print("\n✅ Historial cargado desde archivo.")

    continuar = True

    while continuar:
        mostrar_menu_principal()

        opcion = input("\nSeleccione una opción (1-6): ")

        if opcion == "1":
            menu_calculadora_basica()

        elif opcion == "2":
            menu_conversor_unidades()

        elif opcion == "3":
            menu_sistemas_numericos()

        elif opcion == "4":
            mostrar_historial()

        elif opcion == "5":
            confirmacion = input("\n¿Está seguro de limpiar el historial? (s/n): ")
            if confirmacion.lower() == "s":
                limpiar_historial()
                print("✅ Historial limpiado.")

        elif opcion == "6":
            print("\n💾 Guardando historial...")
            guardar_historial_archivo()
            print("✅ Historial guardado en datos/historial.txt")
            print("\n¡Gracias por usar la Calculadora Multifuncional!")
            print("¡Hasta pronto! 👋")
            continuar = False

        else:
            print("\n❌ Opción inválida. Por favor seleccione 1-6.")

    print("\nPrograma terminado.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
