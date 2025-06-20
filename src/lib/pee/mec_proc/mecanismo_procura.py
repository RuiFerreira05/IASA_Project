from abc import ABC

from pee.mec_proc.no import No
from pee.mec_proc.solucao import Solucao

# Esta classe representa um mecanismo de procura que
# explora opções possiveis através de uma simulação prospectiva.
class MecanismoProcura(ABC):
    
    @property
    def nos_processados(self):
        return No.nos_criados
        
    @property
    def nos_memorizados(self):
        return No.nos_maximos
    
    def __init__(self, fronteira):
        self._fronteira = fronteira
        self.estados_repetidos = 0
        
    
    def _iniciar_memoria(self):
        self._fronteira.iniciar()
    
    def _memorizar(self, no):
        self._fronteira.inserir(no)
    
    # Procura em profundidade, escolhendo expandir os nós
    # mais recentes primeiro.
    # Esta estrategia é mais eficiente em termos de memória 
    # quando comparada com a procura em largura.
    def procurar(self, problema):
        self._iniciar_memoria()
        fronteira = self._fronteira
        no = No(problema.estado_inicial)
        self._memorizar(no)
        while not fronteira.vazia:
            no = fronteira.remover()
            if problema.objetivo(no.estado):
                return Solucao(no)
            for no_sucessor in self._expandir(problema, no):
                self._memorizar(no_sucessor)
          
    # Expande o nó passado como argumento,
    # gerando os nós sucessores.
    def _expandir(self, problema, no):
        sucessores = list()
        estado = no.estado
        for operador in problema.operadores:
            estado_suc = operador.aplicar(estado)
            if estado_suc is not None:
                custo = no.custo + operador.custo(estado, estado_suc)
                no_sucessor = No(estado_suc, operador, no, custo)
                sucessores.append(no_sucessor)
        return sucessores