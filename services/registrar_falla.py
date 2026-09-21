from models.falla import Falla
from services.registrar_maquina import ESTADOS_MAQUINA
from services.utilidades import (
    describir_maquina,
    leer_fecha,
    leer_texto,
    seleccionar_de_lista,
    seleccionar_opcion,
)


def registrar_falla(lista_maquinas):
    maquinas = lista_maquinas

    if not maquinas:
        print("No hay máquinas registradas. Registre una máquina primero.")
        return maquinas

    maquina = seleccionar_de_lista(
        "Seleccione la máquina que presenta la falla:",
        maquinas,
        describir_maquina,
    )
    if maquina is None:
        return maquinas

    inicio_falla = leer_fecha("Registre la fecha en que inició la falla (DD-MM-AAAA): ")
    causa_falla = leer_texto("Registre la causa de la falla: ")
    gravedad_falla = seleccionar_opcion("Seleccione la gravedad de la falla:", Falla.GRAVEDADES)
    estado_maquina = seleccionar_opcion(
        "Seleccione el estado en que queda la máquina:", ESTADOS_MAQUINA
    )

    falla = Falla()
    falla.set_falla(inicio_falla, causa_falla, gravedad_falla, "Abierta", maquina)

    maquina.set_falla(falla)
    maquina.set_estado(estado_maquina)

    print("\nFalla registrada correctamente.")
    print(falla.get_detalle())

    return maquinas

# Prueba manual desde el menú (opción 6):
#
# Sin máquinas registradas:
# Resultado esperado: "No hay máquinas registradas..." y la lista regresa intacta.
#
# Con una máquina, fecha "01-09-2026", causa "Fuga de aceite",
# gravedad 1 (Alta), estado 4 (Malo):
# Resultado esperado: la falla queda en maquina.get_fallas() y el estado de la
#                     máquina cambia a "Malo" en su ficha técnica.
#
# Fecha "2026-09-01":
# Resultado esperado: "Formato de fecha inválido. Use DD-MM-AAAA" y pide de nuevo.
#
# from models.maquina import Maquina
# tractor = Maquina(); tractor.set_tipo("Tractor")
# tractor.set_modelo("Maquina 5055E"); tractor.set_numero_serie("JD-2024-001")
# tractor.set_estado("Bueno")
# registrar_falla([tractor])
# print(len(tractor.get_fallas()))     # 1
# print(tractor.get_estado())          # Malo
# print(len(tractor.fallas_abiertas()))# 1
