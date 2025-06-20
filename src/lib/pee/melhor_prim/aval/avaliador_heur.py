from pee.melhor_prim.aval.avaliador import Avaliador


class AvaliadorHeur(Avaliador):
    
    @property
    def heuristica(self):
        return self._heuristica
    
    @heuristica.setter
    def heuristica(self, heuristica):
        self._heuristica = heuristica
    
    def __init__(self):
        self._heuristica = None