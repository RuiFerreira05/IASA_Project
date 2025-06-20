class ControloReact:
    
    def __init__(self, comportamento):
        self.__comportamento = comportamento

    # ControloReact vai processar uma percepção com base 
    # no comportamento que lhe foi passado, retornando a
    # ação adequada a esse comportamento
    def processar(self, percepcao):
        return self.__comportamento.activar(percepcao)