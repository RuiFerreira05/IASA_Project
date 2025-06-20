from pee.mec_proc.procura_grafo import ProcuraGrafo
from pee.melhor_prim.fronteira_prioridade import FronteiraPrioridade

# A ProcuraMelhorPrim é uma procura que explora os nós com
# menor custo primeiro, utilizando uma lista de prioridade.
class ProcuraMelhorPrim(ProcuraGrafo):
    
    # A ProcuraMelhorPrim utiliza uma fronteira de prioridade
    # para armazenar os nós a serem explorados.
    # A prioridade é dada pelo avaliador, que é passado como
    # argumento para o seu construtor.
    def __init__(self, avaliador):
        super().__init__(FronteiraPrioridade(avaliador))
        self._avaliador = avaliador
    
    # Manter o Nó se o estado deste já não existe dentro do dict
    # de explorados, ou se o custo do nó for menor que o custo do nó
    # já existente no dict de explorados.
    def _manter(self, no):
        if no.estado in self._explorados:
            self.estados_repetidos += 1
                
        return no.estado not in self._explorados or \
            no.custo < self._explorados[no.estado].custo