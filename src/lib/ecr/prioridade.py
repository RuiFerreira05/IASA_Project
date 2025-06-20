from ecr.comport_comp import ComportComp

class Prioridade(ComportComp):
    
    # A classe "Prioridade" é uma subclasse de "ComportComp".
    # Dado que "ComportComp" contem um construtor, "Prioridade"
    # não precisa de um contrutor próprio.
    
    # A prioridade escolhe a ação com maior prioridade da lista de ações
    def seleccionar_accao(self, accoes):
        # lambda age como função não nomeada, unica ao instante em que é utilizada
        # Nesta situação, serve para retirar o valor de prioridade de cada accao
        return max(accoes, key=lambda accao: accao.prioridade)