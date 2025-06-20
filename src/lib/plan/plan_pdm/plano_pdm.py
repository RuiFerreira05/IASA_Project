from mod.estado import Estado
from mod.operador import Operador
from plan.plano import Plano


class PlanoPDM(Plano):
    """ 
    Representa um plano baseado em um Processo de Decisão de Markov (PDM).
    Esta classe é responsável por armazenar a utilidade e a política associada ao plano,
    e por fornecer métodos para obter ações com base em estados, e exibir o plano.
    """
    
    def __init__(self, utilidade, politica):
        self.__utilidade = utilidade
        self.__politica = politica
        
    def obter_accao(self, estado):
        if self.__politica:
            return self.__politica.get(estado)
    
    def mostrar(self, vista):
        if self.__politica:
            # mostrar utilidade
            for estado, valor in self.__utilidade.items():
                vista.mostrar_valor_posicao(estado.posicao, valor)
            # mostrar politica
            for estado, accao in self.__politica.items():
                vista.mostrar_vector(estado.posicao, accao.ang)