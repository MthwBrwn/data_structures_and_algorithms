from queue import Queue
import pytest

@pytest.fixture
def empty_queue():
    return Queue()


def test_for_class_queue_exists():
    """ This tests the import is working/ existence of class Queue in tests
    """
    testaqueue = Queue()
    assert isinstance(testaqueue, Queue)


def test_for_top_of_empty():
    """ This tests the the value of of queue is 0 at start
    """
    testaqueue = Queue()
    assert testaqueue.top is None


def test_for_back_of_empty():
    """ This tests the the back of an empty queue object is None
    """
    testaqueue = Queue()
    assert testaqueue.back is None


def test_for_size_of_empty(empty_queue):
    """ This tests the the size (len) of an empty queue object is None
    The test uses a pytest fixture.
    """
    assert len(empty_queue) == 0
