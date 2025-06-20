
from abc import ABC, abstractmethod

# Um plano representa uma sequência de passos
# a realizar para chegar a um determinado objetivo.
# tem também de ser capaz de obter a accao a realizar
# com base no estado actual.
class Plano(ABC):
    
    @abstractmethod
    def obter_accao(self, estado):
        """
        Obtem a ação a ser realizada no estado atual (parâmetro Estado).
        """
        
    @abstractmethod
    def mostrar(self, vista):
        """
        Mostra o plano de acordo com a vista (parâmetro Vista).
        """