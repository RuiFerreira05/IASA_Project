from pee.prof.procura_profundidade import ProcuraProfundidade


class ProcuraProfLim(ProcuraProfundidade):
    
    def __init__(self, prof_max = 10):
        super().__init__()
        self._prof_max = prof_max

    def _expandir(self, problema, no):
        if no.profundidade < self._prof_max:
            # Se a profundidade do nó for menor que a profundidade máxima,
            # expande o nó normalmente
            return super()._expandir(problema, no)
        else:
            # Se a profundidade do nó for maior ou igual à profundidade máxima,
            # não expande o nó e retorna uma lista vazia
            return []