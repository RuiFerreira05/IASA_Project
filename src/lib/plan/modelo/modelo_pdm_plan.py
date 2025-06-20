from pdm.modelo.modelo_pdm import ModeloPDM
from plan.modelo.modelo_plan import ModeloPlan


class ModeloPDMPlan(ModeloPlan, ModeloPDM):
    """
    representa o modelo de um plano baseado em um 
    Processo de Decisão de Markov (PDM).
    """
    
    def __init__(self, modelo_plan, objectivos, rmax = 1000):
        self.__modelo_plan = modelo_plan
        self.__objectivos = objectivos
        self.__rmax = rmax
        
        self.__transicoes = {}
        for s in self.obter_estados():
            for a in self.obter_operadores():
                sn = a.aplicar(s)
                if sn:
                    self.__transicoes[(s, a)] = sn
    
    def obter_estado(self):
        return self.__modelo_plan.obter_estado()
    
    def obter_estados(self):
        return self.__modelo_plan.obter_estados()
    
    def obter_operadores(self):
        return self.__modelo_plan.obter_operadores()
    
    def S(self):
        return self.obter_estados()
    
    def A(self, s):
        return self.obter_operadores() if s not in self.__objectivos else []
    
    def T(self, s, a, sn):
        # Dado a lista de transições ser gerada a partir dos operadores e estados do modelo de plano,
        # não existirá uma transição inválida, daí não ser necessário verificar se sn é um estado válido.
        # para a condição (s, a) == sn.
        
        # Dado o ambiente ser determinístico, a probabilidade de transição é sempre 1 ou 0.
        return 1 if sn is not None else 0
    
    def R(self, s, a, sn):
        # Neste modelo, o agente não é penalizado por ações inválidas, dado
        # que estas não existem na simulação, daí, apenas será necessário
        # verificar se o estado seguinte é um objetivo e retornar a recompensa máxima
        # se for o caso.
        return self.__rmax if sn in self.__objectivos else 0
    
    def suc(self, s, a):
        sn = self.__transicoes.get((s, a))
        return [sn] if sn else []