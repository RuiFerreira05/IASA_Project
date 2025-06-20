from contagem.modelo.estado_contagem import EstadoContagem
from mod.operador import Operador


class OperadorIncremento(Operador):
    
    def __init__(self, incremento):
        self.incremento = incremento
    
    def aplicar(self, estado):
        novo_valor = estado.valor + self.incremento
        return EstadoContagem(novo_valor)
    
    def custo(self, estado, estado_suc):
        return self.incremento ** 2