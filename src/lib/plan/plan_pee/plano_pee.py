from plan.plano import Plano

# Um plano em um Espaco de Estados é definido
# como uma sequencia de passos a realizar para
# chegar a um determinado objetivo.
class PlanoPEE(Plano):
    
    @property
    def dimensao(self):
        return self.__dimensao
    
    def __init__(self, solucao):
        self.__passos = [passo for passo in solucao]
        self.__dimensao = len(self.__passos)


    def obter_accao(self, estado):
        # Se existirem passos no plano, retira o primeiro passo
        # deste e verifica se o estado corresponde ao passo,
        # se sim, retorna o operador do passo.
        # por omissão retorna None.
        if self.__passos:
            passo = self.__passos.pop(0)
            if estado == passo.estado:
                return passo.operador
    
    def mostrar(self, vista):
        if self.__passos:
            for passo in self.__passos:
                vista.mostrar_vector(passo.estado.posicao, 
                                     passo.operador.ang)