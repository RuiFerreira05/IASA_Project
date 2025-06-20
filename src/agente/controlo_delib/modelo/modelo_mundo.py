from agente.controlo_delib.modelo.estado_agente import EstadoAgente
from agente.controlo_delib.modelo.operador_mover import OperadorMover
from plan.modelo.modelo_plan import ModeloPlan
from sae.ambiente.direccao import Direccao
import math

from sae.ambiente.elemento import Elemento

# Esta classe representa o modelo do mundo onde o agente será inserido.
# O modelo é atualizado com base em percepcoes.
class ModeloMundo(ModeloPlan):
    
    @property
    def alterado(self):
        return self.__alterado
    
    @property
    def elementos(self):
        return self.__elementos
    
    def __init__(self):
        self.estado_inicial = None # Propriedade adicionada para permitir ao agente retornar ao estado inicial.
        self.__estado = None
        self.__estados = []
        # É inicializada uma lista de OperadoresMover, um para cada direcção do Enum Direccao.
        self.__operadores = [OperadorMover(self, direccao) for direccao in Direccao]
        
        self.__elementos = {}
        self.__alterado = False
        
    def obter_estado(self):
        return self.__estado
    
    def obter_estados(self):
        return self.__estados
    
    def obter_operadores(self):
        return self.__operadores
    
    def obter_elemento(self, estado):
        # Retorna o elemento com base na posição do estado.
        # Se o estado não existir, retorna None (Por omissão, default=None).
        return self.__elementos.get(estado.posicao)
    
    def distancia(self, estado):
        # Retorna a distância entre o agente e o estado.
        return math.dist(self.__estado.posicao, estado.posicao)
    
    def actualizar(self, percepcao):
        self.__estado = EstadoAgente(percepcao.posicao)
        
        # Estado inicial é definido na primeira percepcao.
        if self.estado_inicial is None:
            self.estado_inicial = self.__estado
            
        # Atualizar propriedade alterado se os elementos do modelo do mundo forem diferentes dos da percepcao.
        self.__alterado = self.elementos != percepcao.elementos
        if self.__alterado:
            # Se o modelo do mundo foi alterado, atualiza os elementos e estados deste.
            self.__elementos = percepcao.elementos
            self.__estados = [EstadoAgente(posicao) for posicao in percepcao.posicoes]
    
    def mostrar(self, vista):
        for posicao, elemento in self.__elementos.items():
            if elemento in [Elemento.ALVO, Elemento.OBSTACULO]:
                vista.mostrar_elemento(posicao, elemento)
        vista.marcar_posicao(self.__estado.posicao)
        
    # permite a utilização do operador in para verificar se um estado existe no modelo do mundo.
    # Exemplo: if estado in modelo_mundo:
    def __contains__(self, estado):
        return estado in self.__estados