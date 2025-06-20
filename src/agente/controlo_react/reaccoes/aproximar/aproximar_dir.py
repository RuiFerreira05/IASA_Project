from agente.controlo_react.reaccoes.aproximar.estimulo_alvo import EstimuloAlvo
from agente.controlo_react.reaccoes.resposta.resposta_mover import RespostaMover
from ecr.reaccao import Reaccao


class AproximarDir(Reaccao):
    
    def __init__(self, direccao):
        super().__init__(
            EstimuloAlvo(direccao),     # Estimulo
            RespostaMover(direccao)     # Resposta
            )