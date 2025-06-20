from abc import ABC, abstractmethod

class Planeador(ABC):
    """
    Uma classe que implemente o contrato de planeador
    tem de ser uma classe capaz de planear um plano com
    base num modelo de plano e um conjunto de objectivos
    """
    
    @abstractmethod
    def planear(self, modelo_plan, objectivos):
        """
        Planeia um plano com base num modelo de plano e um conjunto de objectivos.
        """