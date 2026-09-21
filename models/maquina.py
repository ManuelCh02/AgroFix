class Maquina:
    def __init__(self):
        self.tipo = None
        self.modelo = None
        self.numero_serie = None
        self.fallas = []
        self.horas_uso_total = 0.0
        self.historial_de_uso = None
        self.historial_de_manteniniento = None
        self.operador = None

    def registrar_uso(self, uso):
        self.horas_uso_total += uso

    def set_modelo(self, modelo):
        self.modelo = modelo

    def set_numero_serie(self, serie):
        self.numero_serie = serie

    def set_operador(self, operador):
        self.operador = operador

    def set_estado(self, estado):
        self.estado = estado

    def set_falla(self, falla):
        self.fallas.append(falla)

    def get_modelo(self):
        return self.modelo
    
    def get_numero_serie(self):
        return self.numero_serie

    def proximo_mantenimiento(self, ):
        pass

    def costo_total(self, ):
        pass

    def tiempo_detenida(self, ):
        pass

    def get_ficha_tecnica(self):
        lista_fallas = [falla.get_falla() for falla in self.fallas]
        fallas_str = ", ".join(lista_fallas) if lista_fallas else "Ninguna"

        return (f"Modelo: {self.modelo}\n"
                f"Serie: {self.numero_serie}\n"
                f"Estado: {self.estado}\n"
                f"Horas de uso: {self.horas_uso_total}\n"
                f"Operador: {self.operador}\n"
                f"Fallas: {fallas_str}")