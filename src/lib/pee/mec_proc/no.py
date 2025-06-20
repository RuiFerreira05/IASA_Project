# Classe Nó que representa um nó na árvore de procura.
# Esta classe é utilizada para armazenar o estado, o operador que gerou
# o nó, o antecessor (nó pai), o custo e a profundidade do nó.
# A classe também possui um atributo de prioridade que é utilizado
# para determinar a ordem de exploração dos nós na fronteira de prioridade.
# A classe possuí tambem atributos estáticos que guardam a contagem de nós
# criados e eliminados, com o objetivo de monitorizar o desempenho dos vários 
# algoritmos de procura.
class No:
    
    # Atributos estáticos da classe No.
    nos_criados = 0
    nos_eliminados = 0
    nos_maximos = 0
    
    @property
    def profundidade(self):
        return self.__profundidade
    
    @property
    def custo(self):
        return self.__custo
    
    @property
    def estado(self):
        return self.__estado
    
    @property
    def operador(self):
        return self.__operador
    
    @property
    def antecessor(self):
        return self.__antecessor
    
    @property
    def prioridade(self):
        return self.__prioridade
    
    # Setter para o atributo prioridade.
    @prioridade.setter
    def prioridade(self, prioridade):
        self.__prioridade = prioridade
        
    def __init__(self, estado, operador = None, antecessor = None, custo = 0):
        # O custo do nó é o custo do nó anterior + o custo do operador
        # que gerou este nó.
        self.__custo = custo
        # O estado é o estado da resolução do problema neste nó.
        self.__estado = estado
        # O operador é o operador que gerou este nó
        self.__operador = operador
        # O antecessor é o nó anterior que gerou este nó
        # (o nó pai na árvore de procura).
        self.__antecessor = antecessor
        # Prioridade é um atributo que será utilizado na fronteira de prioridade
        # para determinar a ordem de exploração dos nós.
        self.__prioridade = None
        # A profundidade do no é igual à profundidade do nó anterior + 1
        if antecessor is not None:
            self.__profundidade = antecessor.profundidade + 1
        else:
            self.__profundidade = 0
            No.nos_criados = 0
            No.nos_eliminados = 0
            No.nos_maximos = 0
        
        No.nos_criados += 1
        self.nos_memorizados = No.nos_criados - No.nos_eliminados
        if self.nos_memorizados > No.nos_maximos:
            No.nos_maximos = self.nos_memorizados
        
    # Método para comparar dois nós, baseado na sua prioridade.
    # Este método é utilizado pela fronteira de prioridade (heapq) para
    # determinar a ordem de inserção dos nós na lista de prioridade.
    def __lt__(self, outro_no):
        return self.prioridade < outro_no.prioridade
    
    def __del__(self):
        No.nos_eliminados += 1