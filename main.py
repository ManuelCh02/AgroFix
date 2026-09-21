from models.finca import Finca
from models.gestorMaquinaria import GestorMaquinaria
from models.maquina import Maquina
from services.asignar_maquina_operador import asignar_maquina_operador
from services.consultar_historial import consultar_historial
from services.registrar_falla import registrar_falla
from services.registrar_finca import registrar_finca
from services.registrar_mantenimiento import registrar_mantenimiento
from services.registrar_maquina import registrar_maquina
from services.registrar_operador import registrar_operador
from services.registrar_repuesto import actualizar_repuesto, registrar_repuesto
from services.registrar_uso_maquina import registrar_uso_maquina
from services.resolver_falla import resolver_falla
from services.utilidades import leer_entero

NOMBRE_APP = "AgroFix"

REGISTRAR_MAQUINA = 1
REGISTRAR_USO_MAQUINA = 2
REGISTRAR_OPERADOR = 3
ASIGNAR_MAQUINA_OPERADOR = 4
REGISTRAR_FALLA = 5
RESOLVER_FALLA = 6
REGISTRAR_MANTENIMIENTO = 7
REGISTRAR_REPUESTO = 8
ACTUALIZAR_REPUESTO = 9
LISTA_MAQUINAS = 10
LISTA_OPERADORES = 11
LISTA_REPUESTOS = 12
CONSULTAR_HISTORIAL = 13
REPORTE_COSTOS = 14
MAQUINAS_POR_REVISAR = 15
DATOS_FINCA = 16
SALIR = 0

lista_maquinas = []
lista_operadores = []
lista_repuestos = []

finca = Finca()
gestor = GestorMaquinaria()


def mostrar_menu():
    print(f"\n======== Bienvenido a {NOMBRE_APP}!! ========")
    print("--- Registro ---")
    print(f"{REGISTRAR_MAQUINA}. Registrar una máquina")
    print(f"{REGISTRAR_USO_MAQUINA}. Registrar uso de una máquina")
    print(f"{REGISTRAR_OPERADOR}. Registrar operador")
    print(f"{ASIGNAR_MAQUINA_OPERADOR}. Asignar máquina a operador")
    print("--- Mantenimiento ---")
    print(f"{REGISTRAR_FALLA}. Registrar una falla")
    print(f"{RESOLVER_FALLA}. Resolver una falla")
    print(f"{REGISTRAR_MANTENIMIENTO}. Registrar un mantenimiento")
    print(f"{REGISTRAR_REPUESTO}. Registrar repuesto / entrada de inventario")
    print(f"{ACTUALIZAR_REPUESTO}. Actualizar un repuesto")
    print("--- Consultas y reportes ---")
    print(f"{LISTA_MAQUINAS}. Mostrar lista de máquinas")
    print(f"{LISTA_OPERADORES}. Mostrar lista de operadores")
    print(f"{LISTA_REPUESTOS}. Mostrar inventario de repuestos")
    print(f"{CONSULTAR_HISTORIAL}. Consultar historial de una máquina")
    print(f"{REPORTE_COSTOS}. Reporte de costos de mantenimiento")
    print(f"{MAQUINAS_POR_REVISAR}. Máquinas que requieren revisión")
    print(f"{DATOS_FINCA}. Registrar / ver datos de la finca")
    print(f"{SALIR}. Salir")


def actualizar_gestor():
    gestor.set_maquinas(lista_maquinas)
    gestor.set_operadores(lista_operadores)
    gestor.set_repuestos(lista_repuestos)


