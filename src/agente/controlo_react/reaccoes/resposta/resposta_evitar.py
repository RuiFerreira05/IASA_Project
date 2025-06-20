from ecr.resposta import Resposta
from sae.agente.rodar import Rodar


class RespostaEvitar(Resposta):
        
    # Roda para a direita quando encontra um obstáculo à sua frente
    def activar(self, percepcao, intensidade):
        direccao_atual = percepcao.direccao
        if percepcao.contacto_obst(direccao_atual):
            self._accao = Rodar(direccao_atual.rodar())
            return super().activar(percepcao, intensidade)