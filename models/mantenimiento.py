class Mantenimiento:
    TIPOS = ["Preventivo", "Correctivo", "Predictivo"]

    def __init__(self):
        self.tipo = None
        self.fecha = None
        self.descripcion = None
        self.costo_mano_obra = 0.0
        self.maquina_asignada = None
        self.repuestos_usados = []

    def set_mantenimiento(self, tipo, fecha, descripcion, costo_mano_obra, maquina_asignada):
        self.tipo = tipo
        self.fecha = fecha
        self.descripcion = descripcion
        self.costo_mano_obra = costo_mano_obra
        self.maquina_asignada = maquina_asignada

    def set_tipo(self, tipo):
        self.tipo = tipo

    def set_fecha(self, fecha):
        self.fecha = fecha

    def set_descripcion(self, descripcion):
        self.descripcion = descripcion

    def set_costo_mano_obra(self, costo_mano_obra):
        self.costo_mano_obra = costo_mano_obra

    def set_maquina_asignada(self, maquina_asignada):
        self.maquina_asignada = maquina_asignada


    def get_tipo(self):
        return self.tipo

    def get_fecha(self):
        return self.fecha

    def get_descripcion(self):
        return self.descripcion

    def get_costo_mano_obra(self):
        return self.costo_mano_obra

    def get_maquina_asignada(self):
        return self.maquina_asignada

    def get_repuestos_usados(self):
        return self.repuestos_usados


    def agregar_repuesto(self, repuesto, cantidad):
        if not repuesto.descontar_stock(cantidad):
            return False
        self.repuestos_usados.append({"repuesto": repuesto, "cantidad": cantidad})
        return True

    def costo_repuestos(self):
        total = 0.0
        for usado in self.repuestos_usados:
            total += usado["repuesto"].get_costo() * usado["cantidad"]
        return round(total, 2)

    def costo_total(self):
        return round(self.costo_mano_obra + self.costo_repuestos(), 2)

    def get_mantenimiento(self):
        if self.maquina_asignada is None:
            maquina_str = "Sin asignar"
        else:
            maquina_str = f"{self.maquina_asignada.get_modelo()} ({self.maquina_asignada.get_numero_serie()})"

        if self.repuestos_usados:
            lista_repuestos = [
                f"{usado['repuesto'].get_nombre()} x{usado['cantidad']}"
                for usado in self.repuestos_usados
            ]
            repuestos_str = ", ".join(lista_repuestos)
        else:
            repuestos_str = "Ninguno"

        return (f"Tipo: {self.tipo}\n"
                f"Fecha: {self.fecha}\n"
                f"Descripción: {self.descripcion}\n"
                f"Máquina: {maquina_str}\n"
                f"Repuestos usados: {repuestos_str}\n"
                f"Costo mano de obra: ${self.costo_mano_obra}\n"
                f"Costo repuestos: ${self.costo_repuestos()}\n"
                f"Costo total: ${self.costo_total()}")


# from models.maquina import Maquina
# from models.repuesto import Repuesto
#
# tractor = Maquina()
# tractor.set_modelo("Maquina 5055E")
# tractor.set_numero_serie("JD-2024-001")
#
# filtro = Repuesto()
# filtro.set_repuesto("Filtro de aceite", "FIL-001", 5, 45000.0)
#
# mantenimiento = Mantenimiento()
# mantenimiento.set_mantenimiento("Preventivo", "18-09-2026", "Cambio de aceite", 80000.0, tractor)
#
# print(mantenimiento.get_tipo())            # Preventivo
# print(mantenimiento.get_fecha())           # 18-09-2026
# print(mantenimiento.costo_repuestos())     # 0.0
# print(mantenimiento.costo_total())         # 80000.0
#
# # Agregar repuesto descuenta stock y suma al costo
# print(mantenimiento.agregar_repuesto(filtro, 2))  # True
# print(filtro.get_stock())                  # 3 (5 - 2)
# print(mantenimiento.costo_repuestos())     # 90000.0
# print(mantenimiento.costo_total())         # 170000.0
#
# # Si no hay stock suficiente no se agrega ni se altera el costo
# print(mantenimiento.agregar_repuesto(filtro, 99)) # False
# print(filtro.get_stock())                  # 3 (sin cambios)
# print(mantenimiento.costo_total())         # 170000.0
#
# # El mantenimiento queda en el historial de la máquina
# tractor.set_mantenimiento(mantenimiento)
# print(tractor.costo_total())               # 170000.0
# print(mantenimiento.get_mantenimiento())
