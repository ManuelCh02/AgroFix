from models.repuesto import Repuesto
from services.utilidades import (
    describir_repuesto,
    leer_decimal,
    leer_entero,
    leer_texto,
    seleccionar_de_lista,
)


def registrar_repuesto(lista_repuestos):
    lista = lista_repuestos

    codigo = leer_texto("Ingrese el código del repuesto: ")

    for registrado in lista:
        if registrado.get_codigo() == codigo:
            print("Ya existe un repuesto con ese código, se sumará al stock actual.")
            cantidad = leer_entero("Ingrese la cantidad que ingresa al inventario: ", 1)
            registrado.agregar_stock(cantidad)
            print("\nStock actualizado correctamente.")
            print(registrado.get_datos_repuesto())
            return lista

    nombre = leer_texto("Ingrese el nombre del repuesto: ")
    stock = leer_entero("Ingrese la cantidad en stock: ", 0)
    costo = leer_decimal("Ingrese el costo unitario: ", 0)

    repuesto = Repuesto()
    repuesto.set_repuesto(nombre, codigo, stock, costo)
    lista.append(repuesto)

    print("\nRepuesto registrado correctamente.")
    print(repuesto.get_datos_repuesto())
    return lista


def actualizar_repuesto(lista_repuestos):
    lista = lista_repuestos

    repuesto = seleccionar_de_lista(
        "Seleccione el repuesto que desea actualizar:", lista, describir_repuesto
    )
    if repuesto is None:
        return lista

    nuevo_stock = leer_entero("Ingrese la nueva cantidad en stock: ", 0)
    nuevo_costo = leer_decimal("Ingrese el nuevo costo unitario: ", 0)
    repuesto.update_repuesto(stock=nuevo_stock, costo=nuevo_costo)

    print("\nRepuesto actualizado correctamente.")
    print(repuesto.get_datos_repuesto())
    return lista

# Prueba manual desde el menú (opción 8):
#
# Código "FIL-001", nombre "Filtro de aceite", stock 5, costo 45000:
# Resultado esperado: repuesto creado con stock 5.
#
# Repetir con el código "FIL-001" y cantidad 3:
# Resultado esperado: "Ya existe un repuesto con ese código, se sumará al stock"
#                     y el stock queda en 8 sin crear un segundo repuesto.
#
# Cantidad "-1":
# Resultado esperado: "El valor debe ser mayor o igual a 1."
#
# lista = []
# lista = registrar_repuesto(lista)     # FIL-001 / Filtro de aceite / 5 / 45000
# print(len(lista))                     # 1
# print(lista[0].get_stock())           # 5
# lista = registrar_repuesto(lista)     # FIL-001 / cantidad 3
# print(len(lista))                     # 1 (no se duplica)
# print(lista[0].get_stock())           # 8
