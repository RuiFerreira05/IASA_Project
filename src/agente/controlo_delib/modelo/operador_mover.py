from turtle import pos
from agente.controlo_delib.modelo.estado_agente import EstadoAgente
from mod.operador import Operador
from sae.agente.accao import Accao
import math

class OperadorMover(Operador):

    @property
    def ang(self):
        return self.__ang

    @property
    def accao(self):
        return self.__accao    
    
    def __init__(self, modelo_mundo, direccao):
        self.__modelo_mundo = modelo_mundo
        self.__direccao = direccao
        self.__ang = direccao.value
        self.__accao = Accao(direccao)

    def __translacao(self, posicao, dist_deslocacao, ang_deslocacao):
        x, y = posicao # Desconstrução automática do tuplo
        dx = round(dist_deslocacao * math.cos(ang_deslocacao))
        dy = - round(dist_deslocacao * math.sin(ang_deslocacao))
        nova_posicao = x + dx, y + dy
        return nova_posicao
                

    def aplicar(self, estado):
        nova_posicao = self.__translacao(estado.posicao, self.__accao.passo, self.__ang)
        novo_estado = EstadoAgente(nova_posicao)
        if novo_estado in self.__modelo_mundo:
            return novo_estado

    # Obtem o custo de mover de um estado para outro
    # O custo tem um minimo de 1 e equivale à distância entre os dois estados
    def custo(self, estado, estado_suc):
        return max(1, math.dist(estado.posicao, estado_suc.posicao))