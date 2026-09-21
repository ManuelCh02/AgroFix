def asignar_maquina_operador(lista_maquinas, lista_operadores):
    maquinas = lista_maquinas
    operadores = lista_operadores

    for operador in operadores:
        print(f"{lista_operadores.index(operador) + 1}. {operador.get_datos()}\n")

        seleccion_operador = int(input("Ingrese el número de la lista de operadores al que desea asignarle máquina: "))

        operador_seleccionado = lista_operadores[seleccion_operador - 1]

        print ("Ingrese el número de la lista de máquinas que desea asignarle al operador")
        for maquina in maquinas:
            print(f"{lista_maquinas.index(maquina) + 1}. {maquina.get_ficha_tecnica()}\n")
        seleccion_maquina = int(input(":"))

        lista_maquinas[seleccion_maquina - 1].set_operador(operador_seleccionado)

        return [maquinas, operadores]