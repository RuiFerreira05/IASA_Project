from abc import ABC, abstractmethod

# Avaliador consiste na classe que atribuirá 
# uma determinada prioridade a cada nó da árvore de procura.
class Avaliador(ABC):
    
    @abstractmethod
    def prioridade(self, no):
        """"""