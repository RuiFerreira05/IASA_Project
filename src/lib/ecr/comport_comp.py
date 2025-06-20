from abc import ABC, abstractmethod
from .comportamento import Comportamento
# Import relativo começa com "." no inicio,
# import global é composto apenas pelo nome do modulo


class ComportComp(Comportamento, ABC):
    
    def __init__(self, comportamentos):
        self.__comportamentos = comportamentos
    
    def activar(self, percepcao):
        accoes = []
        for comportamento in self.__comportamentos:
            accao = comportamento.activar(percepcao)
            # Instancias de objetos são convertidas para true, "None" para falso
            if accao: # Mesma coisa que "accao is not None"
                accoes.append(accao)
        
        # Contentores (Arrays, Listas, ...) são convertidos para 
        # booleanos com base em se têm elementos ou não.
        # (eg: [] == false, [x, y] == true)
        if accoes: 
            return self.seleccionar_accao(accoes)
    
    @abstractmethod
    def seleccionar_accao(self, accoes):
        """"""