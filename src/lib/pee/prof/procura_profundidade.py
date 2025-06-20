from pee.mec_proc.mecanismo_procura import MecanismoProcura
from pee.prof.fronteira_lifo import FronteiraLIFO

# A procura em profundidade consiste em explorar os
# nós mais recentes primeiros (Implemnentação LIFO), 
# explorando ao maximo cada ramo até que seja encontrada
# uma solução ou que não haja mais nós a expandir.
class ProcuraProfundidade(MecanismoProcura):
    
    def __init__(self):
        super().__init__(FronteiraLIFO())