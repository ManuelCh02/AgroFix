class Finca:
    def __init__(self):
        self.propietario = None
        self.nombre = None
        self.municipio = None
        self.zona_rural = None
        self.maquinas = []

    def set_datos_finca(self, nombre, propietario, municipio, zona_rural):
        self.nombre = nombre
        self.propietario = propietario
        self.municipio = municipio
        self.zona_rural = zona_rural

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_propietario(self, propietario):
        self.propietario = propietario

    def set_municipio(self, municipio):
        self.municipio = municipio

    def set_zona_rural(self, zona_rural):
        self.zona_rural = zona_rural

    def set_maquina(self, maquina):
        self.maquinas.append(maquina)

    def get_nombre(self):
        return self.nombre

    def get_propietario(self):
        return self.propietario

    def get_municipio(self):
        return self.municipio

    def get_zona_rural(self):
        return self.zona_rural

    def get_maquinas(self):
        return self.maquinas

    def listar_maquinas(self):
        if not self.maquinas:
            return "La finca no tiene maquinaria registrada."

        lineas = []
        for maquina in self.maquinas:
            lineas.append(f"- {maquina.get_tipo()} {maquina.get_modelo()} "
                          f"({maquina.get_numero_serie()}) - Estado: {maquina.get_estado()}")
        return "\n".join(lineas)

    def total_maquinas(self):
        return len(self.maquinas)

    def get_datos_finca(self):
        return (f"Finca: {self.nombre}\n"
                f"Propietario: {self.propietario}\n"
                f"Municipio: {self.municipio}\n"
                f"Zona rural: {self.zona_rural}\n"
                f"Maquinaria registrada: {self.total_maquinas()}")


# from models.maquina import Maquina
#
# finca = Finca()
# finca.set_datos_finca("La Esperanza", "Carlos Ruiz", "Duitama", "ZCBOY")
#
# print(finca.get_nombre())       # La Esperanza
# print(finca.get_propietario())  # Carlos Ruiz
# print(finca.get_municipio())    # Duitama
# print(finca.get_zona_rural())   # ZCBOY
# print(finca.total_maquinas())   # 0
# print(finca.listar_maquinas())  # La finca no tiene maquinaria registrada.
#
# tractor = Maquina()
# tractor.set_tipo("Tractor")
# tractor.set_modelo("John Deere 5055E")
# tractor.set_numero_serie("JD-2024-001")
# tractor.set_estado("Bueno")
# finca.set_maquina(tractor)
#
# print(finca.total_maquinas())   # 1
# print(finca.listar_maquinas())  # - Maqquina 5055E (JD-2024-001) - Estado: Bueno
# print(finca.get_datos_finca())
