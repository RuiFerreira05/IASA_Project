from abc import ABC, abstractmethod

# Um comportamento pode ser definido por uma reaccao, 
# que aceita uma percepcao e retorna uma accao, ou um 
# comportamento composto, que desencadeia vários outros 
# comportamentos, e seleciona um destes para retornar a sua accao
class Comportamento(ABC):
    
    @abstractmethod
    def activar(self, percepcao):
        """"""