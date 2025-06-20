from pee.mec_proc.fronteira import Fronteira


class FronteiraLIFO(Fronteira):
    
    def inserir(self, no):
        # Last in First out
        self._nos.insert(0, no)