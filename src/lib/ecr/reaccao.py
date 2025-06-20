from ecr.comportamento import Comportamento


class Reaccao(Comportamento):
# Pelas regras da naming convention de python, a classe 
# deve ser escrita em PascalCase, com o nome dos modulos 
# em snake_case
    
    def __init__(self, estimulo, resposta):
        # Construtor das classes é definido com "__init__"
        # Todas as funções que devem ser métodos da classe 
        # começam a sua lista de parametros com uma instancia 
        # dessa classe ("self")
        
        self.__estimulo = estimulo
        # "__"(double underscore) significa um atributo privado
        self.__resposta = resposta
        #  "_"(single underscore) significa protegido
        
    def activar(self, percepcao):
        intensidade = self.__estimulo.detectar(percepcao)
        if intensidade > 0:
            return self.__resposta.activar(percepcao, intensidade)
        # Por omissão (falta de return) todas as funções python retornam "None"