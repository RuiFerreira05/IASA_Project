from agente.controlo_react.reaccoes.evitar.estimulo_obst import EstimuloObst
from agente.controlo_react.reaccoes.resposta.resposta_evitar import RespostaEvitar
from ecr.reaccao import Reaccao


class EvitarDir(Reaccao):
    
    def __init__(self, direccao):
        super().__init__(
            EstimuloObst(direccao),
            RespostaEvitar(direccao)
            )