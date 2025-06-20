from agente.controlo_react.controlo_react import ControloReact
from agente.controlo_react.reaccoes.explorar.explorar import Explorar
from agente.controlo_react.reaccoes.recolher import Recolher
from sae.agente.agente import Agente

# O Agente reactivo é um agente que reage de acordo com o 
# ambiente que o rodeia, percepcionando e decidindo como atuar 
# baseando-se no seu comportamento.
class AgenteReact(Agente):
    
    def __init__(self):
        super().__init__()
        # self.__comportamento = Explorar(0.7)
        self.__comportamento = Recolher()
        self.controlo = ControloReact(self.__comportamento)
    
    def executar(self):
        # O Agente percepciona o ambiente, processa este, 
        # e actua de acordo com o seu comportamento
        percepcao = self._percepcionar()
        accao = self.controlo.processar(percepcao)
        self._actuar(accao)