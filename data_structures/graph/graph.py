class Graph(object):
    """this class creates a graph object. This object has the ability to have a node with a value
    nd a number of edges connecting those nodes .
    """
    def __init__(self):
        self.graph = {}
        # graph is a dictionary of key pairs { 'a' : ['d'], 'b' : ['c']} etc.
        # self._size = 0

    # def __repr__(self):
    #     output = f'<Graph: size - { self.size }>'
    #     return output

    # def __str__(self):
    #     self.size

    # def __len__(self):
    #     return self._size

    def has_vert(self, val):
        """This method takes in a value and determines if this value exists in the graph.
        """
        return val in self.graph

    def add_vert(self, val):
        """ this method takes in a value and adds a node to the graph.
        """
        # if self.graph.has_vert(val) is True:
        #     raise Exception('This value has been used already.')
        # else:
        self.graph[val] = {}

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
