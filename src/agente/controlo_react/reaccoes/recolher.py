from agente.controlo_react.reaccoes.aproximar.aproximar_alvo import AproximarAlvo
from agente.controlo_react.reaccoes.evitar.evitar_obst import EvitarObst
from agente.controlo_react.reaccoes.explorar.explorar import Explorar
from agente.controlo_react.reaccoes.explorar.explorar_mem import ExplorarMem
from ecr.hierarquia import Hierarquia


class Recolher(Hierarquia):
    
    def __init__(self):
        super().__init__(
            # Instancia de AproximarAlvo em primeiro lugar dado Recolher
            # herdar de Hierarquia
            [AproximarAlvo(), EvitarObst(), ExplorarMem(), Explorar(0.7)]
        )