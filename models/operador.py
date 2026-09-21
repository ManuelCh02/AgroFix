class Operador:
    def __init__(self):
        self.nombre = None
        self.identificacion = None
        self.maquina_asignada = None
        self.historial_de_uso = []

    def set_operador(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_identificacion(self, identificacion):
        self.identificacion = identificacion

    def set_maquina_asignada(self, maquina_asignada):
        self.maquina_asignada = maquina_asignada

    def set_registro_uso(self, registro_uso):
        self.historial_de_uso.append(registro_uso)

    def get_nombre(self):
        return self.nombre

    def get_identificacion(self):
        return self.identificacion

    def get_maquina_asignada(self):
        return self.maquina_asignada

    def get_historial_de_uso(self):
        return self.historial_de_uso

    def update_operador(self, nombre=None, identificacion=None):
        if nombre is not None:
            self.nombre = nombre
        if identificacion is not None:
            self.identificacion = identificacion

    def total_horas(self): 
        total = 0.0
        for registro in self.historial_de_uso:
            total += registro.get_horas_uso()
        return round(total, 2)

    def tiene_maquina(self):
        return self.maquina_asignada is not None

    def get_datos(self):
        if self.maquina_asignada is None:
            maquina_str = "Sin asignar"
        else:
            maquina_str = f"{self.maquina_asignada.get_modelo()} ({self.maquina_asignada.get_numero_serie()})"

        return (f"Nombre: {self.nombre}\n"
                f"Identificación: {self.identificacion}\n"
                f"Máquina asignada: {maquina_str}\n"
                f"Total de horas trabajadas: {self.total_horas()}\n"
                f"Registros de uso: {len(self.historial_de_uso)}")


# from models.maquina import Maquina
# from models.registroUso import RegistroUso
#
# operador = Operador()
# operador.set_operador("Ana Gómez", "1090123456")
# print(operador.get_nombre())          # Ana Gómez
# print(operador.get_identificacion())  # 1090123456
# print(operador.tiene_maquina())       # False
# print(operador.total_horas())         # 0.0
#
# # Asignación de máquina
# tractor = Maquina()
# tractor.set_modelo("John Deere 5055E")
# tractor.set_numero_serie("JD-2024-001")
# operador.set_maquina_asignada(tractor)
# print(operador.tiene_maquina())                        # True
# print(operador.get_maquina_asignada().get_modelo())    # Maquina 5055E
#
# # Las horas se suman de todos los registros del operador
# uso1 = RegistroUso(); uso1.set_registro_uso("15-09-2026", 6.5, operador)
# uso2 = RegistroUso(); uso2.set_registro_uso("16-09-2026", 3.5, operador)
# operador.set_registro_uso(uso1)
# operador.set_registro_uso(uso2)
# print(operador.total_horas())         # 10.0
#
# # update_operador cambia solo el dato enviado
# operador.update_operador(nombre="Ana María Gómez")
# print(operador.get_nombre())          # Ana María Gómez
# print(operador.get_identificacion())  # 1090123456 (sin cambios)
# print(operador.get_datos())
