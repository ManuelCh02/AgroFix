class RegistroUso:
    def __init__(self):
        self.fecha = None
        self.horas_uso = 0.0
        self.operador_asignado = None
        self.observaciones = None

    def set_registro_uso(self, fecha, horas_uso, operador_asignado=None, observaciones=""):
        self.fecha = fecha
        self.horas_uso = horas_uso
        self.operador_asignado = operador_asignado
        self.observaciones = observaciones

    def set_fecha(self, fecha):
        self.fecha = fecha

    def set_horas_uso(self, horas_uso):
        self.horas_uso = horas_uso

    def set_operador_asignado(self, operador_asignado):
        self.operador_asignado = operador_asignado

    def set_observaciones(self, observaciones):
        self.observaciones = observaciones

    def get_fecha(self):
        return self.fecha

    def get_horas_uso(self):
        return self.horas_uso

    def get_operador_asignado(self):
        return self.operador_asignado

    def get_observaciones(self):
        return self.observaciones


    def update_registro(self, horas_uso=None, observaciones=None):
        if horas_uso is not None:
            self.horas_uso = horas_uso
        if observaciones is not None:
            self.observaciones = observaciones

    def get_duracion(self):
        return round(self.horas_uso / 8.0, 2)

    def get_registro_uso(self):
        if self.operador_asignado is None:
            operador_str = "Sin asignar"
        else:
            operador_str = self.operador_asignado.get_nombre()

        return (f"Fecha: {self.fecha} - "
                f"Horas: {self.horas_uso} ({self.get_duracion()} jornadas) - "
                f"Operador: {operador_str} - "
                f"Observaciones: {self.observaciones if self.observaciones else 'Ninguna'}")

# from models.operador import Operador
#
# operador = Operador()
# operador.set_operador("Ana Gómez", "1090123456")
#
# registro = RegistroUso()
# registro.set_registro_uso("15-09-2026", 16.0, operador, "Arado del lote 3")
#
# print(registro.get_fecha())             # 15-09-2026
# print(registro.get_horas_uso())         # 16.0
# print(registro.get_duracion())          # 2.0 jornadas de 8 horas
# print(registro.get_operador_asignado().get_nombre())  # Ana Gómez
# print(registro.get_observaciones())     # Arado del lote 3
#
# # El setter asigna, no acumula: al volver a llamarlo el valor se reemplaza
# registro.set_horas_uso(4.0)
# print(registro.get_horas_uso())         # 4.0
#
# # update_registro solo cambia lo que se le envía
# registro.update_registro(observaciones="Se detuvo por lluvia")
# print(registro.get_horas_uso())         # 4.0 (no cambió)
# print(registro.get_observaciones())     # Se detuvo por lluvia
# print(registro.get_registro_uso())
