from abc import ABC, abstractmethod

# Representa o modelo de um plano
# Esta interface é contratada pelo ModeloMundo
class ModeloPlan(ABC):
    
    @abstractmethod
    def obter_estado():
        """
        Retorna o estado atual do Agente.
        """
        
    @abstractmethod
    def obter_estados():
        """
        Retorna a lista de estados possíveis do ambiente.
        """
        
    @abstractmethod
    def obter_operadores():
        """
        Retorna a lista de operadores possíveis do Modelo.
        """