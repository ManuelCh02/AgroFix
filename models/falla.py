from datetime import datetime

FORMATO_FECHA = "%d-%m-%Y"

class Falla:
    GRAVEDADES = ["Alta", "Media", "Baja"]
    ESTADOS = ["Abierta", "Resuelta"]

    def __init__(self):
        self.inicio = None
        self.causa = None
        self.gravedad = None
        self.estado = "Abierta"
        self.fecha_resolucion = None
        self.maquina_afectada = None

    def set_falla(self, inicio, causa, gravedad, estado, maquina_afectada):
        self.inicio = inicio
        self.causa = causa
        self.gravedad = gravedad
        self.estado = estado
        self.maquina_afectada = maquina_afectada

    def set_inicio(self, inicio):
        self.inicio = inicio

    def set_causa(self, causa):
        self.causa = causa

    def set_gravedad(self, gravedad):
        self.gravedad = gravedad

    def set_estado(self, estado):
        self.estado = estado

    def set_maquina_afectada(self, maquina_afectada):
        self.maquina_afectada = maquina_afectada


    def get_inicio(self):
        return self.inicio

    def get_causa(self):
        return self.causa

    def get_gravedad(self):
        return self.gravedad

    def get_estado(self):
        return self.estado

    def get_fecha_resolucion(self):
        return self.fecha_resolucion

    def get_maquina_afectada(self):
        return self.maquina_afectada


    def resolver(self, fecha_resolucion):
        self.fecha_resolucion = fecha_resolucion
        self.estado = "Resuelta"

    def esta_resuelta(self):
        return self.fecha_resolucion is not None

    def get_duracion(self):
        if not self.esta_resuelta():
            return None
        try:
            inicio = datetime.strptime(self.inicio, FORMATO_FECHA)
            fin = datetime.strptime(self.fecha_resolucion, FORMATO_FECHA)
        except (ValueError, TypeError):
            return None
        return (fin - inicio).days

    def get_tiempo_inactividad(self):
        if self.esta_resuelta():
            duracion = self.get_duracion()
            return duracion if duracion is not None else 0
        try:
            inicio = datetime.strptime(self.inicio, FORMATO_FECHA)
        except (ValueError, TypeError):
            return 0
        return (datetime.today() - inicio).days

    def get_falla(self):
        return (f"[{self.estado}] Inicio: {self.inicio} - "
                f"Causa: {self.causa} - "
                f"Gravedad: {self.gravedad}")

    def get_detalle(self):
        if self.maquina_afectada is None:
            maquina_str = "Sin asignar"
        else:
            maquina_str = f"{self.maquina_afectada.get_modelo()} ({self.maquina_afectada.get_numero_serie()})"

        return (f"Máquina afectada: {maquina_str}\n"
                f"Inicio: {self.inicio}\n"
                f"Causa: {self.causa}\n"
                f"Gravedad: {self.gravedad}\n"
                f"Estado de la falla: {self.estado}\n"
                f"Fecha de resolución: {self.fecha_resolucion if self.esta_resuelta() else 'Pendiente'}\n"
                f"Días de inactividad: {self.get_tiempo_inactividad()}")


# from models.maquina import Maquina
#
# tractor = Maquina()
# tractor.set_modelo("Maquina 5055E")
# tractor.set_numero_serie("JD-2024-001")
#
# falla = Falla()
# falla.set_falla("01-09-2026", "Fuga de aceite", "Alta", "Abierta", tractor)
#
# print(falla.get_inicio())      # 01-09-2026
# print(falla.get_causa())       # Fuga de aceite
# print(falla.get_gravedad())    # Alta
# print(falla.esta_resuelta())   # False
# print(falla.get_duracion())    # None (aún abierta)
#
# # Al resolverla se calculan los días de duración
# falla.resolver("06-09-2026")
# print(falla.esta_resuelta())          # True
# print(falla.get_duracion())           # 5
# print(falla.get_tiempo_inactividad()) # 5
# print(falla.get_estado())             # Resuelta
#
# # Una fecha mal escrita no debe romper el programa
# falla_mala = Falla()
# falla_mala.set_falla("31-31-2026", "Fecha inválida", "Baja", "Abierta", tractor)
# falla_mala.resolver("01-01-2026")
# print(falla_mala.get_duracion())      # None
# print(falla.get_detalle())
