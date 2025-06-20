from mod.problema import Problema

# ProblemaPlan é uma especialização de Problema
# iniciada no contrutor com um modelo de plano e 
# um estado final.
# O estado inicial e os operadores são obtidos
# através do modelo de plano
class ProblemaPlan(Problema):
    
    def __init__(self, modelo_plan, estado_final):
        super().__init__(modelo_plan.obter_estado(), 
                         modelo_plan.obter_operadores())
        self.__estado_final = estado_final
        
    def objetivo(self, estado):
        return estado == self.__estado_final