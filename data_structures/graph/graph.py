class Graph(object):
    """this class creates a graph object. This object has the ability to have a node with a value
    nd a number of edges connecting those nodes .
    """
    def __init__(self):
        self.graph = {}

    def __repr__(self):
        output = f'<Graph: size - {len(self.graph)}>'
        return output

    def __str__(self):
        pass

    def __len__(self):
        return len(self.graph)

    def has_vert(self, val):
        """This method takes in a value and determines if this value exists in the graph.
        """
        return val in self.graph

    def add_vert(self, val):
        """ this method takes in a value and adds a node to the graph.
        """
        if self.has_vert(val):

            raise Exception('This value has been used already.')

        self.graph[val] = {}

    def add_edge(self, v1, v2, weight):
        """This sets up an edge between two vertices as well as a weight
        """
        if v1 in self.graph and v2 in self.graph:
            self.graph[v1][v2] = weight
            self.graph[v2][v1] = weight

            return self
        else:
            raise Exception('vertex not found')

    def get_neighbors(self, val):
        """ This method returns back any vertex that is adjacent to the argument
        """
        if val in self.graph:
            return tuple(self.graph[val])

        raise Exception('vertex not found. Please input valid vertex.')

