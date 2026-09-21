from services.utilidades import describir_maquina, describir_operador, seleccionar_de_lista


def asignar_maquina_operador(lista_maquinas, lista_operadores):
    maquinas = lista_maquinas
    operadores = lista_operadores

    if not maquinas:
        print("No hay máquinas registradas. Registre una máquina primero.")
        return maquinas, operadores

    if not operadores:
        print("No hay operadores registrados. Registre un operador primero.")
        return maquinas, operadores

    operador = seleccionar_de_lista(
        "Seleccione el operador al que desea asignar la máquina:",
        operadores,
        describir_operador,
    )
    if operador is None:
        return maquinas, operadores

    maquina = seleccionar_de_lista(
        "Seleccione la máquina que desea asignar al operador:",
        maquinas,
        describir_maquina,
    )
    if maquina is None:
        return maquinas, operadores

    operador_anterior = maquina.get_operador()
    if operador_anterior is not None and operador_anterior is not operador:
        operador_anterior.set_maquina_asignada(None)
        print(f"La máquina estaba asignada a {operador_anterior.get_nombre()} "
              f"y fue liberada.")

    maquina.set_operador(operador)
    operador.set_maquina_asignada(maquina)

    print("\nAsignación realizada correctamente.")
    print(operador.get_datos())

    return maquinas, operadores


# Prueba manual desde el menú (opción 4):
#
# Sin máquinas registradas:
# Resultado esperado: "No hay máquinas registradas..." y las listas regresan intactas
#                     (antes el for vacío hacía que la función retornara None).
#
# Con 1 operador y 1 máquina, seleccionando 1 y 1:
# Resultado esperado: la ficha de la máquina muestra el operador y los datos del
#                     operador muestran la máquina (relación en los dos sentidos).
#
# Reasignar la misma máquina a un segundo operador:
# Resultado esperado: "La máquina estaba asignada a <nombre> y fue liberada."
#                     y el primer operador queda con "Máquina asignada: Sin asignar".
#
# from models.maquina import Maquina
# from models.operador import Operador
# tractor = Maquina(); tractor.set_modelo("Maquina 5055E")
# tractor.set_numero_serie("JD-2024-001"); tractor.set_tipo("Tractor")
# ana = Operador(); ana.set_operador("Ana Gómez", "1090123456")
# maquinas, operadores = asignar_maquina_operador([tractor], [ana])  # elegir 1 y 1
# print(tractor.get_operador().get_nombre())            # Ana Gómez
# print(ana.get_maquina_asignada().get_modelo())        # Maquina 5055E
