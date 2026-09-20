class Operador:
    def __init__(self):
        self.nombre = None
        self.identificacion = None
        self.maquina_asignada = None
        self.historial_de_uso = None

    def total_horas(self, ):
        pass

    def set_operador(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion

    def update_operador(self, ):
        pass

    def get_datos(self):
        return (f"Nombre: {self.nombre}\n"
                f"Identificación: {self.identificacion}\n"
                f"Maquina asignada: {self.maquina_asignada}\n"
                f"Historial de uso: {self.historial_de_uso}\n")