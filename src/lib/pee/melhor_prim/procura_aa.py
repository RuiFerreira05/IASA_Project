from pee.melhor_prim.aval.avaliador_aa import AvaliadorAA
from pee.melhor_prim.procura_informada import ProcuraInformada


class ProcuraAA(ProcuraInformada):
    
    def __init__(self):
        super().__init__(AvaliadorAA())