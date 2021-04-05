import sys
from heapdict import heapdict

#Clean up everything here
class PathFinding():
    def __init__(self, cursorX, cursorY, level):
        self.level = level
        self.rows = len(self.level)
        self.columns = len(self.level[0])

        self.queue = heapdict()

        self.distance = [[50000 for x in range(self.columns)] for y in range(self.rows)]
        self.visited = [[False for x in range(self.columns)] for y in range(self.rows)]
        #needed later for reconstructing path
        self.previous = {(x,y):0 for x in range(self.columns) for y in range(self.rows)}

        self.distance[cursorY][cursorX] = 0
        self.visited[cursorY][cursorX] = True
        self.queue[cursorY, cursorX] = 0
        self.path_found = False
        
    def _isValid(self, x, y):
        return x >= 0 and x < len(self.level[0]) and y >= 0 and y < len(self.level)
    
    #Visit each of the node's neighbors
    def traverse(self, row, column, destination=(-1, -1)):
        for i in range (0, 4):
            new_row = row
            new_column = column
            if i == 0:
                new_row -= 1
            elif i == 1:
                new_row += 1
            elif i == 2:
                new_column += 1
            elif i == 3:
                new_column -= 1
            if not self._isValid(new_column, new_row):
                continue
            if self.visited[new_row][new_column]:
                continue

            node = (column, row)
            self.previous[new_column, new_row] = node
            if (new_column, new_row) == destination:
                self.path_found = True
                break


            node_distance = int(self.distance[row][column]) + int(self.level[new_row][new_column])

            self.queue[new_row, new_column] = node_distance
            self.distance[new_row][new_column] = node_distance
            self.visited[new_row][new_column] = True
    
    def PrintRange(self, reach):
        for line in self.distance:
            for value in line:
                if (value > reach):
                    print("X",end=" ")
                else:
                    print("*",end=" ")
            print("")
    
    def PrintDistances(self):
        for line in self.distance:
            for value in line:
                print(value,end=" ")
            print("")
    
    #Returns a list of reachable nodes
    def ReturnRanges(self, reach):
        reachableSpaces = []
        for i in range(0, len(self.level)):
            for j in range(0, len(self.level[0])):
                if (self.distance[i][j] > reach):
                    pass
                else:
                    reachableSpaces.append((j,i))
        return reachableSpaces
    
    #Returns shortest path to point
    #Incomplete
    def _constructPath(self, start, destination):
        path = []
        current_node = destination
        path.append(destination)
        while current_node != start:
            current_node = self.previous[current_node]
            path.append(current_node)
        return path

    def ReturnPath(self, start, destination):
        self.__init__(start[0], start[1], self.level)
        while not self.path_found and len(self.queue) > 0:
            head = self.queue.popitem()
            row, column = head[0]
            self.traverse(row, column, destination)
        return self._constructPath(start, destination)
    
    #Run the algorithm to determine the distance between each point on the level and the cursor position
    def CalculateDistances(self, x, y):
        self.__init__(x, y, self.level)
        while not self.path_found and len(self.queue) > 0:
            head = self.queue.popitem()
            row, column = head[0]
            self.traverse(row, column)
        self.PrintRange(8)
        self.PrintDistances()