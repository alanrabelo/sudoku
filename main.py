import numpy as np
import random


def grauParaIndice(indice, board):
    color = board[indice][indice]
    sum = np.sum(board[indice]) - color
    return sum


def corParaIndice(indice, board):
    return board[indice][indice]


def allColored(size, board):
    for index in range(0, size * size):
        if board[index][index] == 0:
            return False
    return True


# def saturacaoParaIndice2(indice, board):
#
#     colorSet = set()
#
#     for index, line in enumerate(board):
#         if index == indice:
#             continue
#
#         if board[index][indice] == 1 and line[index] != 0:
#             colorSet.add(line[index])
#
#     return (len(colorSet), colorSet)

def saturacaoParaIndice(indice, board):
    colorSet = set()

    for index in range(0, size * size):
        if index == indice:
            continue

        if board[indice][index] == 1 and board[index][index] != 0:
            colorSet.add(corParaIndice(index, board))

    return (len(colorSet), colorSet)

def getSaturationFromBoard(boardToGet):
    saturation = []
    for index in range(0, size * size):
        satura, neighborColo = saturacaoParaIndice(index, boardToGet)

        if len(neighborColo) == size:
            print("its impossible to solve")
        saturation.append(satura)

    return list(reversed(np.argsort(saturation)))

def getIncidenceFromBoard(boardToGet):
    saturation = []
    for index in range(0, size * size):
        satura, neighborColo = saturacaoParaIndice(index, boardToGet)

        if len(neighborColo) == size:
            print("its impossible to solve")
        saturation.append(satura)

    return list(reversed(np.argsort(saturation)))

center = [3,8,5,7,2,6,1,4,9]

initial = [[0, 2, 0, 5, 0, 1, 0, 9, 0],
           [8, 0, 0, 2, 0, 3, 0, 0, 6],
           [0, 3, 0, 0, 6, 0, 0, 7, 0],
           [0, 0, 1, 0, 0, 0, 6, 0, 0],
           [5, 4, 0, 0, 0, 6, 0, 1, 9],
           [0, 0, 2, 0, 0, 0, 7, 0, 0],
           [0, 9, 0, 0, 3, 0, 0, 8, 0],
           [2, 0, 0, 8, 0, 4, 0, 0, 7],
           [0, 1, 0, 9, 0, 7, 0, 6, 0]]

initial_center = [[0, 2, 0, 5, 0, 1, 0, 9, 0],
                  [8, 0, 0, 2, 0, 3, 0, 0, 6],
                  [0, 3, 0, 0, 6, 0, 0, 7, 0],
                  [0, 0, 1, 0, 8, 0, 6, 0, 0],
                  [5, 4, 0, 0, 0, 0, 0, 1, 9],
                  [0, 0, 2, 0, 0, 0, 7, 0, 0],
                  [0, 9, 0, 0, 3, 0, 0, 8, 0],
                  [2, 0, 0, 8, 0, 4, 0, 0, 7],
                  [0, 1, 0, 9, 0, 7, 0, 6, 0]]

initial_original = [[0, 2, 0, 5, 0, 1, 0, 9, 0],
           [8, 0, 0, 2, 0, 3, 0, 0, 6],
           [0, 3, 0, 0, 6, 0, 0, 7, 0],
           [0, 0, 1, 0, 0, 0, 6, 0, 0],
           [5, 4, 0, 0, 0, 0, 0, 0, 9],
           [0, 0, 0, 0, 0, 0, 7, 0, 0],
           [0, 9, 0, 0, 3, 0, 0, 8, 0],
           [2, 0, 0, 8, 0, 4, 0, 0, 7],
           [0, 1, 0, 9, 0, 7, 0, 6, 0]]

easy = [[4, 2, 0, 0, 0, 7, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 7, 1, 6, 0, 0, 0, 9],
        [0, 0, 2, 0, 5, 0, 0, 8, 0],
        [9, 8, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 9, 1],
        [7, 0, 1, 9, 0, 0, 0, 0, 2],
        [5, 0, 0, 0, 2, 0, 0, 3, 6]]

initial_flatten = np.array(initial_center).flatten()

size = len(initial)

def numberOfUsageOfColor(color, board):

    usages = 0

    for index in range(0,size*size):
        value = board[index][index]
        if value == color:
            usages += 1

    return usages

