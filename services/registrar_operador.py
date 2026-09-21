from models.operador import Operador
from services.utilidades import leer_texto


def registrar_operador(lista_operadores, nombre=None, identificacion=None):
    lista = lista_operadores

    if nombre is None:
        nombre = leer_texto("Ingrese el nombre del operador: ")

    if identificacion is None:
        identificacion = leer_texto("Ingrese la identificación del operador: ")

    for registrado in lista:
        if registrado.get_identificacion() == identificacion:
            print("Ya existe un operador registrado con esa identificación.")
            return lista

    operador = Operador()
    operador.set_operador(nombre, identificacion)
    lista.append(operador)

    print("\nOperador registrado correctamente.")
    print(operador.get_datos())
    return lista

# lista = []
# lista = registrar_operador(lista, "Ana Gómez", "1090123456")
# print(len(lista))                        # 1
# print(lista[0].get_nombre())             # Ana Gómez
#
# # Segundo operador con identificación distinta: se agrega
# lista = registrar_operador(lista, "Luis Pérez", "1090999888")
# print(len(lista))                        # 2
#
# # Identificación repetida: no se agrega y avisa
# lista = registrar_operador(lista, "Otro Nombre", "1090123456")
# print(len(lista))                        # 2 (sin cambios)
