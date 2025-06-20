from pee.larg.fronteira_fifo import FronteiraFIFO
from pee.mec_proc.mecanismo_procura import MecanismoProcura

# A procura em largura consiste em explorar os
# nós mais antigos primeiro (Implemnentação FIFO),
# explorando ao maximo cada nivel de procura, até que
# seja encontrada uma solução ou que não haja mais nós a expandir.
class ProcuraLargura(MecanismoProcura):
    
    def __init__(self):
        super().__init__(FronteiraFIFO())