from abc import ABC, abstractmethod

# Esta classe representa uma ação que quando aplicada
# sob um estado, gera uma transição para um novo estado.
class Operador(ABC):
    
    # retorna o estado sucessivo que resulta 
    # da aplicacao do operador no estado atual
    @abstractmethod
    def aplicar(self, estado):
        """"""
    
    # Determina o custo da transição    
    @abstractmethod
    def custo(self, estado, estado_suc):
        """"""