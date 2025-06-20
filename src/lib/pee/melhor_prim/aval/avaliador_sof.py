from pee.melhor_prim.aval.avaliador_heur import AvaliadorHeur


class AvaliadorSof(AvaliadorHeur):
    
    # só a heurística do estado do nó
    # prioridade = h(n)
    def prioridade(self, no):
        return self.heuristica.h(no.estado)