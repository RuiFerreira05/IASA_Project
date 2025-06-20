from pee.mec_proc.fronteira import Fronteira


class FronteiraFIFO(Fronteira):
    
    def inserir(self, no):
        # First in First out
        self._nos.append(no)