from abc import ABC, abstractmethod

# Ao Herdar da classe ABC, definimos a classe como abstract
class Estimulo(ABC):
    
    # Decorator "abstractmethod" permite declarar metodos abstratos
    @abstractmethod
    def detectar(self, percepcao):
        """Detectar estimulo na percepcao"""