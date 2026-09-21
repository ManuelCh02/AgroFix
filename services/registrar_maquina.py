from services.utilidades import leer_texto, seleccionar_opcion

TIPOS_MAQUINA = ["Tractor", "Cosechadora", "Fumigadora", "Motobomba", "Guadañadora", "Otro"]
ESTADOS_MAQUINA = ["Excelente", "Bueno", "Regular", "Malo"]


def registrar_maquina(instancia, lista_maquinas):
    maquina = instancia
    lista = lista_maquinas

    tipo = seleccionar_opcion("Seleccione el tipo de máquina:", TIPOS_MAQUINA)
    if tipo == "Otro":
        tipo = leer_texto("Escriba el tipo de máquina: ")
    maquina.set_tipo(tipo)

    modelo = leer_texto("Ingrese el modelo de la máquina: ")
    maquina.set_modelo(modelo)

    while True:
        serie = leer_texto("Ingrese el número de serie: ")
        if any(registrada.get_numero_serie() == serie for registrada in lista):
            print("Ya existe una máquina registrada con ese número de serie.")
            continue
        maquina.set_numero_serie(serie)
        break

    estado = seleccionar_opcion("Seleccione el estado de la máquina:", ESTADOS_MAQUINA)
    maquina.set_estado(estado)

    lista.append(maquina)
    print("\nMáquina registrada correctamente.")
    print(maquina.get_ficha_tecnica())
    return lista

# Prueba manual desde el menú (opción 1):
#
# Entradas: tipo 1 (Tractor), modelo "Maquina 5055E",
#           serie "JD-2024-001", estado 2 (Bueno)
# Resultado esperado: la lista queda con 1 máquina y se imprime su ficha técnica.
#
# Repetir la opción 1 con la misma serie "JD-2024-001":
# Resultado esperado: "Ya existe una máquina registrada con ese número de serie."
#                     y vuelve a pedir la serie sin duplicar el registro.
#
# Entrada de tipo "9" (fuera del menú):
# Resultado esperado: "El valor debe ser menor o igual a 6." y pide de nuevo.
#
# from models.maquina import Maquina
# lista = []
# lista = registrar_maquina(Maquina(), lista)
# print(len(lista))                          # 1
# print(lista[0].get_numero_serie())         # JD-2024-001