array = np.zeros(shape=(size * size, size * size), dtype=int)

identity = np.identity(size, dtype=int)

inverse_identity = np.identity(size, dtype=int)
inverse_identity[inverse_identity > 0] = -1
inverse_identity[inverse_identity > -1] = 1
inverse_identity[inverse_identity < 1] = 0

zeros = np.zeros(shape=(int(pow(size, 0.5)), int(pow(size, 0.5))), dtype=int)
ones = np.zeros(shape=(int(pow(size, 0.5)), int(pow(size, 0.5))), dtype=int)
ones[ones < 1] = 1

m31 = np.concatenate([ones, zeros, zeros])
m32 = np.concatenate([zeros, ones, zeros])
m33 = np.concatenate([zeros, zeros, ones])

blocks = np.concatenate([m31, m32, m33], axis=1)

l1 = np.concatenate([inverse_identity, blocks, blocks, identity, identity, identity, identity, identity, identity],
                    axis=1)
l2 = np.concatenate([blocks, inverse_identity, blocks, identity, identity, identity, identity, identity, identity],
                    axis=1)
l3 = np.concatenate([blocks, blocks, inverse_identity, identity, identity, identity, identity, identity, identity],
                    axis=1)

l4 = np.concatenate([identity, identity, identity, inverse_identity, blocks, blocks, identity, identity, identity],
                    axis=1)
l5 = np.concatenate([identity, identity, identity, blocks, inverse_identity, blocks, identity, identity, identity],
                    axis=1)
l6 = np.concatenate([identity, identity, identity, blocks, blocks, inverse_identity, identity, identity, identity],
                    axis=1)

l7 = np.concatenate([identity, identity, identity, identity, identity, identity, inverse_identity, blocks, blocks],
                    axis=1)
l8 = np.concatenate([identity, identity, identity, identity, identity, identity, blocks, inverse_identity, blocks],
                    axis=1)
l9 = np.concatenate([identity, identity, identity, identity, identity, identity, blocks, blocks, inverse_identity],
                    axis=1)

board = np.concatenate([l1, l2, l3, l4, l5, l6, l7, l8, l9])

for index, value in enumerate(initial_flatten):
    board[index][index] = value

uncolored = set()

while not allColored(size, board):

    saturationReversed = getSaturationFromBoard(board)

    for index, value in enumerate(saturationReversed):

        corParaIndex = corParaIndice(value, board)

        if corParaIndex == 0 and value not in uncolored:

            todasAsCores = {1, 2, 3, 4, 5, 6, 7, 8, 9}
            saturacao, coresUtilizadas = saturacaoParaIndice(value, board)
            maior = 0
            coresPossiveis = todasAsCores.difference(coresUtilizadas)

            # if value == 31:
            #     print(value)

            for cor in coresPossiveis:
                if numberOfUsageOfColor(cor, board) > maior:
                    maior = cor

            print(coresPossiveis)

            if len(coresPossiveis) > 0:
                if value in uncolored:
                    uncolored.remove(value)
                board[value][value] = list(reversed(list(coresPossiveis)))[0]

            else:
                uncolored.add(value)
                print('Impossivel resolver')

            print("Changed: row")
            solution = []
            for index in range(0, size * size):
                solution.append(board[index][index])
            print(np.array(solution).reshape((size, size)))
            break

        if index == len(saturationReversed)-1:
            uncolored = set()

def verifySolution(unverifiedSolution):
    sumToVerify = ((size * size) + size) / 2
    error = False
    for index, sumatory in enumerate(np.sum(unverifiedSolution, axis=0)):
        if sumatory != sumToVerify:
            print("Error at horizontal index: " + str(index))
            error = True

    for index, sumatory in enumerate(np.sum(unverifiedSolution, axis=1)):
        if sumatory != sumToVerify:
            print("Error at vertical index: " + str(index))
            error = True

    return not error

solution = np.array(solution).reshape((size, size))

print(verifySolution(solution))
print(solution)


