class GestorMaquinaria:
    def __init__(self):
        self.maquinas = []
        self.operadores = []
        self.repuestos = []

    def set_maquinas(self, maquinas):
        self.maquinas = maquinas

    def set_operadores(self, operadores):
        self.operadores = operadores

    def set_repuestos(self, repuestos):
        self.repuestos = repuestos

    def get_maquinas(self):
        return self.maquinas

    def get_operadores(self):
        return self.operadores

    def get_repuestos(self):
        return self.repuestos

    def buscar_maquina(self, texto_busqueda):
        for maquina in self.maquinas:
            if maquina.es_la_maquina(texto_busqueda):
                return maquina
        return None

    def buscar_repuesto(self, texto_busqueda):
        for repuesto in self.repuestos:
            if repuesto.es_el_repuesto(texto_busqueda):
                return repuesto
        return None

    def buscar_operador(self, identificacion):
        for operador in self.operadores:
            if operador.get_identificacion() == identificacion:
                return operador
        return None

    def maquinas_por_revisar(self):
        por_revisar = []
        for maquina in self.maquinas:
            if maquina.requiere_mantenimiento() or maquina.fallas_abiertas():
                por_revisar.append(maquina)
        return por_revisar

    def repuestos_por_comprar(self):
        return [repuesto for repuesto in self.repuestos if repuesto.stock_bajo()]

    def costo_total_mantenimientos(self):
        total = 0.0
        for maquina in self.maquinas:
            total += maquina.costo_total()
        return round(total, 2)

    def maquina_mas_costosa(self):
        if not self.maquinas:
            return None
        return max(self.maquinas, key=lambda maquina: maquina.costo_total())

    def reporte_costos(self):
        if not self.maquinas:
            return "No hay maquinaria registrada para generar el reporte."

        lineas = ["----- REPORTE DE COSTOS DE MANTENIMIENTO -----"]
        for maquina in self.maquinas:
            lineas.append(f"- {maquina.get_modelo()} ({maquina.get_numero_serie()}): "
                          f"${maquina.costo_total()} en "
                          f"{len(maquina.get_historial_de_mantenimiento())} mantenimiento(s)")

        lineas.append(f"COSTO TOTAL DE LA FINCA: ${self.costo_total_mantenimientos()}")

        mas_costosa = self.maquina_mas_costosa()
        if mas_costosa is not None and mas_costosa.costo_total() > 0:
            lineas.append(f"Máquina con mayor costo: {mas_costosa.get_modelo()} "
                          f"(${mas_costosa.costo_total()})")
        return "\n".join(lineas)

    def reporte_revision(self):
        por_revisar = self.maquinas_por_revisar()
        if not por_revisar:
            return "Ninguna máquina requiere revisión en este momento."

        lineas = ["----- MÁQUINAS QUE REQUIEREN REVISIÓN -----"]
        for maquina in por_revisar:
            motivos = []
            if maquina.requiere_mantenimiento():
                motivos.append(f"mantenimiento en {maquina.proximo_mantenimiento()} horas")
            if maquina.fallas_abiertas():
                motivos.append(f"{len(maquina.fallas_abiertas())} falla(s) sin resolver")
            lineas.append(f"- {maquina.get_modelo()} ({maquina.get_numero_serie()}): "
                          f"{' y '.join(motivos)}")
        return "\n".join(lineas)


# from models.maquina import Maquina
# from models.repuesto import Repuesto
# from models.mantenimiento import Mantenimiento
# from models.falla import Falla
# from models.registroUso import RegistroUso
#
# tractor = Maquina()
# tractor.set_tipo("Tractor")
# tractor.set_modelo("John Deere 5055E")
# tractor.set_numero_serie("JD-2024-001")
# tractor.set_estado("Bueno")
#
# fumigadora = Maquina()
# fumigadora.set_tipo("Fumigadora")
# fumigadora.set_modelo("Jacto PJ-600")
# fumigadora.set_numero_serie("JA-2023-007")
# fumigadora.set_estado("Regular")
#
# filtro = Repuesto()
# filtro.set_repuesto("Filtro de aceite", "FIL-001", 1, 45000.0)
#
# gestor = GestorMaquinaria()
# gestor.set_maquinas([tractor, fumigadora])
# gestor.set_repuestos([filtro])
#
# # Búsquedas
# print(gestor.buscar_maquina("JD-2024-001").get_modelo())  # Maquina 5055E
# print(gestor.buscar_maquina("No existe"))                 # None
# print(gestor.buscar_repuesto("FIL-001").get_nombre())     # Filtro de aceite
#
# # Sin uso ni fallas ninguna máquina requiere revisión
# print(len(gestor.maquinas_por_revisar()))   # 0
#
# # El tractor llega a 240 horas -> faltan 10 para el mantenimiento
# uso = RegistroUso(); uso.set_registro_uso("15-09-2026", 240.0)
# tractor.registrar_uso(uso)
# print(len(gestor.maquinas_por_revisar()))   # 1
#
# # Una falla abierta también obliga a revisar la máquina
# falla = Falla()
# falla.set_falla("01-09-2026", "Boquilla tapada", "Media", "Regular", fumigadora)
# fumigadora.set_falla(falla)
# print(len(gestor.maquinas_por_revisar()))   # 2
#
# # Reporte de costos
# mantenimiento = Mantenimiento()
# mantenimiento.set_mantenimiento("Preventivo", "18-09-2026", "Cambio de aceite", 80000.0, tractor)
# tractor.set_mantenimiento(mantenimiento)
# print(gestor.costo_total_mantenimientos())            # 80000.0
# print(gestor.maquina_mas_costosa().get_modelo())      # Maquina 5055E
# print(len(gestor.repuestos_por_comprar()))   
# print(gestor.reporte_costos())
# print(gestor.reporte_revision())
