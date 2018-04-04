#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Usando Numpy para operações em matrizes
import numpy as np

# Essa função retorna o grau de qualquer vértice dado o índice
def grauParaIndice(indice, board):
    color = board[indice][indice]
    sum = np.sum(board[indice]) - color
    return sum

# Essa função retorna a cor de qualquer vértice dado o índice
# Por ser baseado em Matrizes, ele apenas busca na coluna e linha com o valor do índice
def corParaIndice(indice, board):
    return board[indice][indice]

# Essa função apenas verifica se a matriz inteira está colorida, comparando os valores dos nós com 0
def allColored(size, board):
    for index in range(0, size * size):
        if board[index][index] == 0:
            return False
    return True

# Essa função retorna a saturação: Quantidade de cores diferentes nos vizinhos de um nó
def saturacaoParaIndice(indice, board):

    # Foi utilizado um set para armazenar as cores sem repetição
    colorSet = set()

    for index in range(0, size * size):
        # Ela percorre todo o array, portanto precisa verificar se o índice atual não é o indice para o qual buscamos a saturação
        if index == indice:
            continue

        # Ao utilizar matrizes, um vértice é vizinho de outro caso o valor da matriz em seus índices seja 1
        if board[indice][index] == 1 and board[index][index] != 0:
            colorSet.add(corParaIndice(index, board))

    return (len(colorSet), colorSet)


# Essa função retorna a incidencia para um vértice: Quantidade de vizinhos coloridos
def incidenciaParaIndice(indice_buscado, board):

    contador_de_indice = 0
    for index in range(0, size * size):
        # Como anteriormente é verificado se o indice atual não é o buscado
        if index == indice_buscado:
            continue

        # Ao utilizar matrizes, um vértice é vizinho de outro caso o valor da matriz em seus índices seja 1,
        # se tiver cor, ou seja for diferente de 0, o número de incidencia é aumentado
        if board[indice_buscado][index] == 1 and board[index][index] != 0:
            contador_de_indice += 1

    return contador_de_indice

def getSaturationFromBoard(boardToGet):
    saturation = []
    for index in range(0, size * size):
        satura, neighborColo = saturacaoParaIndice(index, boardToGet)

        saturation.append(satura)

    return list(reversed(np.argsort(saturation)))

def getIncidenceFromBoard(boardToGet):

    saturation = []
    for index in range(0, size * size):
        incidence = incidenciaParaIndice(index, boardToGet)

        saturation.append(incidence)

    return list(reversed(np.argsort(saturation)))

# Gera a matriz de adjacências
def generateBoard(size):
    array = np.zeros(shape=(size * size, size * size), dtype=int)

    # A matriz identidade é utilizada na formação da matriz de adjacências para o problema
    identity = np.identity(size, dtype=int)

    # A matriz identidade com zeros trocados por uns é utilizada também
    inverse_identity = np.identity(size, dtype=int)
    inverse_identity[inverse_identity > 0] = -1
    inverse_identity[inverse_identity > -1] = 1
    inverse_identity[inverse_identity < 1] = 0

    zeros = np.zeros(shape=(int(pow(size, 0.5)), int(pow(size, 0.5))), dtype=int)
    ones = np.zeros(shape=(int(pow(size, 0.5)), int(pow(size, 0.5))), dtype=int)
    ones[ones < 1] = 1

    # São utilizados blocos de 1's intercalados com 0's
    m31 = np.concatenate([ones, zeros, zeros])
    m32 = np.concatenate([zeros, ones, zeros])
    m33 = np.concatenate([zeros, zeros, ones])
    blocks = np.concatenate([m31, m32, m33], axis=1)

    # Esse é o formato da matriz de adjacências
    l1 = np.concatenate([inverse_identity, blocks, blocks, identity, identity, identity, identity, identity, identity], axis=1)
    l2 = np.concatenate([blocks, inverse_identity, blocks, identity, identity, identity, identity, identity, identity], axis=1)
    l3 = np.concatenate([blocks, blocks, inverse_identity, identity, identity, identity, identity, identity, identity], axis=1)

    l4 = np.concatenate([identity, identity, identity, inverse_identity, blocks, blocks, identity, identity, identity], axis=1)
    l5 = np.concatenate([identity, identity, identity, blocks, inverse_identity, blocks, identity, identity, identity], axis=1)
    l6 = np.concatenate([identity, identity, identity, blocks, blocks, inverse_identity, identity, identity, identity], axis=1)

    l7 = np.concatenate([identity, identity, identity, identity, identity, identity, inverse_identity, blocks, blocks], axis=1)
    l8 = np.concatenate([identity, identity, identity, identity, identity, identity, blocks, inverse_identity, blocks], axis=1)
    l9 = np.concatenate([identity, identity, identity, identity, identity, identity, blocks, blocks, inverse_identity], axis=1)

    return np.concatenate([l1, l2, l3, l4, l5, l6, l7, l8, l9])

