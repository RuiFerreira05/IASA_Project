from abc import ABC, abstractmethod

# Um problema é definido por um estado inicial
# e um conjunto de operadores que quando aplicados
# sob os estados de um espaço de estados, devem levar 
# a um estado objetivo tambem definido. 
# (Pode não existir solução, dentro do espaço de estados).

# O problema é resolvido por um mecanismo de procura,
# que, começando no estado inicial, procura a solução do problema, 
# explorando o espaço de estados em que este se aplica.
class Problema(ABC):
    
    # Define uma propriedade {read-only} dado ser declarado
    # apenas um getter com o decorador @property.
    @property
    def estado_inicial(self):
        return self.__estado_inicial
    
    # read-only
    @property
    def operadores(self):
        return self.__operadores
    
    def __init__(self, estado_inicial, operadores):
        
        # garantir que operadores não é uma lista vazia
        assert(len(operadores) > 0)
        
        self.__estado_inicial = estado_inicial
        self.__operadores = operadores
    
    # Classe Problema pretende ser aplicada
    # a qualquer tipo de problema, portanto o método
    # objetivo deve ser abstrato
    @abstractmethod
    def objetivo(self, estado):
        """"""
    
    
    