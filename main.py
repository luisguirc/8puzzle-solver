# Luis Guilherme Redigolo Crosselli RA 11201920964

import math
import copy

estados_gerados = 0

def solucionar_8puzzle(estado_inicial):
    
    def prepara_array_e_encontra_zero(estado):
        # estrutura do estado: [[1a linha],[2a linha],[3a linha],
            # profundidade, acao_tomada_para_chegar_no_estado, pai, posicao_do_zero]
        estado.append(0)
        estado.append(0)
        estado.append(0)
        indices_zero = []
        for row in range(3):
            if(estado[row].count(0)):
                indices_zero = [row, estado[row].index(0)]
        estado_inicial.append(indices_zero)
        
    def troca_posicao_zero(estado_atual, novo_estado):
      novo_estado[estado_atual[6][0]][estado_atual[6][1]] = estado_atual[novo_estado[6][0]][novo_estado[6][1]]
      novo_estado[novo_estado[6][0]][novo_estado[6][1]] = 0

    def incrementa_estados_gerados():
        global estados_gerados
        estados_gerados += 1
        
    def expande_estado(estado_atual, vizinhanca):
        estados_expandidos.append(estado_atual[0:3])
        
        for acao in acoes:
            novo_estado = copy.deepcopy(estado_atual) #usando deepcopy para poder colocar a profundidade no fim do array
            novo_estado[3] = estado_atual[3] + 1 #aumentando a profundidade
            novo_estado[6][0] = estado_atual[6][0] + acoes[acao][0] #equivalente a novo_zero[0] = zero_atual[0] + acoes[acao][0]
            novo_estado[6][1] = estado_atual[6][1] + acoes[acao][1] # equivalente a novo_zero[1] = zero_atual[1] + acoes[acao][1]
            if(not((novo_estado[6][0] < 0 or novo_estado[6][0] > 2) or (novo_estado[6][1] < 0 or novo_estado[6][1] > 2))):
                troca_posicao_zero(estado_atual, novo_estado)
                novo_estado[4] = acao
                vizinhanca.append(novo_estado)
                novo_estado[5] = estado_atual #setando o pai dentro do novo estado
                incrementa_estados_gerados()
                
    def h(estado):
        """
        calcula a distancia de manhattan do estado
        """
        h = 0
        for i in range(3):
            for j in range(3):
                numero = estado[i][j]
                #if(numero != 0):
                linha_objetivo = math.floor((numero - 1)/3)
                if(numero%3 == 0):
                    coluna_objetivo = 2
                else:
                    coluna_objetivo = (numero%3 - 1)
                h_numero = abs(i - linha_objetivo) + abs(j - coluna_objetivo)
                h += h_numero
        return h

    def escolhe_prox_estado_atual_e_ordena_vizinhanca(vizinhanca):
        vizinhanca.sort(key=h) #ordena a vizinhanca do menor para o maior f
        novo_estado_atual = vizinhanca[0]
        vizinhanca = vizinhanca[1:]
        return novo_estado_atual

    def exclui_estados_ja_expandidos(vizinhanca):
        for estado in vizinhanca: #desconsidera o estado se ele ja foi expandido
            if(estados_expandidos.count(estado[0:3])):
                del vizinhanca[vizinhanca.index(estado)]

    def imprimir_estado(estado):
        print(estado[4])
        for row in estado[0:3]:
            print(row)
        print("-------------------------")
    
    def monta_historico(estado,historico_acoes):
        if(estado[4] == 0):
            historico_estados.append(estado)
            return
        else:
            historico_acoes.append(estado[4])
            historico_estados.append(estado)
            estado = estado[5]
            monta_historico(estado,historico_acoes)
        
    prepara_array_e_encontra_zero(estado_inicial)
    
    estado_atual = copy.deepcopy(estado_inicial)
    estado_final = [[1,2,3],[4,5,6],[7,8,0]]
    
    acoes = { "cima": [-1,0],
            "baixo": [1,0],
            "direita": [0,1],
            "esquerda": [0,-1]
            }
    
    vizinhanca = []
    historico_acoes = []
    estados_expandidos = []
    historico_estados = []

    # inicia a busca, expandindo o estado inicial
    vizinhanca.append(estado_atual)
    expande_estado(estado_atual, vizinhanca)

    print("=========================")
    print("----------Início---------")
    print("=========================")
    
    while((estado_atual[0:3] != estado_final[0:3])):
        exclui_estados_ja_expandidos(vizinhanca)
        estado_atual = escolhe_prox_estado_atual_e_ordena_vizinhanca(vizinhanca)
        expande_estado(estado_atual, vizinhanca)

    exclui_estados_ja_expandidos(vizinhanca)
    # estados_gerados = len(vizinhanca) + len(estados_expandidos) - 2 #ja que o primeiro é expandido e vai para a vizinhanca
    
    monta_historico(estado_atual,historico_acoes)
    historico_acoes = historico_acoes[::-1]

    historico_estados = historico_estados[::-1]
    for estado in historico_estados:
        imprimir_estado(estado)

    solucao = [estados_gerados, historico_acoes]
    
    print("=========================")
    print("Estados (nós) gerados: {}".format(solucao[0]))
    print("=========================")
    
    return solucao
    

estado_inicial = [[1,3,0],[5,6,4],[7,8,2]]
solucao = solucionar_8puzzle(estado_inicial)
print(solucao)
estados_gerados = 0

# =========================
# ----------Início---------
# =========================
# 0
# [1, 8, 2]
# [0, 4, 3]
# [7, 6, 5]
# -------------------------
# direita
# [1, 8, 2]
# [4, 0, 3]
# [7, 6, 5]
# -------------------------
# cima
# [1, 0, 2]
# [4, 8, 3]
# [7, 6, 5]
# -------------------------
# direita
# [1, 2, 0]
# [4, 8, 3]
# [7, 6, 5]
# -------------------------
# baixo
# [1, 2, 3]
# [4, 8, 0]
# [7, 6, 5]
# -------------------------
# baixo
# [1, 2, 3]
# [4, 8, 5]
# [7, 6, 0]
# -------------------------
# esquerda
# [1, 2, 3]
# [4, 8, 5]
# [7, 0, 6]
# -------------------------
# cima
# [1, 2, 3]
# [4, 0, 5]
# [7, 8, 6]
# -------------------------
# direita
# [1, 2, 3]
# [4, 5, 0]
# [7, 8, 6]
# -------------------------
# baixo
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 0]
# -------------------------
# =========================
# Estados (nós) gerados: 31
# =========================

# e o retorno da função é o seguinte array:
# [31, ['direita', 'cima', 'direita', 'baixo', 'baixo', 'esquerda', 'cima', 'direita', 'baixo']]

# seguindo a estrutura:
# [estados_gerados, caminho_da_solucao]