def getSolutionFromMatrix(matrix):
    solution = []
    for index in range(0, size * size):
        solution.append(board[index][index])
    return np.array(solution).reshape((size, size))

# O problema inicial em forma de matriz
problema_inicial = [[0, 2, 0, 5, 0, 1, 0, 9, 0],
                    [8, 0, 0, 2, 0, 3, 0, 0, 6],
                    [0, 3, 0, 0, 6, 0, 0, 7, 0],
                    [0, 0, 1, 0, 0, 0, 6, 0, 0],
                    [5, 4, 0, 0, 0, 0, 0, 1, 9],
                    [0, 0, 2, 0, 0, 0, 7, 0, 0],
                    [0, 9, 0, 0, 3, 0, 0, 8, 0],
                    [2, 0, 0, 8, 0, 4, 0, 0, 7],
                    [0, 1, 0, 9, 0, 7, 0, 6, 0]]


initial_flatten = np.array(problema_inicial).flatten()
size = len(problema_inicial)

board = generateBoard(size)

# Essa função adiciona as cores que já vieram do modelo
for index, value in enumerate(initial_flatten):
    board[index][index] = value


# Este while mantem o loop enquanto todos os vértices não foram coloridos
while not allColored(size, board):

    # Estes são os índices dos vértices ordenados por incidencia
    incidenciaInverted = list(getIncidenceFromBoard(board))
    # Estes são os índices dos vértices ordenados por saturação
    saturationReversed = list(getSaturationFromBoard(board))

    # Estes são os índices dos vértices ordenados por incidencia e saturação para que o algoritmo Incident Degree Ordering funcione
    tuples = zip(incidenciaInverted, saturationReversed)
    tuples.sort(key=lambda tup: incidenciaParaIndice(int(tup[1]), board), reverse=True)
    tuples.sort(key=lambda tup: saturacaoParaIndice(int(tup[0]), board), reverse=True)

    for index, (value, saturation) in enumerate(tuples):

        # Recebe a cor para o índice atual e verifica se o vértice atual ainda não foi colorido
        corParaIndex = corParaIndice(value, board)
        if corParaIndex == 0:

            todasAsCores = {1, 2, 3, 4, 5, 6, 7, 8, 9}
            saturacao, coresUtilizadas = saturacaoParaIndice(value, board)
            incidencia = incidenciaParaIndice(value, board)

            # As cores possiveis são a diferença entre todas as cores e as cores que já foram utilizadas
            coresPossiveis = todasAsCores.difference(coresUtilizadas)


            if len(coresPossiveis) > 0:
                # Seta o valor do vértice na matriz como o primeiro valor possível
                board[value][value] = list(coresPossiveis)[0]

            break



# Gera uma matriz para exibir a solução do problema baseada nas diagonais da matriz principal
solution = getSolutionFromMatrix(board)
print(solution)






