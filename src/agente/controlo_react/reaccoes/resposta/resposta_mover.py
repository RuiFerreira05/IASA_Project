from ecr.resposta import Resposta
from sae.agente.accao import Accao


class RespostaMover(Resposta):
    
    # Move-se em frente (No contexto de aproximar, 
    # move-se na direção do obstaculo)
    def __init__(self, direccao):
        super().__init__(Accao(direccao))