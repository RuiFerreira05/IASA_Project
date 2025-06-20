from abc import ABC, abstractmethod

# Esta classe pretende representar uma configuração
# de um problema ou sistema.
# É definida com identificação unica.
# e1 = Estado(1, 2)
# e2 = Estado(1, 2)
# e1 == e2 -> True 
# Esta caracteristica foi implementada dando override
# dos métodos default __hash__ e __eq__.
class Estado(ABC):
    
    @abstractmethod
    def id_valor(self):
        """"""
    
    # Função de identificador unico para o estado
    # Permite que Estados com mesmo valor sejam considerados iguais
    def __hash__(self):
        return self.id_valor()
    
    # Método de comparação entre dois estados
    # Utiliza o método __hash__ para comparar os estados
    def __eq__(self, other):
        if isinstance(other, Estado):
            return self.__hash__() == other.__hash__()
        
    