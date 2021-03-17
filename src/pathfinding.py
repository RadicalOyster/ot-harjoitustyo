import sys
from heapdict import heapdict

def GetMovementRange(cursorX, cursorY):
    map = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    movement = 3
    rows = len(map)
    columns = len(map[0])

    queue = heapdict()

    distance = [[sys.maxsize for x  in range(columns)] for y in range(rows)]
    visited = [[False for x  in range(columns)] for y in range(rows)]
    previous = {(x,y):0 for x in range(columns) for y in range(rows)}

    distance[cursorY][cursorX] = 0
    visited[cursorY][cursorX] = True
    queue[cursorY, cursorX] = 0

    def isValid(x, y):
        return x >= 0 and x < len(map[0]) and y >= 0 and y < len(map)

    def traverse(row, column):
        for i in range (0,4):
            new_row = row
            new_column = column
            if i == 0:
                new_row -= 1
            elif i == 1:
                new_row += 1
            elif i == 2:
                new_column -= 1
            elif i == 3:
                new_column += 1
            if not isValid(new_column,new_row):
                continue
            if visited[new_row][new_column]:
                continue

            node = (row,column)
            previous[new_row,new_column] = node

            node_distance = int(distance[row][column]) + int(map[new_row][new_column])
            queue[new_row,new_column] = node_distance
            distance[new_row][new_column] = node_distance
            visited[new_row][new_column] = True

    while len(queue) > 0:
        head = queue.popitem()
        row, column = head[0]
        traverse(row,column)

    def PrintMovementRange(distance, movement):
        for line in distance:
            for value in line:
                if (value > movement):
                    print("X",end=" ")
                else:
                    print("*",end=" ")
            print("")

    #PrintMovementRange(distance, 5)

    def ReturnMovementRange():
        movableSpaces = []
        for i in range(0,len(map)):
            for j in range(0,len(map[0])):
                if (distance[i][j] > movement):
                    pass
                else:
                    movableSpaces.append((i,j))
        return movableSpaces
    
    return ReturnMovementRange()