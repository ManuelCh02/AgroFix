from services.registrar_maquina import ESTADOS_MAQUINA
from services.utilidades import (
    describir_falla,
    describir_maquina,
    leer_fecha,
    seleccionar_de_lista,
    seleccionar_opcion,
)


def resolver_falla(lista_maquinas):
    maquinas = lista_maquinas

    maquinas_con_fallas = [maquina for maquina in maquinas if maquina.fallas_abiertas()]
    if not maquinas_con_fallas:
        print("No hay fallas pendientes por resolver.")
        return maquinas

    maquina = seleccionar_de_lista(
        "Seleccione la máquina cuya falla va a resolver:",
        maquinas_con_fallas,
        describir_maquina,
    )
    if maquina is None:
        return maquinas

    falla = seleccionar_de_lista(
        "Seleccione la falla que va a resolver:",
        maquina.fallas_abiertas(),
        describir_falla,
    )
    if falla is None:
        return maquinas

    fecha_resolucion = leer_fecha("Ingrese la fecha de resolución (DD-MM-AAAA): ")
    falla.resolver(fecha_resolucion)

    nuevo_estado = seleccionar_opcion(
        "Seleccione el estado en que queda la máquina:", ESTADOS_MAQUINA
    )
    maquina.set_estado(nuevo_estado)

    duracion = falla.get_duracion()
    print("\nFalla resuelta correctamente.")
    if duracion is not None:
        print(f"La máquina estuvo detenida {duracion} día(s).")
    print(falla.get_detalle())

    return maquinas

# Prueba manual desde el menú (opción 7):
#
# Sin fallas abiertas:
# Resultado esperado: "No hay fallas pendientes por resolver."
#
# Con una falla iniciada el "01-09-2026" y resolución "06-09-2026":
# Resultado esperado: "La máquina estuvo detenida 5 día(s)", la falla pasa a
#                     [Resuelta] y desaparece de maquina.fallas_abiertas().
#
# from models.maquina import Maquina
# from models.falla import Falla
# tractor = Maquina(); tractor.set_tipo("Tractor")
# tractor.set_modelo("John Deere 5055E"); tractor.set_numero_serie("JD-2024-001")
# falla = Falla()
# falla.set_falla("01-09-2026", "Fuga de aceite", "Alta", "Malo", tractor)
# tractor.set_falla(falla)
# resolver_falla([tractor])            # elegir 1, 1, fecha 06-09-2026, estado 2
# print(falla.esta_resuelta())         # True
# print(falla.get_duracion())          # 5
# print(len(tractor.fallas_abiertas()))# 0
# print(tractor.tiempo_detenida())     # 5
