class Graph(object):
    """this class creates a graph object. This object has the ability to have a node with a value
    nd a number of edges connecting those nodes .
    """
    def __init__(self):
        self.graph = {}
        # self._size = 0

    # def __repr__(self):
    #     output = f'<Graph: size - { self.size }>'
    #     return output

    # def __str__(self):
    #     self.size

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
        # self._size += 1

    def add_edge(self, v1, v2, weight):
        """
        """
        # add a relationship and weight between two verts
        # don't forget to validate
        pass

    def get_neighbors(self, val):
        """
        """
        # Given a val (key), return all adjacent verts
        pass
