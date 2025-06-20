from ecr.estimulo import Estimulo
from sae.ambiente.elemento import Elemento


class EstimuloAlvo(Estimulo):
    
    def __init__(self, direccao, gama = 0.9):
        self.__gama = gama
        self.__direccao = direccao
    
    def detectar(self, percepcao):
        elemento, distancia, _ = percepcao[self.__direccao]
        # gama^distancia retorna valores exponenciais conforme a distancia do alvo,
        # quão mais longe tiver, menor o valor da intensidade,
        # e vice versa.
        # "true if cond else false"
        intensidade =  self.__gama ** distancia if elemento == Elemento.ALVO else 0.0
        return intensidade