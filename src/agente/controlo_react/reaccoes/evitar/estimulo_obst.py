from ecr.estimulo import Estimulo


class EstimuloObst(Estimulo):
    
    def __init__(self, direccao, intensidade = 1.0):
        self.__intensidade = intensidade
        self.__direccao = direccao
        
    # Agir caso houver contacto com obstaculo na 
    # direccao atual do agente
    def detectar(self, percepcao):
        return self.__intensidade if percepcao.contacto_obst(self.__direccao) else 0.0