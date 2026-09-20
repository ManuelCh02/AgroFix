from models.operador import Operador

def registrar_operador(lista_operadores, nombre, identificacion):
    operador = Operador()
    operador.set_operador(nombre, identificacion)
    lista = lista_operadores
    
    lista.append(operador)
    return lista
