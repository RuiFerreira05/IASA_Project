from agente.controlo_react.reaccoes.evitar.evitar_dir import EvitarDir
from ecr.hierarquia import Hierarquia
from sae.ambiente.direccao import Direccao


class EvitarObst(Hierarquia):
    
    def __init__(self):
        super().__init__(
            [EvitarDir(direccao) for direccao in Direccao]
        )