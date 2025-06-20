
from agente.controlo_react.reaccoes.aproximar.aproximar_dir import AproximarDir
from ecr.prioridade import Prioridade
from sae.ambiente.direccao import Direccao


class AproximarAlvo(Prioridade):
    
    def __init__(self):
        
        super().__init__(
            # Gerador de uma lista (List comprehension) de instancias de AproximarDir com
            # todos os valores do Enum "Direccao"
            [AproximarDir(direccao) for direccao in Direccao]
        )