from ecr.comportamento import Comportamento
from sae import Avancar, Rodar, Direccao
import random

class Explorar(Comportamento):
    def __init__(self, prob_rotacao):
        self.__prob_rotacao = prob_rotacao
        self.__direccoes = list(Direccao) # lista com as direções possíveis
    
    def activar(self, percepcao): # A perceção é ignorada
        movimento = random.random()
        if movimento < self.__prob_rotacao:
            direccao_aleatoria = random.choice(self.__direccoes) # Escolhe uma direção aleatória
            return Rodar(direccao_aleatoria)
        return Avancar() # Se não rodar, avança