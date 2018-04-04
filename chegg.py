adjMap = { "a": ["b", "c", "d"], "b": ["a", "d"], "c": ["a"], "d": ["a", "b"]}


colors = ['r','g']


# A quick map of nodes to degrees
degreeMap = dict(zip(adjMap.keys(), [len(adjMap[x]) for x in adjMap.keys()]))

# Sorts the map by degree of each key and reverses it, so the highest degree is first
sortedDegreeList = sorted(degreeMap, key=degreeMap.get, reverse=True)

# Empty coloring
currentColor = {}

def welshPowell(adjMap, sortedDegreeList, availColors, currentColoring):

    # Get first node that is not colored
    for index in range(len(sortedDegreeList)):

        node = sortedDegreeList[index]

        if (node not in currentColoring.keys()):
            # Get the first available color
            newColor = availColors.pop()
            currentColoring[node] = newColor

        # Iterate through remaining vertices, looking for non-adjacent nodes
        for otherNode in sortedDegreeList[index + 1:]:
        flag = False

            for adjacentNode in adjMap[otherNode]:

                if ( currentColoring[adjacentNode] == newColor ):
                flag = True

                break

    # We did not find any neighbors of the current node with this color
    if ( flag == False ):
        currentColoring[otherNode] = newColor

        # Recursive call to shorter degree list with updated coloring
        welshPowell(adjMap, sortedDegreeList[index + 1:], availColors, currentColoring)