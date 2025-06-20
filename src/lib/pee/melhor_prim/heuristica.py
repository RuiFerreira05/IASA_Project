from abc import ABC, abstractmethod


class Heuristica(ABC):
    
    @abstractmethod
    def h(estado):
        """
        Calcula a heuristica para o estado dado.
        Deve ser implementada por subclasses para fornecer
        uma função heurística específica que avalia a qualidade
        de um estado em relação ao objetivo do modelo.
        """