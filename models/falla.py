class Falla:
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.causa = None
        self.gravedad = None
        self.estado = None
        self.fecha_resolucion = None
        self.maquina_afectada = None

    def set_falla(self, inicio, causa, gravedad, estado, maquina_afectada):
        self.inicio = inicio
        self.causa = causa
        self.gravedad = gravedad
        self.estado = estado
        self.maquina_afectada = maquina_afectada

    def get_falla(self):
        return (f"Inicio: {self.inicio}, Gravedad: {self.gravedad}\n")

    def get_duracion(self, ):
        pass

    def resolver(self, ):
        pass

    def get_tiempo_inactividad(self, ):
        pass