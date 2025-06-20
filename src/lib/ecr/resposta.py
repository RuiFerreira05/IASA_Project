class Resposta:
    
    # accao irá ser uma instancia da classe Accao da biblioteca sae
    def __init__(self, accao):
        self._accao = accao
        
    # valor por omissão de intensidade é 0
    def activar(self, percepcao, intensidade=0):
        # Aqui é verificado especificamente se percepcao é diferente 
        # de None, dado que Percepcao pode assumir um valor de zero, 
        # considerado falsy para o python, e daí levando o código a não 
        # ser executado da forma que deve.
        if percepcao is not None: 
            self._accao.prioridade = intensidade
            return self._accao