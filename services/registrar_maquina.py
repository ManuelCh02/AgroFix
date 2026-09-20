ESTADOS_MAQUINA = ["Excelente", "Bueno", "Regular", "Malo"]

def registrar_maquina(instancia):
    maquina = instancia
    modelo = input("Ingrese el modelo de la máquina: ")
    maquina.set_modelo(modelo)

    serie = input("Ingrese el número de serie: ")
    maquina.set_numero_serie(serie)
    while True: 
        opcion_estado = int(input("Ingrese el estado de la máquina de acuerdo a una de las siguientes opciones:\n"
                "1. Excelente\n"
                "2. Bueno\n"
                "3. Regular\n"
                "4. Malo\n"
                ))

        match opcion_estado:
            case 1:
                maquina.set_estado(ESTADOS_MAQUINA[0])
                break
            case 2:
                maquina.set_estado(ESTADOS_MAQUINA[1])
                break
            case 3:
                maquina.set_estado(ESTADOS_MAQUINA[2])
                break
            case 4:
                maquina.set_estado(ESTADOS_MAQUINA[3])
                break
            case _:
                print("Selección inválida, vuelva a intentar")
                continue
    return maquina