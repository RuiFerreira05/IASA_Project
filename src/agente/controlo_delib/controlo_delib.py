from agente.controlo_delib.mec_delib import MecDelib
from agente.controlo_delib.modelo.modelo_mundo import ModeloMundo

# Esta classe é responsável por implementar o modelo deliberativo num agente,
# deliberando sobre um modelo interno do mundo, gerando objetivos com ajuda de um
# mecanismo de deliberação, planeando como alcançar esses objetivos com ajuda de um planeador,
# e executando o plano gerado.
class ControloDelib:
    
    def __init__(self, planeador):
        self.__planeador = planeador
        self.__modelo_mundo = ModeloMundo()
        self.__mec_delib = MecDelib(self.__modelo_mundo)
        self.__objectivos = None
        self.__plano = None
    
    # Processo de tomada de decisão e Acção do agente.
    def processar(self, percepcao):
        # Observa o mundo, gera percepcoes e actualiza o modelo do mundo com base nestas percepcoes.
        self.__assimilar(percepcao)
        if self.__reconsiderar():
            # Se reconsiderar, então delibera sobre o seu modelo, gerando objetivos (raciocinio sobre fins)
            self.__deliberar()
            # e planeia como chegar a estes (raciocinio sobre meios).
            self.__planear()
        return self.__executar()
    
    def __assimilar(self, percepcao):
        # Assimilar baseia-se em atualizar o modelo interno do mundo com base numa percepcao.
        self.__modelo_mundo.actualizar(percepcao)
    
    def __reconsiderar(self):
        # Reconsiderar consiste em verificar se o modelo do mundo foi alterado, para que, caso esta condição
        # se verifique, o agente delibere novamente sobre este, possivelmente alterando o seu plano.
        # Se não existir um plano, o agente deve também reconsiderar, para poder gerar um novo plano.
        return self.__modelo_mundo.alterado or self.__plano is None
    
    def __deliberar(self):
        # Deliberar consiste em gerar uma lista de objectivos que o agente deve alcançar,
        # ordenados conforme a sua distancia a este.
        self.__objectivos = self.__mec_delib.deliberar()
    
    def __planear(self):
        # Planear consiste em gerar uma sequencia de accoes (plano) que o agente
        # deve seguir para alcançar os objectivos deliberados.
        # Se não existirem objectivos, o agente não tem nada a planear.
        if self.__objectivos:
            self.__plano = self.__planeador.planear(self.__modelo_mundo, self.__objectivos)
        else:
            # self.__plano = None
            
            # Nesta alteração, o agente irá retornar ao estado inicial do modelo do mundo
            # caso não existam mais objectivos. O estado inicial é guardado no modelo do mundo
            self.__plano = self.__planeador.planear(self.__modelo_mundo, [self.__modelo_mundo.estado_inicial])

    
    def __executar(self):
        # Executar consiste em executar a próxima acção do plano, se este existir.
        if self.__plano:
            estado = self.__modelo_mundo.obter_estado()
            operador = self.__plano.obter_accao(estado)
            if operador:
                return operador.accao
            else:
                self.__plano = None
    
    def mostrar(self, vista):
        # Mostrar consiste em mostrar o modelo do mundo, os objectivos e o plano na Interface gráfica.
        vista.limpar()
        self.__modelo_mundo.mostrar(vista)
        if self.__plano:
            self.__plano.mostrar(vista)
        if self.__objectivos:
            for objectivo in self.__objectivos:
                vista.marcar_posicao(objectivo.posicao)