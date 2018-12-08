from queue import Queue
import pytest

@pytest.fixture
def empty_queue():
    return Queue()


@pytest.fixture
def one_queue():
    q = Queue()
    q.enqueue(1)
    return q


def test_for_class_queue_exists():
    """ This tests the import is working/ existence of class Queue in tests
    """
    testaqueue = Queue()
    assert isinstance(testaqueue, Queue)


def test_for_top_of_empty():
    """ This tests the the value of of queue is 0 at start
    """
    testaqueue = Queue()
    assert testaqueue.front is None


def test_for_front_of_one(one_queue):
    """ This checks the value of the front when enqueue is called
    """
    assert one_queue.front.value == 1


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


def test_repr_at_empty(empty_queue):
    """
    """
    assert repr(empty_queue) == '<Queue Front: None> <<Queue back: None>'


def test_str_at_empty(empty_queue):
    """
    """
    assert str(empty_queue) == '<Queue Front: None>'