while True:
    mostrar_menu()
    opcion = leer_entero("Selecciona una de las opciones: ", SALIR, DATOS_FINCA)

    match opcion:
        case 1:
            print("\n----- Registrar una máquina -----")
            lista_maquinas = registrar_maquina(Maquina(), lista_maquinas)
            finca.set_maquina(lista_maquinas[-1])
        case 2:
            print("\n----- Registrar uso de una máquina -----")
            lista_maquinas = registrar_uso_maquina(lista_maquinas)
        case 3:
            print("\n----- Registrar operador -----")
            lista_operadores = registrar_operador(lista_operadores)
        case 4:
            print("\n----- Asignar máquina a operador -----")
            lista_maquinas, lista_operadores = asignar_maquina_operador(
                lista_maquinas, lista_operadores
            )
        case 5:
            print("\n----- Registrar una falla presentada -----")
            lista_maquinas = registrar_falla(lista_maquinas)
        case 6:
            print("\n----- Resolver una falla -----")
            lista_maquinas = resolver_falla(lista_maquinas)
        case 7:
            print("\n----- Registrar un mantenimiento -----")
            lista_maquinas, lista_repuestos = registrar_mantenimiento(
                lista_maquinas, lista_repuestos
            )
        case 8:
            print("\n----- Registrar repuesto -----")
            lista_repuestos = registrar_repuesto(lista_repuestos)
        case 9:
            print("\n----- Actualizar un repuesto -----")
            lista_repuestos = actualizar_repuesto(lista_repuestos)
        case 10:
            print("\n----- Lista de máquinas -----")
            if not lista_maquinas:
                print("No hay máquinas registradas.")
            for maquina in lista_maquinas:
                print(f"{maquina.get_ficha_tecnica()}\n")
        case 11:
            print("\n----- Lista de operadores -----")
            if not lista_operadores:
                print("No hay operadores registrados.")
            for operador in lista_operadores:
                print(f"{operador.get_datos()}\n")
        case 12:
            print("\n----- Inventario de repuestos -----")
            if not lista_repuestos:
                print("No hay repuestos registrados.")
            for repuesto in lista_repuestos:
                print(f"{repuesto.get_datos_repuesto()}\n")
        case 13:
            print("\n----- Historial de una máquina -----")
            lista_maquinas = consultar_historial(lista_maquinas)
        case 14:
            print()
            actualizar_gestor()
            print(gestor.reporte_costos())
            repuestos_por_comprar = gestor.repuestos_por_comprar()
            if repuestos_por_comprar:
                print("\nRepuestos con stock bajo:")
                for repuesto in repuestos_por_comprar:
                    print(f"- {repuesto.get_nombre()} ({repuesto.get_codigo()}): "
                          f"{repuesto.get_stock()} unidad(es)")
        case 15:
            print()
            actualizar_gestor()
            print(gestor.reporte_revision())
        case 16:
            print("\n----- Datos de la finca -----")
            if finca.get_nombre() is None:
                registrar_finca(finca)
            else:
                print(finca.get_datos_finca())
                print("\nMaquinaria de la finca:")
                print(finca.listar_maquinas())

                actualizar = leer_entero("\n¿Desea actualizar los datos? (1. Sí / 2. No): ", 1, 2)
                if actualizar == 1:
                    registrar_finca(finca)
        case 0:
            print(f"\nGracias por usar {NOMBRE_APP}. ¡Hasta pronto!")
            break

# Secuencia ejecutada sobre el menú y resultado obtenido:
#
# "abc" -> "Debe ingresar un número entero, vuelva a intentar."
# "99"  -> "El valor debe ser menor o igual a 16."
#
# 1  -> tipo 1, "Maquina 5055E", "JD-2024-001", estado 2
#       Resultado: máquina registrada y ficha impresa (250.0 horas al próximo
#       mantenimiento, sin operador y sin fallas).
# 1  -> repitiendo la serie "JD-2024-001"
#       Resultado: "Ya existe una máquina registrada con ese número de serie."
#       y vuelve a pedir la serie sin duplicar el registro.
# 3  -> "Ana Gómez", "1090123456"  -> operador registrado con 0.0 horas.
# 3  -> repitiendo la identificación "1090123456"
#       Resultado: "Ya existe un operador registrado con esa identificación."
# 4  -> operador 1, máquina 1
#       Resultado: la ficha de la máquina muestra "Ana Gómez (1090123456)" y los
#       datos del operador muestran la máquina (relación en los dos sentidos).
# 2  -> máquina 1, horas 240, observación "Arado del lote 3"
#       Resultado: horas de uso 240.0 y
#       "ALERTA: faltan 10.0 horas para el mantenimiento preventivo".
# 8  -> "FIL-001", "Filtro de aceite", stock 5, costo 45000 -> repuesto creado.
# 7  -> máquina 1, tipo 1, "18-09-2026", "Cambio de aceite", 80000,
#       repuestos: sí -> repuesto 1 cantidad 2 -> "Stock restante: 3";
#                  sí -> repuesto 1 cantidad 99 -> "Stock insuficiente. Solo hay
#                        3 unidad(es)." (no altera el costo);
#                  no; estado 1
#       Resultado: costo mano de obra $80000, repuestos $90000, total $170000.
# 5  -> máquina 1, fecha "2026-09-01" -> "Formato de fecha inválido. Use DD-MM-AAAA";
#       fecha "01-09-2026", causa "Fuga de aceite", gravedad 1, estado 4
#       Resultado: falla [Abierta] y la máquina queda en estado "Malo".
# 15 -> "Maquina 5055E (JD-2024-001): mantenimiento en 10.0 horas y
#        1 falla(s) sin resolver".
# 6  -> máquina 1, falla 1, "06-09-2026", estado 2
#       Resultado: "La máquina estuvo detenida 5 día(s)" y la falla pasa a
#       [Resuelta].
# 14 -> "COSTO TOTAL DE LA FINCA: $170000.0" y "Máquina con mayor costo".
# 13 -> máquina 1: ficha técnica + 1 registro de uso + 1 mantenimiento + 1 falla.
# 16 -> "La Esperanza", "Carlos Ruiz", "Duitama", zona 3 (ZCBOY)
#       Resultado: datos de la finca con 1 máquina registrada.
# 16 -> segunda vez: muestra los datos, lista la maquinaria y pregunta
#       "¿Desea actualizar los datos?".
# 10, 11, 12 -> listan máquinas, operadores e inventario de repuestos.
# 9  -> repuesto 1, stock 10, costo 50000 -> repuesto actualizado.
# 0  -> "Gracias por usar AgroFix. ¡Hasta pronto!" y termina.
#
# Pruebas con las listas vacías (opciones 2, 4, 5, 6, 7, 9, 13, 14, 15):
# Resultado: cada una avisa que no hay registros y el programa continúa sin
# romperse ni perder la información ya cargada.
