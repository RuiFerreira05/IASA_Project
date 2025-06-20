from sae.ambiente.elemento import Elemento


# Esta classe é responsável por guardar a lógica de seleção de objetivos
class MecDelib:
    
    def __init__(self, modelo_mundo):
        self.__modelo_mundo = modelo_mundo

    def deliberar(self):
        # Deliberar baseia-se em gerar uma lista dos vários objétivos no modelo
        # do mundo, e retornar-los ordenados pela sua distância ao agente.
        # Para um mecanismo de deliberação que escolhe o objétivo mais próximo,
        # este apenas tem de obter o primeiro elemento da lista.
        # No entanto ao retornar a lista ordenada na sua totalidade, damos
        # liberdade ao agente deliberativo de os selecionar como quiser.
        objetivos = self.__gerar_objetivos()
        if objetivos:
            return self.__selecionar_objetivos(objetivos)
        
    def __gerar_objetivos(self):
        # Geração de uma lista por significado utilizando um gerador,
        # Começamos por obter todos os estados do modelo do mundo e adicionamos
        # à lista aqueles que são do tipo ALVO.
        return [estado for estado in self.__modelo_mundo.obter_estados()
                if self.__modelo_mundo.obter_elemento(estado) == Elemento.ALVO]
    
    def __selecionar_objetivos(self, objetivos):
        # Ordenamos os objetivos pela sua distancia
        objetivos.sort(key=self.__modelo_mundo.distancia)
        # e retornamos a nova lista ordenada, para o controle deliberativo poder
        # usar como quiser.
        return objetivos