from contagem.modelo.estado_contagem import EstadoContagem
from contagem.modelo.operador_incremento import OperadorIncremento
from mod.problema import Problema


class ProblemaContagem(Problema):
    
    def __init__(self, valor_inicial, valor_final, incrementos):
        super().__init__(EstadoContagem(valor_inicial), [OperadorIncremento(incremento) for incremento in incrementos])
        self.__valor_final = valor_final
    
    def objetivo(self, estado):
        return estado.valor >= self.__valor_final