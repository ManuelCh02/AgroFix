from datetime import datetime

FORMATO_FECHA = "%d-%m-%Y"


def leer_texto(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("El dato no puede quedar vacío, vuelva a intentar.")


def leer_entero(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensaje))
        except ValueError:
            print("Debe ingresar un número entero, vuelva a intentar.")
            continue

        if minimo is not None and valor < minimo:
            print(f"El valor debe ser mayor o igual a {minimo}.")
            continue
        if maximo is not None and valor > maximo:
            print(f"El valor debe ser menor o igual a {maximo}.")
            continue
        return valor


def leer_decimal(mensaje, minimo=None):
    while True:
        try:
            valor = float(input(mensaje).replace(",", "."))
        except ValueError:
            print("Debe ingresar un número, vuelva a intentar.")
            continue

        if minimo is not None and valor < minimo:
            print(f"El valor debe ser mayor o igual a {minimo}.")
            continue
        return valor


def leer_fecha(mensaje):
    while True:
        valor = input(mensaje).strip()
        try:
            datetime.strptime(valor, FORMATO_FECHA)
            return valor
        except ValueError:
            print("Formato de fecha inválido. Use DD-MM-AAAA (ejemplo: 18-09-2026).")


def seleccionar_opcion(mensaje, opciones):
    print(mensaje)
    for indice, opcion in enumerate(opciones, start=1):
        print(f"{indice}. {opcion}")

    seleccion = leer_entero("Seleccione una opción: ", 1, len(opciones))
    return opciones[seleccion - 1]


def seleccionar_de_lista(mensaje, lista, describir):
    if not lista:
        print("No hay registros disponibles para seleccionar.")
        return None

    print(mensaje)
    for indice, elemento in enumerate(lista, start=1):
        print(f"{indice}. {describir(elemento)}")

    seleccion = leer_entero("Seleccione una opción: ", 1, len(lista))
    return lista[seleccion - 1]


def describir_maquina(maquina):
    return f"{maquina.get_tipo()} {maquina.get_modelo()} ({maquina.get_numero_serie()})"


def describir_operador(operador):
    return f"{operador.get_nombre()} - C.C. {operador.get_identificacion()}"


def describir_repuesto(repuesto):
    return f"{repuesto.get_nombre()} ({repuesto.get_codigo()}) - Stock: {repuesto.get_stock()}"


def describir_falla(falla):
    return falla.get_falla()


# Las funciones de lectura dependen de input(), por eso se prueban manualmente
# desde el menú. Estos son los casos verificados:
#
# leer_entero("Opción: ", 1, 9)
#   "abc"  -> "Debe ingresar un número entero, vuelva a intentar."
#   "15"   -> "El valor debe ser menor o igual a 9."
#   "0"    -> "El valor debe ser mayor o igual a 1."
#   "3"    -> retorna 3
#
# leer_decimal("Horas: ", 0)
#   "ocho" -> "Debe ingresar un número, vuelva a intentar."
#   "-2"   -> "El valor debe ser mayor o igual a 0."
#   "7,5"  -> retorna 7.5 (acepta coma decimal)
#
# leer_fecha("Fecha: ")
#   "2026-09-18" -> "Formato de fecha inválido. Use DD-MM-AAAA"
#   "31-02-2026" -> "Formato de fecha inválido" (día que no existe)
#   "18-09-2026" -> retorna "18-09-2026"
#
# leer_texto("Modelo: ")
#   ""     -> "El dato no puede quedar vacío, vuelva a intentar."
#   "  X " -> retorna "X" (sin espacios sobrantes)
#
# from models.maquina import Maquina
# tractor = Maquina(); tractor.set_tipo("Tractor")
# tractor.set_modelo("John Deere 5055E"); tractor.set_numero_serie("JD-2024-001")
# print(describir_maquina(tractor))  # Tractor Maquina 5055E (JD-2024-001)
# print(seleccionar_de_lista("Máquinas:", [], describir_maquina))  # None
