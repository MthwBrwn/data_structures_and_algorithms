from .graph import Graph
from .conftest import graph_empty


def test_graph_import():
    """
    """
    assert Graph


def test_empty_graph():
    """
    """
    testgraph = Graph()
    assert testgraph.has_vert('foo') is False


#create a test to check for added vertex
# def test_adds_a_node():
#     """
#     """
#     startgraph = Graph()
#     assert startgraph.add_vert("3") == ["3"]


#create a test to determine is has Vert


#create a test to see if add vert to Dict which already has vert
# raises exception
#
#
# Create a test to show a new formed graph has no edges

