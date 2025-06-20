from matplotlib.pylab import f
from contagem.modelo.heuristica_de_contagem import HeuristicaDeContagem
from contagem.modelo.problema_contagem import ProblemaContagem
from pee.larg.procura_largura import ProcuraLargura
from pee.mec_proc import solucao
from pee.mec_proc.no import No
from pee.melhor_prim.procura_aa import ProcuraAA
from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim
from pee.melhor_prim.procura_sofrega import ProcuraSofrega
from pee.prof.procura_prof_iter import ProcuraProfIter
from pee.prof.procura_prof_lim import ProcuraProfLim
from pee.prof.procura_profundidade import ProcuraProfundidade


VALOR_INICIAL = 0
VALOR_FINAL = 20
INCREMENTOS = [5, 1, 5, 9, 7]

# VALOR_INICIAL = 0
# VALOR_FINAL = 9
# INCREMENTOS = [1, 2, -1]

problema = ProblemaContagem(VALOR_INICIAL, VALOR_FINAL, INCREMENTOS)

print("################ iter ###############")

# Procura em profundidade iterativa

mec_proc_iter = ProcuraProfIter(5)

solucao = mec_proc_iter.procurar(problema)

if solucao:
    print(f"Dimensão: {solucao.dimensao}")
    print(f"Custo: {solucao.custo}")
    # print("Passos:")
    # for passo in solucao:
    #     print(f"Estado: {passo.estado.valor}")
    #     print(f"Operador: {passo.operador.incremento}")
    print("Operadores:" + str([passo.operador.incremento for passo in solucao])) 
    print(f'Nós processados: {mec_proc_iter.nos_processados}')
    print(f'Nós memorizados: {mec_proc_iter.nos_memorizados}')	
    
# Dimensão: 3
# Custo: 147
# Operadores:[7, 7, 7]
# Nós processados: 16
# Nós memorizados: 16
    
print("############### lim ################")

# Procura em profundidade com limite de profundidade

mec_proc_lim = ProcuraProfLim(5)

solucao = mec_proc_lim.procurar(problema)

if solucao:
    print(f"Dimensão: {solucao.dimensao}")
    print(f"Custo: {solucao.custo}")
    # print("Passos:")
    # for passo in solucao:
    #     print(f"Estado: {passo.estado.valor}")
    #     print(f"Operador: {passo.operador.incremento}")
    print("Operadores:" + str([passo.operador.incremento for passo in solucao])) 
    print(f'Nós processados: {mec_proc_lim.nos_processados}')
    print(f'Nós memorizados: {mec_proc_lim.nos_memorizados}')
    
# Dimensão: 3
# Custo: 147
# Operadores:[7, 7, 7]
# Nós processados: 16
# Nós memorizados: 16
    
print("############### prof ################")

# Procura em profundidade sem limite de profundidade

mec_proc_prof = ProcuraProfundidade()

solucao = mec_proc_prof.procurar(problema)

if solucao:
    print(f"Dimensão: {solucao.dimensao}")
    print(f"Custo: {solucao.custo}")
    # print("Passos:")
    # for passo in solucao:
    #     print(f"Estado: {passo.estado.valor}")
    #     print(f"Operador: {passo.operador.incremento}")
    print("Operadores:" + str([passo.operador.incremento for passo in solucao])) 
    print(f'Nós processados: {mec_proc_prof.nos_processados}')
    print(f'Nós memorizados: {mec_proc_prof.nos_memorizados}')
    
# Dimensão: 3
# Custo: 147
# Operadores:[7, 7, 7]
# Nós processados: 16
# Nós memorizados: 16
    
print("################ larg ###############")

# Procura em largura

mec_proc_larg = ProcuraLargura()

solucao = mec_proc_larg.procurar(problema)

if solucao:
    print(f"Dimensão: {solucao.dimensao}")
    print(f"Custo: {solucao.custo}")
    # print("Passos:")
    # for passo in solucao:
    #     print(f"Estado: {passo.estado.valor}")
    #     print(f"Operador: {passo.operador.incremento}")
    print("Operadores:" + str([passo.operador.incremento for passo in solucao])) 
    print(f'Nós processados: {mec_proc_larg.nos_processados}')
    print(f'Nós memorizados: {mec_proc_larg.nos_memorizados}')
    
# Dimensão: 3
# Custo: 187
# Operadores:[5, 9, 9]
# Nós processados: 246
# Nós memorizados: 246
    
print("############## unif #################")


# Procura com custo uniforme

mec_proc_unif = ProcuraCustoUnif()

solucao = mec_proc_unif.procurar(problema)

if solucao:
    print(f"Dimensão: {solucao.dimensao}")
    print(f"Custo: {solucao.custo}")
    # print("Passos:")
    # for passo in solucao:
    #     print(f"Estado: {passo.estado.valor}")
    #     print(f"Operador: {passo.operador.incremento}")
    print("Operadores:" + str([passo.operador.incremento for passo in solucao])) 
    print(f'Nós processados: {mec_proc_unif.nos_processados}')
    print(f'Nós memorizados: {mec_proc_unif.nos_memorizados}')
    print(f'Estados repetidos: {mec_proc_unif.estados_repetidos}')

# Dimensão: 20
# Custo: 20
# Operadores:[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# Nós processados: 101
# Nós memorizados: 82
# Estados repetidos: 72
    
print("############### sof ################")

# Procura sofrega com heuristica de contagem

mec_proc_sofrega = ProcuraSofrega()

solucao = mec_proc_sofrega.procurar(problema, HeuristicaDeContagem(VALOR_FINAL))

if solucao:
    print(f"Dimensão: {solucao.dimensao}")
    print(f"Custo: {solucao.custo}")
    # print("Passos:")
    # for passo in solucao:
    #     print(f"Estado: {passo.estado.valor}")
    #     print(f"Operador: {passo.operador.incremento}")
    print("Operadores:" + str([passo.operador.incremento for passo in solucao])) 
    print(f'Nós processados: {mec_proc_sofrega.nos_processados}')
    print(f'Nós memorizados: {mec_proc_sofrega.nos_memorizados}')
    print(f'Estados repetidos: {mec_proc_sofrega.estados_repetidos}')
    
# Dimensão: 4
# Custo: 164
# Operadores:[9, 9, 1, 1]
# Nós processados: 21
# Nós memorizados: 18
# Estados repetidos: 4
    
print("############### a* ################")

# Procura A* com heuristica de contagem

mec_proc_aa = ProcuraAA()

solucao = mec_proc_aa.procurar(problema, HeuristicaDeContagem(VALOR_FINAL))

if solucao:
    print(f"Dimensão: {solucao.dimensao}")
    print(f"Custo: {solucao.custo}")
    # print("Passos:")
    # for passo in solucao:
    #     print(f"Estado: {passo.estado.valor}")
    #     print(f"Operador: {passo.operador.incremento}")
    print("Operadores:" + str([passo.operador.incremento for passo in solucao])) 
    print(f'Nós processados: {mec_proc_aa.nos_processados}')
    print(f'Nós memorizados: {mec_proc_aa.nos_memorizados}')
    print(f'Estados repetidos: {mec_proc_aa.estados_repetidos}')

# Dimensão: 20
# Custo: 20
# Operadores:[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# Nós processados: 101
# Nós memorizados: 82
# Estados repetidos: 72