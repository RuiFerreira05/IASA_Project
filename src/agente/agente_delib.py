from agente.controlo_delib.controlo_delib import ControloDelib
from plan.plan_pee.planeador_pee import PlaneadorPEE
from sae.agente.agente import Agente
from sae.simulador import Simulador

# Agente Deliberativo
# O Agente Deliberativo é um agente que toma decisões com base
# em um modelo do mundo e um planeador, utilizando um mecanismo
# de deliberação para gerar objetivos e um planeador para
# determinar como alcançá-los.
class AgenteDelib(Agente):
    
    def __init__(self):
        super().__init__()
        planeador = PlaneadorPEE()
        self.__controlo = ControloDelib(planeador)
        
    def executar(self):
        percepcao = self._percepcionar()
        accao = self.__controlo.processar(percepcao)
        self.__controlo.mostrar(self.vista)
        self._actuar(accao)
        
# Função de teste do agente deliberativo
if __name__ == "__main__":
    agente = AgenteDelib()
    simulador = Simulador(4, agente, vista_modelo=True)
    simulador.executar()