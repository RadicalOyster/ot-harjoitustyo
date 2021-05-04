import sys
from heapdict import heapdict

# Clean up everything here


class PathFinding():
    """A class that takes care of all pathfinding functionality, including
    determining distances and finding the shortest path between points using
    Dijkstra's algorithm.
    """
    def __init__(self, position_x, position_y, level):
        """Constructor for Pathfinding. Called every time paths are calculated
        in order to initialize the state of the system.

        Args:
            position_x: x coordinate of the start position for the algorithm
            position_y: y coordinate of the start position for the algorithm
            level: a 2-dimensional array containing the movement costs for every node.
        """
        self.level = level
        self.rows = len(self.level)
        self.columns = len(self.level[0])

        self.queue = heapdict()

        self.distance = [[50000 for x in range(
            self.columns)] for y in range(self.rows)]
        self.visited = [[False for x in range(
            self.columns)] for y in range(self.rows)]
        # needed later for reconstructing path
        self.previous = {(x, y): 0 for x in range(self.columns)
                         for y in range(self.rows)}

        self.distance[position_y][position_x] = 0
        self.visited[position_y][position_x] = True
        self.queue[position_y, position_x] = 0
        self.path_found = False

    def is_valid(self, x, y):
        """Checks if a position is within bounds.

        Args:
            x: x coordinate of the node
            y: y coordinate of the node
        """
        return x >= 0 and x < len(self.level[0]) and y >= 0 and y < len(self.level)

    # Visit each of the node's neighbors
    def _traverse(self, row, column, destination=(-1, -1)):
        """Check each of the given node's neighbors and add them
        to the queue if they haven't been visited yet. 

        Args:
            row: Y coordinate of the node.
            column: X coordinate of the node.
        """
        for i in range(0, 4):
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
            if not self.is_valid(new_column, new_row):
                continue
            if self.visited[new_row][new_column]:
                continue

            node = (column, row)
            self.previous[new_column, new_row] = node
            if (new_column, new_row) == destination:
                self.path_found = True
                break

            node_distance = int(
                self.distance[row][column]) + int(self.level[new_row][new_column])

            self.queue[new_row, new_column] = node_distance
            self.distance[new_row][new_column] = node_distance
            self.visited[new_row][new_column] = True

    # Returns a list of reachable nodes
    def return_ranges(self, distance):
        """Returns all nodes within a given distance. Should be used
        after calculating distances.

        Args:
            distance: Maximum distance of a node from the start position.
        """
        reachable_spaces = []
        for i in range(0, len(self.level)):
            for j in range(0, len(self.level[0])):
                if (self.distance[i][j] > distance):
                    pass
                else:
                    reachable_spaces.append((j, i))
        return reachable_spaces

    # Returns shortest path to point
    def _construct_path(self, start, destination):
        """Constructs the shortest path between to nodes.

        Args:
            start: Starting node
            destination: Destination node
        """
        path = []
        current_node = destination
        path.append(destination)
        while current_node != start:
            current_node = self.previous[current_node]
            path.append(current_node)
        return path

    def return_path(self, start, destination):
        """Runs the algorithm and returns the shortest
        path between two nodes.

        Args:
            start: Starting node
            destination: Destination node
        """
        self.__init__(start[0], start[1], self.level)
        while not self.path_found and len(self.queue) > 0:
            head = self.queue.popitem()
            row, column = head[0]
            self._traverse(row, column, destination)
        return self._construct_path(start, destination)

    # Run the algorithm to determine the distance from the given point to
    # every other point on the map
    def calculate_distances(self, position_x, position_y):
        """Calculates the distance of everyone node to the given node.

        Args:
            position_x: X coordinate of the starting node.
            position_y: Y coordinate of the starting node.
        """
        self.__init__(position_x, position_y, self.level)
        while not self.path_found and len(self.queue) > 0:
            head = self.queue.popitem()
            row, column = head[0]
            self._traverse(row, column)