from pee.melhor_prim.procura_aa import ProcuraAA
from plan.plan_pee.mod_prob.heur_dist import HeurDist
from plan.plan_pee.mod_prob.problema_plan import ProblemaPlan
from plan.plan_pee.plano_pee import PlanoPEE
from plan.planeador import Planeador

# O planeador funciona em essencia como a classe que junta
# O plano, o problema, a heuristica e o mecanismo de procura,
# permitindo assim a procura de um plano para o problema
class PlaneadorPEE(Planeador):
    
    def __init__(self):
        self.__mec_pee = ProcuraAA()
    
    # O planeador retorna um plano para o problema
    # alcançado através de um mecanismo de procura
    # em espaco de estados que utiliza uma heuristica
    # (HeurDist) e um problema (ProblemaPlan)
    def planear(self, modelo_plan, objectivos):
        estado_final = objectivos[0]
        problema = ProblemaPlan(modelo_plan, estado_final)
        heuristica = HeurDist(estado_final)
        solucao = self.__mec_pee.procurar(problema, heuristica)
        return PlanoPEE(solucao)