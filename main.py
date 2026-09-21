from models.maquina import Maquina
from services.registrar_maquina import registrar_maquina
from services.registrar_uso_maquina import registrar_uso_maquina
from services.registrar_operador import registrar_operador
from services.asignar_maquina_operador import asignar_maquina_operador
from services.registrar_falla import registrar_falla

NOMBRE_APP = "AgroFix"

REGISTRAR_MAQUINA = 1
REGISTRAR_USO_MAQUINA = 2
REGISTRAR_OPERADOR = 3
ASIGNAR_MAQUINA_OPERADOR = 4
LISTA_MAQUINAS = 5
REGISTRAR_FALLA = 6
SALIR = 9

lista_maquinas = []
lista_operadores = []

while True:
    print(f"======== Bienvenido a {NOMBRE_APP}!! ========")

    opcion = int(input("Selecciona una de las opciones:\n"
            "1. Registrar una maquína\n"
            "2. Registrar uso de una máquina\n"
            "3. Registrar operador\n"
            "4. Asignar máquina a operador\n"
            "5. Mostrar lista de máquinas\n"
            "6. Registrar una falla\n"
            "9. Salir\n"
            ))

    match opcion:
        case 1:
           maquina_registrada = registrar_maquina(Maquina())
           lista_maquinas.append(maquina_registrada)
           for maquina in lista_maquinas:
                print(maquina.get_ficha_tecnica())
        case 2:
            maquina_buscar = input(
                "Ingrese el serial o modelo al cual quiere registrar las horas de uso: "
            )

            horas_uso = float(
                input("Ingrese el número de horas que se usó la máquina: ")
            )

            lista_modificada = registrar_uso_maquina(lista_maquinas, maquina_buscar, horas_uso)
            lista_maquinas = lista_modificada
        case 3:
            nombre_operador = input("Ingrese el nombre del operador: ")
            identificacion_operador = input("Ingrese la identificación del operador: ")

            nueva_lista_operadores = registrar_operador(lista_operadores, nombre_operador, identificacion_operador)
            lista_operadores = nueva_lista_operadores

            for operador in lista_operadores:
                print(operador.get_datos())
        case 4: 
            print("----- Seleccione el operador al que desea asignar la máquina -----")
            
            nuevas_maquinas, nuevos_operadores = asignar_maquina_operador(lista_maquinas, lista_operadores)
            lista_maquinas = nuevas_maquinas
            lista_operadores = nuevos_operadores
        case 5:
            for maquina in lista_maquinas:
                print(f"{maquina.get_ficha_tecnica()}\n")
        case 6:
            print("----- Registrar una falla presentada -----")

            nueva_falla = registrar_falla(lista_maquinas)
            lista_maquinas = nueva_falla
        case 9:
            break
    