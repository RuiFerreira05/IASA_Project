from pee.melhor_prim.aval.avaliador_heur import AvaliadorHeur


class AvaliadorAA(AvaliadorHeur):
    
    # custo do nó + heurística do estado do nó
    # prioridade = g(n) + h(n)
    def prioridade(self, no):
        return self.heuristica.h(no.estado) + no.custo