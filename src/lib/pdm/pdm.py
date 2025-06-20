from lib.pdm.mec_util import MecUtil


class PDM:
    """
    Processo de Decisão de Markov
    """
    
    def __init__(self, modelo, gama, delta_max):
        self.__modelo = modelo
        self.__mec_util = MecUtil(modelo, gama, delta_max)


    def politica(self, U):
        """
        Retorna a política associada ao modelo
        dado um conjunto de utilidades U.
        A política é um dicionário onde a chave é o estado
        e o valor é a ação a tomar nesse estado.
        """
        S, A = self.__modelo.S, self.__modelo.A
        util_acao = self.__mec_util.util_accao
        
        pol = {}

        for s in S():
            if A(s):
                pol[s] = max(A(s), key=lambda a: util_acao(s, a, U))
            
        return pol
                
    def resolver(self):
        """
        Resolve o modelo e retorna a utilidade em cada estado e a política associada.
        """
        utilidade = self.__mec_util.utilidade()
        politica = self.politica(utilidade)
        return utilidade, politica