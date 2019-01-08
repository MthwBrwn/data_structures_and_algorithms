import pytest
from .graph import Graph
# from .conftest import


def test_graph_import():
    """ initial test to see if graph was properly imported
    """
    assert Graph


def test_empty_graph(graph_empty):
    """ this test check to see if empty graph contains a value.
    """
    assert graph_empty.has_vert('foo') is False


def test_has_vert_filled(graph_one):
    """ create a test to check for vertex with known fixture
    """

    assert graph_one.has_vert("C") is True


def test_has_vert_filled_wrong(graph_one):
    """ create a test to check for lack of vertex with known fixture
    """
    assert graph_one.has_vert("X") is False

#create a test to determine is has Vert


#create a test to see if add vert to Dict which already has vert
# raises exception
#
#
# Create a test to show a new formed graph has no edges

