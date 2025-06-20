from abc import ABC, abstractmethod


class ModeloPDM(ABC):
    
    # estados possiveis
    @abstractmethod
    def S(self):
        """
        Retorna a lista de estados possiveis do ambiente
        """
        
    # acções possiveis
    @abstractmethod
    def A(self, s):
        """
        Retorna a lista de acções possiceis para o estado 's'
        """

    # transição de estados
    @abstractmethod    
    def T(self, s, a, sn):
        """
        retorna a probabilidade de transição do estado 's' 
        para o estado 'sn' ao aplicar a ação 'a'
        """

    # recompensa
    @abstractmethod
    def R(self, s, a, sn):
        """
        retorna a recompensa da transição do estado 's'
        para o estado 'sn' ao aplicar a ação 'a'
        """

    #estado sucessor
    @abstractmethod
    def suc(self, s, a):
        """
        Gera o estado successor que resulta de aplicar a ação 'a' 
        no estado 's'
        """
