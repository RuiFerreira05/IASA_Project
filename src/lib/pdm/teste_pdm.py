from lib.pdm.modelo.modelo_pdm import ModeloPDM
from lib.pdm.pdm import PDM


class ModeloAmbiente7x1(ModeloPDM):
    """
    Esta classe representa um teste da resolução de um modelo com base em um Processo de Decisão de Markov (PDM).
    Este modelo é um ambiente 1D com 7 estados, onde, em cada estado, o agente pode mover-se para a esquerda ou para a direita.
    Os estados 1 e 7 são estados terminais, onde o agente não pode realizar mais ações (Representada como a probabilidade de 
    transição para qualquer estado vizinho ser igual a 0).
    A recompensa positiva é dada quando o agente transiciona do estado 6 para o estado 7.
    A recompensa negativa é dada quando o agente transiciona do estado 2 para o estado 1.
    O objetivo é maximizar a utilidade esperada do agente ao longo do tempo, considerando as recompensas e as transições de estado.
    
    Solução esperada:
    Utilidade: {1: 0, 2: 0.0625, 3: 0.125, 4: 0.25, 5: 0.5, 6: 1.0, 7: 0}
    Política: {2: '>', 3: '>', 4: '>', 5: '>', 6: '>'}
    """
    
    def __init__(self):
        # A boa convenção de python diz que variaveis devem ser
        # nomeadas com letras minusculas, mas tambem diz que
        # variaveis que representem variaveis matemáticas
        # e sejam constituidas por apenas uma letra, podem e devem ser
        # nomeadas com letras maiusculas.
        
        # lista de estados possiveis
        self.__S = [1, 2, 3, 4, 5, 6, 7]
        # lista de acções possiveis
        self.__A = ['<', '>']
        
        # Dicionário de transições possiveis entre estados
        # {(estado atual, ação, estado seguinte): probabilidade}
        # Dado este ambiente ser deterministico, a probabilidade de
        # transição entre estados é sempre 1 ou 0.
        self.__T = {
            (1, '<', 1): 0,
            (1, '>', 2): 0,
            (2, '<', 1): 1,
            (2, '>', 3): 1,
            (3, '<', 2): 1,
            (3, '>', 4): 1,
            (4, '<', 3): 1,
            (4, '>', 5): 1,
            (5, '<', 4): 1,
            (5, '>', 6): 1,
            (6, '<', 5): 1,
            (6, '>', 7): 1,
            (7, '<', 6): 0,
            (7, '>', 7): 0
        }
        
        self.__R = {
            (1, '<', 1): 0,
            (1, '>', 2): 0,
            (2, '<', 1): -1,
            (2, '>', 3): 0,
            (3, '<', 2): 0,
            (3, '>', 4): 0,
            (4, '<', 3): 0,
            (4, '>', 5): 0,
            (5, '<', 4): 0,
            (5, '>', 6): 0,
            (6, '<', 5): 0,
            (6, '>', 7): 1,
            (7, '<', 6): 0,
            (7, '>', 7): 0
        }
        
        self.__transicoes = {(s, a) : sn for (s, a, sn) in self.__T if s not in [1, 7]}
        
    def S(self):
        return self.__S
    
    def A(self, s):
        return self.__A if s not in [1, 7] else []
    
    def T(self, s, a, sn):
        return self.__T.get((s, a, sn))
    
    def R(self, s, a, sn):
        return self.__R.get((s, a, sn))
    
    def suc(self, s, a):
        sn = self.__transicoes.get((s, a))
        return [sn] if sn else []
    
if __name__ == '__main__':
    modelo_pdm = ModeloAmbiente7x1()
    pdm = PDM(modelo_pdm, 0.5, 0.0)
    utilidade, politica = pdm.resolver()
    print(f"\nUtilidade: {utilidade}")
    print(f"\nPolitica: {politica}")
        