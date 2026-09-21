class Repuesto:
    def __init__(self):
        self.nombre = None
        self.codigo = None
        self.stock = 0
        self.costo = 0.0

    def set_repuesto(self, nombre, codigo, stock, costo):
        self.nombre = nombre
        self.codigo = codigo
        self.stock = stock
        self.costo = costo

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_codigo(self, codigo):
        self.codigo = codigo

    def set_stock(self, stock):
        self.stock = stock

    def set_costo(self, costo):
        self.costo = costo

    def get_nombre(self):
        return self.nombre

    def get_codigo(self):
        return self.codigo

    def get_stock(self):
        return self.stock

    def get_costo(self):
        return self.costo

    def update_repuesto(self, nombre=None, costo=None, stock=None):
        if nombre is not None:
            self.nombre = nombre
        if costo is not None:
            self.costo = costo
        if stock is not None:
            self.stock = stock

    def hay_stock(self, cantidad):
        return self.stock >= cantidad

    def agregar_stock(self, cantidad):
        if cantidad <= 0:
            return False
        self.stock += cantidad
        return True

    def descontar_stock(self, cantidad):
        if cantidad <= 0 or not self.hay_stock(cantidad):
            return False
        self.stock -= cantidad
        return True

    def es_el_repuesto(self, texto_busqueda):
        return self.codigo == texto_busqueda or self.nombre == texto_busqueda

    def stock_bajo(self):
        return self.stock <= 2

    def get_datos_repuesto(self):
        alerta = " (STOCK BAJO)" if self.stock_bajo() else ""
        return (f"Nombre: {self.nombre}\n"
                f"Código: {self.codigo}\n"
                f"Cantidad en stock: {self.stock}{alerta}\n"
                f"Costo unitario: ${self.costo}")

# filtro = Repuesto()
# filtro.set_repuesto("Filtro de aceite", "FIL-001", 5, 45000.0)
#
# print(filtro.get_nombre())   # Filtro de aceite
# print(filtro.get_codigo())   # FIL-001
# print(filtro.get_stock())    # 5
# print(filtro.get_costo())    # 45000.0
#
# # Entradas y salidas de inventario
# print(filtro.agregar_stock(3))     # True  -> stock 8
# print(filtro.get_stock())          # 8
# print(filtro.descontar_stock(2))   # True  -> stock 6
# print(filtro.get_stock())          # 6
#
# # No se permite descontar más de lo que hay ni cantidades inválidas
# print(filtro.descontar_stock(100)) # False
# print(filtro.get_stock())          # 6 (sin cambios)
# print(filtro.agregar_stock(-5))    # False
# print(filtro.get_stock())          # 6 (sin cambios)
#
# # Alerta de stock bajo y búsqueda
# print(filtro.stock_bajo())              # False
# filtro.set_stock(1)
# print(filtro.stock_bajo())              # True
# print(filtro.es_el_repuesto("FIL-001")) # True
# print(filtro.es_el_repuesto("X"))     # False
#
# filtro.update_repuesto(costo=50000.0)
# print(filtro.get_costo())               # 50000.0
# print(filtro.get_nombre())              # Filtro de aceite (sin cambios)
# print(filtro.get_datos_repuesto())
