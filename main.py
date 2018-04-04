import numpy as np

def grauParaIndice(indice, board):
    color = board[indice][indice]
    sum = np.sum(board[indice]) - color
    return sum

def corParaIndice(indice, board):
    return board[indice][indice]

def saturacaoParaIndice(indice, board):

    colorSet = set()

    for index, line in enumerate(board):
        if index == indice:
            continue

        if board[index][indice] == 1 and line[index] != 0:
            colorSet.add(line[index])

    return (len(colorSet), colorSet)

initial = [[1, 3, 0, 0],
           [0, 0, 0, 0],
           [0, 4, 0, 0],
           [0, 0, 0, 2]]
initial_flatten = np.array(initial).flatten()

size = len(initial)


array = np.zeros(shape=(size*size, size*size), dtype=int)

identity = np.identity(size, dtype=int)

inverse_identity = np.identity(size, dtype=int)
inverse_identity[inverse_identity > 0] = -1
inverse_identity[inverse_identity > -1] = 1
inverse_identity[inverse_identity < 1] = 0

zeros = np.zeros(shape=(2,2), dtype=int)
ones = np.zeros(shape=(2,2), dtype=int)
ones[ones < 1] = 1

m31 = np.concatenate([ones, zeros])
m32 = np.concatenate([zeros, ones])
blocks = np.concatenate([m31, m32], axis=1)

l1 = np.concatenate([inverse_identity, blocks, identity, identity], axis=1)
l2 = np.concatenate([blocks, inverse_identity, identity, identity], axis=1)
l3 = np.concatenate([identity, identity, inverse_identity, blocks], axis=1)
l4 = np.concatenate([identity, identity, blocks, inverse_identity], axis=1)

board = np.concatenate([l1, l2, l3, l4])

for index,value in enumerate(initial_flatten):
    board[index][index] = value
print(board)


saturation = []
neighborColors = []
vertexColors = []

for index in range(0, size * size):
    satura, neighborColo = saturacaoParaIndice(index, board)

    saturation.append(satura)
    neighborColors.append(neighborColo)
    vertexColors.append(corParaIndice(index, board))


print(vertexColors)

saturationReversed = list(reversed(np.argsort(saturation)))

for index, value in enumerate(saturationReversed):

    corParaIndex = corParaIndice(value, board)
    if corParaIndex == 0:
        saturacao, coresUtilizadas = saturacaoParaIndice(value,board)
        for i in range(1, size+1):
            if i not in coresUtilizadas:
                board[value][value] = i
                break


solution = []

for index in range(0, size*size):
    solution.append(board[index][index])

def verifySolution(unverifiedSolution):

    sumToVerify = ((size * size) + size) / 2

    for sumatory in  np.sum(unverifiedSolution, axis=0):
        if sumatory != sumToVerify:
            return False

    for sumatory in  np.sum(unverifiedSolution, axis=1):
        if sumatory != sumToVerify:
            return False

    return True




solution = np.array(solution).reshape((size, size))


print(verifySolution(solution))
print(solution)


# print(np.argmax(saturation))





# values[15] = (1, set())



# 1 0 0 0 1 1 0 0 0 1 1 1 0 1 1 1
# 0 1 0 0 1 1 0 0 1 0 1 1 1 0 1 1
# 0 0 1 0 0 0 1 1 1 1 0 1 1 1 0 1
# 0 0 0 1 0 0 1 1 1 1 1 0 1 1 1 0
# 1 1 0 0 1 0 0 0 1 1 0 0 0 1 1 1
# 1 1 0 0 0 1 0 0 1 1 0 0 1 0 1 1
# 0 0 1 1 0 0 1 0 0 0 1 1 1 1 0 1
# 0 0 1 1 0 0 0 1 0 0 1 1 1 1 1 0
# 0 1 1 1 0 1 1 1 1 0 0 0 1 1 0 0
# 1 0 1 1 1 0 1 1 0 1 0 0 1 1 0 0
# 1 1 0 1 1 1 0 1 0 0 1 0 0 0 1 1
# 1 1 1 0 1 1 1 0 0 0 0 1 0 0 1 1
# 0 1 1 1 0 1 1 1 1 1 0 0 1 0 0 0
# 1 0 1 1 1 0 1 1 1 1 0 0 0 1 0 0
# 1 1 0 1 1 1 0 1 0 0 1 1 0 0 1 0
# 1 1 1 0 1 1 1 0 0 0 1 1 0 0 0 1