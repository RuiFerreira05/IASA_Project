from pee.melhor_prim.aval.avaliador import Avaliador


class AvaliadorCustoUnif(Avaliador):
    
    def prioridade(self, no):
        return no.custo