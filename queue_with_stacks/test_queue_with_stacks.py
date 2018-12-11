from .queue_with_stacks import PseudoQueue, Stack, Node
import pytest


def test_for_proper_import():
    """ check for proper import of all classes
    """
    assert PseudoQueue


def test_for_enqueue_with_no_prev_nodes():
    pq = PseudoQueue()
    pq.enqueue(3)
    assert pq.stack_a.top.value == 3


def test_for_enqueue_with_no_prev_nodes_3():
    pq = PseudoQueue()
    pq.enqueue(4)
    pq.enqueue(2)
    pq.enqueue(1)
    assert pq.stack_a.top.value == 1


def test_for_dequeue_after_enqueue():
    pq = PseudoQueue()
    pq.enqueue(3)
    assert pq.stack_a.top.value == 3
    assert pq.dequeue() == 1




