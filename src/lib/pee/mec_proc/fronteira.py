from abc import ABC, abstractmethod

# classe representativa da fronteira de procura
# A fronteira de procura armazena os nós que ainda estão por
# analizar/expandir. (As folhas da arvore de procura).
class Fronteira(ABC):
    
    @property
    def vazia(self):
        return len(self._nos) == 0
    
    def __init__(self):
        self.iniciar()
        self.__vazia = True # Fronteira começa sempre vazia
        
    def iniciar(self):
        self._nos = list()
    
    @abstractmethod
    def inserir(self, no):
        """"""
        
    def remover(self):
        # A fronteira remove e retorna o nó no index 0
        return self._nos.pop(0)
        