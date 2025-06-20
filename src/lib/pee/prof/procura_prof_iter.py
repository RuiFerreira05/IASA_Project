from pee.prof.procura_prof_lim import ProcuraProfLim

# A Procura em profundidade iterativa consiste em
# realizar uma procura em profundidade com um limite de profundidade
# máximo, e se não encontrar uma solução, aumentar o limite
class ProcuraProfIter(ProcuraProfLim):
    
    def procurar(self, problema, inc_prof = 1, limite_prof = 100):
        for profundidade in range(0, limite_prof + 1, inc_prof):
            self._prof_max = profundidade
            solucao = super().procurar(problema)
            if solucao:
                return solucao