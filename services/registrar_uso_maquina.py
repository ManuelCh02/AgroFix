from datetime import date

from models.registroUso import RegistroUso

def registrar_uso_maquina(lista_maquinas, maquina_buscar, horas_uso):
    fecha_actual = date.today()

    registro_uso = RegistroUso()
    registro_uso.set_registro_uso(fecha_actual, horas_uso)


    encontrada = False
    lista = lista_maquinas

    for maquina in lista:
        if maquina.modelo == maquina_buscar or maquina.serial == maquina_buscar:
            maquina.registrar_uso(horas_uso)
            encontrada = True
            print("Horas registradas correctamente.")
            print(maquina.get_ficha_tecnica())
            return lista
            break

    if not encontrada:
        print("No se encontró una máquina con ese modelo.")