# import numpy as np
# import random
#
#
# def grauParaIndice(indice, board):
#     color = board[indice][indice]
#     sum = np.sum(board[indice]) - color
#     return sum
#
#
# def corParaIndice(indice, board):
#     return board[indice][indice]
#
# def isNeighbor(indice1, indice2, board):
#     return board[indice1][indice2] == 1
#
# def allColored(size, board):
#     for index in range(0, size * size):
#         if board[index][index] == 0:
#             return False
#     return True
#
# def saturacaoParaIndice(indice, board):
#     colorSet = set()
#
#     for index in range(0, size * size):
#         if index == indice:
#             continue
#
#         if board[indice][index] == 1 and board[index][index] != 0:
#             colorSet.add(corParaIndice(index, board))
#
#     return (len(colorSet), colorSet)
#
# def getSaturationFromBoard(boardToGet):
#     saturation = []
#     for index in range(0, size * size):
#         satura, neighborColo = saturacaoParaIndice(index, boardToGet)
#
#         if len(neighborColo) == size:
#             print("its impossible to solve")
#         saturation.append(satura)
#
#     return list(reversed(np.argsort(saturation)))
#
# center = [3,8,5,7,2,6,1,4,9]
#
#
# initial_center = [[0, 2, 0, 5, 0, 1, 0, 9, 0],
#                   [8, 0, 0, 2, 0, 3, 0, 0, 6],
#                   [0, 3, 0, 0, 6, 0, 0, 7, 0],
#                   [0, 0, 1, 0, 8, 0, 6, 0, 0],
#                   [5, 4, 0, 0, 0, 0, 0, 1, 9],
#                   [0, 0, 2, 0, 0, 0, 7, 0, 0],
#                   [0, 9, 0, 0, 3, 0, 0, 8, 0],
#                   [2, 0, 0, 8, 0, 4, 0, 0, 7],
#                   [0, 1, 0, 9, 0, 7, 0, 6, 0]]
#
# initial_original = [[0, 2, 0, 5, 0, 1, 0, 9, 0],
#                     [8, 0, 0, 2, 0, 3, 0, 0, 6],
#                     [0, 3, 0, 0, 6, 0, 0, 7, 0],
#                     [0, 0, 1, 0, 0, 0, 6, 0, 0],
#                     [5, 4, 0, 0, 0, 0, 0, 1, 9],
#                     [0, 0, 2, 0, 0, 0, 7, 0, 0],
#                     [0, 9, 0, 0, 3, 0, 0, 8, 0],
#                     [2, 0, 0, 8, 0, 4, 0, 0, 7],
#                     [0, 1, 0, 9, 0, 7, 0, 6, 0]]
#
# easy = [[4, 2, 0, 0, 0, 7, 0, 0, 0],
#         [1, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 3, 7, 1, 6, 0, 0, 0, 9],
#         [0, 0, 2, 0, 5, 0, 0, 8, 0],
#         [9, 8, 0, 6, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 4, 0, 0, 0, 9, 1],
#         [7, 0, 1, 9, 0, 0, 0, 0, 2],
#         [5, 0, 0, 0, 2, 0, 0, 3, 6]]
#
# initial_flatten = np.array(initial_original).flatten()
#
# size = len(initial_original)
#
# def numberOfUsageOfColor(color, board):
#
#     usages = 0
#
#     for index in range(0,size*size):
#         value = board[index][index]
#         if value == color:
#             usages += 1
#
#     return usages
#
# array = np.zeros(shape=(size * size, size * size), dtype=int)
#
# identity = np.identity(size, dtype=int)
#
# inverse_identity = np.identity(size, dtype=int)
# inverse_identity[inverse_identity > 0] = -1
# inverse_identity[inverse_identity > -1] = 1
# inverse_identity[inverse_identity < 1] = 0
#
# zeros = np.zeros(shape=(int(pow(size, 0.5)), int(pow(size, 0.5))), dtype=int)
# ones = np.zeros(shape=(int(pow(size, 0.5)), int(pow(size, 0.5))), dtype=int)
# ones[ones < 1] = 1
#
# m31 = np.concatenate([ones, zeros, zeros])
# m32 = np.concatenate([zeros, ones, zeros])
# m33 = np.concatenate([zeros, zeros, ones])
#
# blocks = np.concatenate([m31, m32, m33], axis=1)
#
# l1 = np.concatenate([inverse_identity, blocks, blocks, identity, identity, identity, identity, identity, identity],
#                     axis=1)
# l2 = np.concatenate([blocks, inverse_identity, blocks, identity, identity, identity, identity, identity, identity],
#                     axis=1)
# l3 = np.concatenate([blocks, blocks, inverse_identity, identity, identity, identity, identity, identity, identity],
#                     axis=1)
#
# l4 = np.concatenate([identity, identity, identity, inverse_identity, blocks, blocks, identity, identity, identity],
#                     axis=1)
# l5 = np.concatenate([identity, identity, identity, blocks, inverse_identity, blocks, identity, identity, identity],
#                     axis=1)
# l6 = np.concatenate([identity, identity, identity, blocks, blocks, inverse_identity, identity, identity, identity],
#                     axis=1)
#
# l7 = np.concatenate([identity, identity, identity, identity, identity, identity, inverse_identity, blocks, blocks],
#                     axis=1)
# l8 = np.concatenate([identity, identity, identity, identity, identity, identity, blocks, inverse_identity, blocks],
#                     axis=1)
# l9 = np.concatenate([identity, identity, identity, identity, identity, identity, blocks, blocks, inverse_identity],
#                     axis=1)
#
# board = np.concatenate([l1, l2, l3, l4, l5, l6, l7, l8, l9])
#
# for index, value in enumerate(initial_flatten):
#     board[index][index] = value
#
# uncolored = set()
# solution = []
# for index in range(0, size * size):
#     solution.append(board[index][index])
# print(np.array(solution).reshape((size, size)))
#
# for i in range(1, 10):
#     for nodeIndex in range(0, size*size):
#
#         neighborSourceColor = set()
#         neighborSourceColor = set()
#
#         for lastNode in range(0, size * size):
#             if isNeighbor(lastNode, nodeIndex, board):
#                 neighborSourceColor.add(corParaIndice(lastNode, board))
#
#         if i not in neighborSourceColor and board[nodeIndex][nodeIndex] == 0:
#             board[nodeIndex][nodeIndex] = i
#
#         for otherNode in range(0, size*size):
#             if (not isNeighbor(otherNode, nodeIndex, board)) and (corParaIndice(otherNode, board) == 0) and (corParaIndice(otherNode, board) != i):
#                 board[otherNode][otherNode] = i
#                 solution = []
#                 for index in range(0, size * size):
#                     solution.append(board[index][index])
#                 print(np.array(solution).reshape((size, size)))





