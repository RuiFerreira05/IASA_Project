from ecr.comportamento import Comportamento
from sae.agente.avancar import Avancar


class ExplorarMem(Comportamento):
    
    def __init__(self, memoria_max = 100):
        self.__memoria = list()
        self.__memoria_max = memoria_max
        
    # Activar baseia-se em agir só se a situação atual em que se encontra
    # não estiver na memória
    # Se a situação já estiver na memória, não faz nada
    def activar(self, percepcao):
        situacao = (percepcao.posicao, percepcao.direccao)
        if situacao not in self.__memoria:
            self.__memoria.append(situacao)
            if len(self.__memoria) > self.__memoria_max:
                self.__memoria.pop(0)
            return Avancar()