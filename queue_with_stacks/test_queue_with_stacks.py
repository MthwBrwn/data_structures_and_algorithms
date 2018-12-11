from .queue_with_stacks import PseudoQueue
import pytest


def test_for_proper_import():
    """ check for proper import of all classes
    """
    assert PseudoQueue

def test_for_enqueue_when_no_prev_nodes():
    pq = PseudoQueue()
    pq.enqueue(3)
    assert pq.top.value == 3