# while not allColored(size, board):
#
#     saturationReversed = getSaturationFromBoard(board)
#
#     for index, value in enumerate(saturationReversed):
#
#         corParaIndex = corParaIndice(value, board)
#
#         if corParaIndex == 0 and value not in uncolored:
#
#             todasAsCores = {1, 2, 3, 4, 5, 6, 7, 8, 9}
#             saturacao, coresUtilizadas = saturacaoParaIndice(value, board)
#             maior = 0
#             coresPossiveis = todasAsCores.difference(coresUtilizadas)
#
#             # if value == 31:
#             #     print(value)
#
#             for cor in coresPossiveis:
#                 if numberOfUsageOfColor(cor, board) > maior:
#                     maior = cor
#
#             print(coresPossiveis)
#
#             if len(coresPossiveis) > 0:
#                 if value in uncolored: uncolored.remove(value)
#                 board[value][value] = random.choice(list(coresPossiveis))
#
#             else:
#                 uncolored.add(value)
#                 print('Impossivel resolver')
#
#             print("Changed: row")
#             solution = []
#             for index in range(0, size * size):
#                 solution.append(board[index][index])
#             print(np.array(solution).reshape((size, size)))
#             break
#
#         if index == len(saturationReversed)-1:
#             uncolored = set()

def verifySolution(unverifiedSolution):
    sumToVerify = ((size * size) + size) / 2
    error = False
    for index, sumatory in enumerate(np.sum(unverifiedSolution, axis=0)):
        if sumatory != sumToVerify:
            print("Error at horizontal index: " + str(index))
            error = True

    for index, sumatory in enumerate(np.sum(unverifiedSolution, axis=1)):
        if sumatory != sumToVerify:
            print("Error at vertical index: " + str(index))
            error = True

    return not error

solution = np.array(solution).reshape((size, size))

print(verifySolution(solution))
print(solution)
