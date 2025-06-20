from ecr.comport_comp import ComportComp

class Hierarquia(ComportComp):
    
    # A classe "Hierarquia" é uma subclasse de "ComportComp". 
    # Dado que "ComportComp" contem um construtor, "Hierarquia"
    # não precisa de um contrutor próprio.
    
    # A hierarquia escolhe a primeira ação da lista de ações
    def seleccionar_accao(self, accoes):
        return accoes[0]