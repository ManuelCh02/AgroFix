from services.utilidades import leer_texto, seleccionar_opcion

ZONAS_RURALES = ["ZAO", "ZOCC", "ZCBOY", "Otra"]


def registrar_finca(finca):
    nombre = leer_texto("Ingrese el nombre de la finca: ")
    propietario = leer_texto("Ingrese el nombre del propietario: ")
    municipio = leer_texto("Ingrese el municipio: ")

    zona_rural = seleccionar_opcion("Seleccione la zona rural:", ZONAS_RURALES)
    if zona_rural == "Otra":
        zona_rural = leer_texto("Escriba el nombre de la zona: ")

    finca.set_datos_finca(nombre, propietario, municipio, zona_rural)

    print("\nDatos de la finca guardados correctamente.")
    print(finca.get_datos_finca())
    return finca


# Prueba manual desde el menú (opción 11):
#
# Nombre "La Esperanza", propietario "Carlos Ruiz", municipio "Duitama",
# zona 3 (ZCBOY):
# Resultado esperado: se imprimen los datos de la finca con la zona ZCBOY.
#
# Nombre vacío (solo Enter):
# Resultado esperado: "El dato no puede quedar vacío, vuelva a intentar."
#
# from models.finca import Finca
# finca = registrar_finca(Finca())
# print(finca.get_nombre())      # La Esperanza
# print(finca.get_zona_rural())  # ZCBOY
