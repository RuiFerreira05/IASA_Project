from pee.mec_proc.fronteira import Fronteira
import heapq

# A fronteira de prioridade é uma fronteira que
# armazena os nós em uma lista de prioridade (heapq).
# A prioridade é dada pelo avaliador e é "set" no método inserir.
# Heapq é uma representação de uma fila de prioridade, onde o menor
# elemento é sempre o primeiro a ser removido.
class FronteiraPrioridade(Fronteira):
    
    def __init__(self, avaliador):
        self.__avaliador = avaliador
        
    def inserir(self, no):
        no.prioridade = self.__avaliador.prioridade(no)
        # heappush insere o nó na lista de prioridade
        # de acordo com a sua prioridade.
        heapq.heappush(self._nos, no)
        
    def remover(self):
        # heappop remove o nó com a menor prioridade
        # da lista de prioridade, e retorna-o.
        # (isto é, o nó no indice 0 da lista de prioridade).
        return heapq.heappop(self._nos)