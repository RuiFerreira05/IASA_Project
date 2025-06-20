from agente.agente_delib import AgenteDelib
from agente.controlo_delib.controlo_delib import ControloDelib
from plan.plan_pdm.planeador_pdm import PlaneadorPDM
from sae.agente.agente import Agente
from sae.simulador import Simulador


class AgenteDelibPDM(Agente):
    """
    Agente Deliberativo baseado no Processo de Decisão de Markov (PDM).
    Este agente utiliza um mecanismo de deliberação para gerar objetivos
    e um planeador PDM para determinar como alcançá-los.
    """

    def __init__(self):
        super().__init__()
        # Gama aumentada para 0.95 para permitir ao agente
        # "ver" mais no futuro, este valor permite ao agente
        # resolver o ambiente 4 do simulador.
        # Dado a gama ser um valor exponencial, quanto maior
        # for, mais pesado será o processamento do agente.
        planeador = PlaneadorPDM(0.95)
        self.__controlo = ControloDelib(planeador)

    def executar(self):
        percepcao = self._percepcionar()
        accao = self.__controlo.processar(percepcao)
        self.__controlo.mostrar(self.vista)
        self._actuar(accao)
        
# teste
if __name__ == "__main__":
    agente = AgenteDelibPDM()
    simulador = Simulador(4, agente, vista_modelo=True)
    simulador.executar()