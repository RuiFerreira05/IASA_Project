from pee.melhor_prim.heuristica import Heuristica
import math

# Esta classe define a heurística de distância
# que apenas classifica uma heuristica com base na distância
# entre o estado actual do agente e o estado final
class HeurDist(Heuristica):
    
    def __init__(self, estado_final):
        self.__estado_final = estado_final
    
    def h(self, estado):
        # A qualidade da heurística é dada pela distância
        # entre o estado actual do agente e o estado final (Objetivo).
        return math.dist(estado.posicao, self.__estado_final.posicao)