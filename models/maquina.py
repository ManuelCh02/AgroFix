class Maquina:
    HORAS_ENTRE_MANTENIMIENTOS = 250.0

    def __init__(self):
        self.tipo = None
        self.modelo = None
        self.numero_serie = None
        self.estado = None
        self.horas_uso_total = 0.0
        self.fallas = []
        self.historial_de_uso = []
        self.historial_de_mantenimiento = []
        self.operador = None

    def set_tipo(self, tipo):
        self.tipo = tipo

    def set_modelo(self, modelo):
        self.modelo = modelo

    def set_numero_serie(self, serie):
        self.numero_serie = serie

    def set_estado(self, estado):
        self.estado = estado

    def set_operador(self, operador):
        self.operador = operador

    def set_falla(self, falla):
        self.fallas.append(falla)

    def set_mantenimiento(self, mantenimiento):
        self.historial_de_mantenimiento.append(mantenimiento)


    def get_tipo(self):
        return self.tipo

    def get_modelo(self):
        return self.modelo

    def get_numero_serie(self):
        return self.numero_serie

    def get_estado(self):
        return self.estado

    def get_operador(self):
        return self.operador

    def get_horas_uso_total(self):
        return self.horas_uso_total

    def get_fallas(self):
        return self.fallas

    def get_historial_de_uso(self):
        return self.historial_de_uso

    def get_historial_de_mantenimiento(self):
        return self.historial_de_mantenimiento

    def registrar_uso(self, registro_uso):
        self.horas_uso_total += registro_uso.get_horas_uso()
        self.historial_de_uso.append(registro_uso)

    def es_la_maquina(self, texto_busqueda):
        return self.modelo == texto_busqueda or self.numero_serie == texto_busqueda

    def proximo_mantenimiento(self):
        horas_restantes = self.HORAS_ENTRE_MANTENIMIENTOS - (
            self.horas_uso_total % self.HORAS_ENTRE_MANTENIMIENTOS
        )
        return round(horas_restantes, 2)

    def requiere_mantenimiento(self):
        return self.proximo_mantenimiento() <= 20.0

    def costo_total(self):
        total = 0.0
        for mantenimiento in self.historial_de_mantenimiento:
            total += mantenimiento.costo_total()
        return round(total, 2)

    def tiempo_detenida(self):
        total = 0
        for falla in self.fallas:
            total += falla.get_tiempo_inactividad()
        return total

    def fallas_abiertas(self):
        return [falla for falla in self.fallas if not falla.esta_resuelta()]

    def get_ficha_tecnica(self):
        lista_fallas = [falla.get_falla() for falla in self.fallas]
        fallas_str = " | ".join(lista_fallas) if lista_fallas else "Ninguna"

        if self.operador is None:
            operador_str = "Sin asignar"
        else:
            operador_str = f"{self.operador.get_nombre()} ({self.operador.get_identificacion()})"

        return (f"Tipo: {self.tipo}\n"
                f"Modelo: {self.modelo}\n"
                f"Serie: {self.numero_serie}\n"
                f"Estado: {self.estado}\n"
                f"Horas de uso: {self.horas_uso_total}\n"
                f"Próximo mantenimiento en: {self.proximo_mantenimiento()} horas\n"
                f"Costo en mantenimientos: ${self.costo_total()}\n"
                f"Días detenida por fallas: {self.tiempo_detenida()}\n"
                f"Operador: {operador_str}\n"
                f"Fallas: {fallas_str}")

# from models.registroUso import RegistroUso
#
# tractor = Maquina()
# tractor.set_tipo("Tractor")
# tractor.set_modelo("John Deere 5055E")
# tractor.set_numero_serie("JD-2024-001")
# tractor.set_estado("Bueno")
#
# print(tractor.get_tipo())           # Tractor
# print(tractor.get_modelo())         # Maquina 5055E
# print(tractor.get_numero_serie())   # JD-2024-001
# print(tractor.get_estado())         # Bueno
# print(tractor.get_horas_uso_total()) # 0.0
#
# # Registro de uso: debe acumular horas y guardar el registro
# uso = RegistroUso()
# uso.set_registro_uso("10-09-2026", 240.0)
# tractor.registrar_uso(uso)
# print(tractor.get_horas_uso_total())      # 240.0
# print(len(tractor.get_historial_de_uso()))# 1
#
# # 250 - 240 = 10 horas restantes -> requiere mantenimiento (<= 20)
# print(tractor.proximo_mantenimiento())    # 10.0
# print(tractor.requiere_mantenimiento())   # True
#
# # Búsqueda por modelo o por serie
# print(tractor.es_la_maquina("JD-2024-001"))     # True
# print(tractor.es_la_maquina("No existe"))       # False
#
# # Sin mantenimientos ni fallas los acumulados quedan en cero
# print(tractor.costo_total())    # 0.0
# print(tractor.tiempo_detenida())# 0
# print(tractor.get_ficha_tecnica())
