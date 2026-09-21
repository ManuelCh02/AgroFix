from datetime import date

from models.registroUso import RegistroUso
from services.utilidades import (
    describir_maquina,
    leer_decimal,
    leer_texto,
    seleccionar_de_lista,
)


def registrar_uso_maquina(lista_maquinas):
    lista = lista_maquinas

    if not lista:
        print("No hay máquinas registradas. Registre una máquina primero.")
        return lista

    maquina = seleccionar_de_lista(
        "Seleccione la máquina a la que va a registrar horas de uso:",
        lista,
        describir_maquina,
    )
    if maquina is None:
        return lista

    horas_uso = leer_decimal("Ingrese el número de horas que se usó la máquina: ", 0)
    observaciones = leer_texto("Ingrese una observación de la jornada: ")
    fecha_actual = date.today().strftime("%d-%m-%Y")

    operador = maquina.get_operador()

    registro_uso = RegistroUso()
    registro_uso.set_registro_uso(fecha_actual, horas_uso, operador, observaciones)

    maquina.registrar_uso(registro_uso)
    if operador is not None:
        operador.set_registro_uso(registro_uso)

    print("\nHoras registradas correctamente.")
    print(maquina.get_ficha_tecnica())

    if maquina.requiere_mantenimiento():
        print(f"\nALERTA: faltan {maquina.proximo_mantenimiento()} horas "
              f"para el mantenimiento preventivo de esta máquina.")

    return lista

# Prueba manual desde el menú (opción 2):
#
# Con la lista vacía:
# Resultado esperado: "No hay máquinas registradas. Registre una máquina primero."
#                     y NO se pierde la lista (antes retornaba None y borraba todo).
#
# Con una máquina registrada y entrada de horas "240":
# Resultado esperado: horas de uso 240.0 en la ficha técnica y la alerta
#                     "faltan 10.0 horas para el mantenimiento preventivo".
#
# Entrada de horas "ocho":
# Resultado esperado: "Debe ingresar un número, vuelva a intentar."
#
# from models.maquina import Maquina
# tractor = Maquina(); tractor.set_tipo("Tractor")
# tractor.set_modelo("Maquina 5055E"); tractor.set_numero_serie("JD-2024-001")
# tractor.set_estado("Bueno")
# lista = registrar_uso_maquina([tractor])   # seleccionar 1, horas 6, observación "Arado"
# print(tractor.get_horas_uso_total())       # 6.0
# print(len(tractor.get_historial_de_uso())) # 1
# print(lista is not None)                   # True
