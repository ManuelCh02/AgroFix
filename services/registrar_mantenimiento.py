from models.mantenimiento import Mantenimiento
from services.registrar_maquina import ESTADOS_MAQUINA
from services.utilidades import (
    describir_maquina,
    describir_repuesto,
    leer_decimal,
    leer_entero,
    leer_fecha,
    leer_texto,
    seleccionar_de_lista,
    seleccionar_opcion,
)


def registrar_mantenimiento(lista_maquinas, lista_repuestos):
    maquinas = lista_maquinas
    repuestos = lista_repuestos

    if not maquinas:
        print("No hay máquinas registradas. Registre una máquina primero.")
        return maquinas, repuestos

    maquina = seleccionar_de_lista(
        "Seleccione la máquina a la que se le hizo el mantenimiento:",
        maquinas,
        describir_maquina,
    )
    if maquina is None:
        return maquinas, repuestos

    tipo = seleccionar_opcion("Seleccione el tipo de mantenimiento:", Mantenimiento.TIPOS)
    fecha = leer_fecha("Ingrese la fecha del mantenimiento (DD-MM-AAAA): ")
    descripcion = leer_texto("Ingrese la descripción del trabajo realizado: ")
    costo_mano_obra = leer_decimal("Ingrese el costo de la mano de obra: ", 0)

    mantenimiento = Mantenimiento()
    mantenimiento.set_mantenimiento(tipo, fecha, descripcion, costo_mano_obra, maquina)

    if repuestos:
        while True:
            continuar = leer_entero("¿Usó repuestos? (1. Sí / 2. No): ", 1, 2)
            if continuar == 2:
                break

            repuesto = seleccionar_de_lista(
                "Seleccione el repuesto utilizado:", repuestos, describir_repuesto
            )
            if repuesto is None:
                break

            cantidad = leer_entero("Ingrese la cantidad utilizada: ", 1)
            if mantenimiento.agregar_repuesto(repuesto, cantidad):
                print(f"Repuesto agregado. Stock restante: {repuesto.get_stock()}")
            else:
                print(f"Stock insuficiente. Solo hay {repuesto.get_stock()} unidad(es).")
    else:
        print("No hay repuestos en inventario, el mantenimiento solo incluirá mano de obra.")

    maquina.set_mantenimiento(mantenimiento)

    nuevo_estado = seleccionar_opcion(
        "Seleccione el estado en que queda la máquina:", ESTADOS_MAQUINA
    )
    maquina.set_estado(nuevo_estado)

    print("\nMantenimiento registrado correctamente.")
    print(mantenimiento.get_mantenimiento())

    return maquinas, repuestos

# Prueba manual desde el menú (opción 9):
#
# Sin máquinas registradas:
# Resultado esperado: "No hay máquinas registradas..." y las listas regresan intactas.
#
# Máquina 1, tipo 1 (Preventivo), fecha "18-09-2026",
# descripción "Cambio de aceite", mano de obra 80000,
# repuestos: Sí -> Filtro de aceite x2 (stock 5, costo 45000):
# Resultado esperado: "Stock restante: 3", costo repuestos $90000
#                     y costo total $170000.
#
# Repetir pidiendo 99 unidades del mismo repuesto:
# Resultado esperado: "Stock insuficiente. Solo hay 3 unidad(es)."
#                     y el costo total no cambia.
#
# from models.maquina import Maquina
# from models.repuesto import Repuesto
# tractor = Maquina(); tractor.set_tipo("Tractor")
# tractor.set_modelo("Maquina 5055E"); tractor.set_numero_serie("JD-2024-001")
# filtro = Repuesto(); filtro.set_repuesto("Filtro de aceite", "FIL-001", 5, 45000.0)
# registrar_mantenimiento([tractor], [filtro])
# print(len(tractor.get_historial_de_mantenimiento()))  # 1
# print(tractor.costo_total())                          # 170000.0
# print(filtro.get_stock())                             # 3
