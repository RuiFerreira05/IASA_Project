from pdm.pdm import PDM
from plan.modelo.modelo_pdm_plan import ModeloPDMPlan
from plan.modelo.modelo_plan import ModeloPlan
from plan.plan_pdm.plano_pdm import PlanoPDM
from plan.planeador import Planeador


class PlaneadorPDM(Planeador):
    """
    Planeador baseado em um Processo de Decisão de Markov (PDM).
    Utiliza o modelo de PDM para gerar planos que maximizam a utilidade esperada
    de um conjunto de objetivos, considerando um fator de desconto gama e um delta máximo.
    (Aqui com gama = 0.85 e delta_max = 1)
    """
    
    def __init__(self, gama = 0.85, delta_max = 1):
        self.gama = gama
        self.delta_max = delta_max
        
    def planear(self, modelo_plan: ModeloPlan, objectivos):
        modelo_pdm_plan = ModeloPDMPlan(modelo_plan, objectivos)
        pdm = PDM(modelo_pdm_plan, self.gama, self.delta_max)
        utilidade, politica = pdm.resolver()
        return PlanoPDM(utilidade, politica)