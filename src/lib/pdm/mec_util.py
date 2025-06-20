class MecUtil:
    
    def __init__(self, modelo, gama, delta_max):
        self.__modelo = modelo
        self.__delta_max = delta_max
        self.__gama = gama
    
    
    def utilidade(self):
        """
        Retorna a utilidade de cada estado do modelo
        dado um determinado gama e delta_max
        """
        # Associa os métodos do modelo a variáveis locais
        # para facilitar a leitura do código
        S, A = self.__modelo.S, self.__modelo.A
        
        U = {s : 0 for s in S()}
        
        # Age como um do-while dado a condição de saida
        # ser no final do ciclo
        while True:
            U_ant = U.copy()
            delta = 0
            for s in S():
                # Gera a utilidade de cada acção 'a' no estado 's' e aplica
                # a função max para obter a acção com maior utilidade
                U[s] = max([self.util_accao(s, a, U_ant) for a in A(s)], 
                           default=0)
                
                # variação da utilidade desde o estado anterior até ao estado atual
                # se for maior que o delta atual, atualiza este
                delta = max(delta, abs(U[s] - U_ant[s]))
                
            # Condição de saida do ciclo
            if delta <= self.__delta_max:
                break
            
        return U
    
    def util_accao(self, s, a, U):
        """
        Retorna a utilidade da acção 'a' no estado 's'
        dado um determinado 'U' que representa a utilidade
        de cada estado
        """
        T, R, suc = self.__modelo.T, self.__modelo.R, self.__modelo.suc
        
        return sum([T(s, a, sn) * (R(s, a, sn) + self.__gama * U[sn]) 
                    for sn in suc(s, a)])