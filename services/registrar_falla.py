from models.falla import Falla

def registrar_falla(lista_maquinas):
    falla = Falla()
    maquinas = lista_maquinas

    inicio_falla = input("Registre la fecha en que inició la falla (DD-MM-AAAA): ")
    causa_falla = input("Registre la causa de la falla: ")
    gravedad_falla = input("Registre la gravedad de la falla (Alta, Media, Baja): ")
    estado_maquina = input("Registre el estado de la máquina: ")

    obtener_maquina_falla = input("Ingrese el serial o modelo de la máquina que presenta la falla: ")
    for maquina in maquinas:
        if maquina.modelo == obtener_maquina_falla or maquina.numero_serie == obtener_maquina_falla:
            falla.set_falla(inicio_falla, causa_falla, gravedad_falla, estado_maquina, maquina)
            maquina.set_falla(falla)

    return maquinas
    

