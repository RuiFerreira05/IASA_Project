from abc import abstractmethod

from pee.mec_proc.mecanismo_procura import MecanismoProcura

# A ProcuraGrafo é uma procura que evita ciclos infinitos aquando da
# exploracão dos nós, mantendo um registo dos nós já explorados.
class ProcuraGrafo(MecanismoProcura):
    
    def _iniciar_memoria(self):
        super()._iniciar_memoria()
        self._explorados = {}
    
    # Se for para manter nó, então memorizar nó como explorado
    # e adicionar nó à fronteira
    def _memorizar(self, no):
        if self._manter(no):
            self._explorados[no.estado] = no
            super()._memorizar(no)
    
    @abstractmethod
    def _manter(self, no):
        """"""