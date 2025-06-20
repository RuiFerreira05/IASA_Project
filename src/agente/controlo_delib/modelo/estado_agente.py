from mod.estado import Estado

# Representa o estado do agente no mundo.
# contem um identificador unico baseado na posicao do agente.
class EstadoAgente(Estado):
    
    @property
    def posicao(self):
        return self.__posicao
    
    def __init__(self, posicao):
        self.__posicao = posicao
    
    def id_valor(self):
        return hash(self.__posicao)