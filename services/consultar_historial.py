from services.utilidades import describir_maquina, seleccionar_de_lista


def consultar_historial(lista_maquinas):
    maquinas = lista_maquinas

    if not maquinas:
        print("No hay máquinas registradas.")
        return maquinas

    maquina = seleccionar_de_lista(
        "Seleccione la máquina que desea consultar:", maquinas, describir_maquina
    )
    if maquina is None:
        return maquinas

    print("\n===== FICHA TÉCNICA =====")
    print(maquina.get_ficha_tecnica())

    print("\n===== HISTORIAL DE USO =====")
    if maquina.get_historial_de_uso():
        for registro in maquina.get_historial_de_uso():
            print(f"- {registro.get_registro_uso()}")
    else:
        print("Sin registros de uso.")

    print("\n===== HISTORIAL DE MANTENIMIENTO =====")
    if maquina.get_historial_de_mantenimiento():
        for mantenimiento in maquina.get_historial_de_mantenimiento():
            print(mantenimiento.get_mantenimiento())
            print("-" * 40)
    else:
        print("Sin mantenimientos registrados.")

    print("\n===== HISTORIAL DE FALLAS =====")
    if maquina.get_fallas():
        for falla in maquina.get_fallas():
            print(falla.get_detalle())
            print("-" * 40)
    else:
        print("Sin fallas registradas.")

    return maquinas

# Prueba manual desde el menú (opción 13):
#
# Sin máquinas registradas:
# Resultado esperado: "No hay máquinas registradas."
#
# Con una máquina sin movimientos:
# Resultado esperado: "Sin registros de uso.", "Sin mantenimientos registrados."
#                     y "Sin fallas registradas."
#
# Con una máquina que tiene uso, mantenimiento y falla:
# Resultado esperado: se listan las tres secciones con sus detalles.
