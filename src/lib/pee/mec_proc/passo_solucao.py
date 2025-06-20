from dataclasses import dataclass

from mod.estado import Estado
from mod.operador import Operador

# Esta classe não se encontra conforme o modelo que esta implementação segue
# dado que as suas variaveis não são Read-Only, mas sim Read-Write.
@dataclass
class PassoSolucao:
    estado: Estado
    operador: Operador