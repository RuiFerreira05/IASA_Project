# Esta classe representa uma solução para um problema.
# A solução consiste num nó final que representa o estado
# objetivo do problema.
# Esta classe contem a dimensão da solução (A sua profundidade)
# e o custo total da solução.


from pee.mec_proc.passo_solucao import PassoSolucao


class Solucao:
    
    # Estas propriedades são propriedades derivadas, que por definição
    # tem o seu valor calculado apenas durante runtime.
    @property
    def dimensao(self):
        return self.__no_final.profundidade
    
    @property
    def custo(self):
        return self.__no_final.custo
    
    def __init__(self, no_final):
        self.__no_final = no_final
        self.__passos = []
        no = no_final
        while no.antecessor:
            passo = PassoSolucao(no.antecessor.estado, no.operador)
            self.__passos.insert(0, passo)
            no = no.antecessor
        
    def __iter__(self):
        return iter(self.__passos)
    
    def __getitem__(self, index):
        return self.__passos[index]