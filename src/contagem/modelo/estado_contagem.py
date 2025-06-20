from mod.estado import Estado


class EstadoContagem(Estado):
    
    def __init__(self, valor):
        self.valor = valor
    
    def id_valor(self):
        return self.valor