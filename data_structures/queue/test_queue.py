from queue import Queue
import pytest

@pytest.fixture
def empty_queue():
    """ This fixture si used to test a empty queue condition
    """
    return Queue()


@pytest.fixture
def one_queue():
    """this fixture is used to test a Queue with one node added (enqueue)
    """
    q = Queue()
    q.enqueue(1)
    return q


@pytest.fixture
def iter_list():
    """ This is=fixture sets a small queue of iterated nodes for testing
    """
    q = Queue([6, 5, 4])
    return q


def test_for_class_queue_exists():
    """ This tests the import is working/ existence of class Queue in tests
    """
    testaqueue = Queue()
    assert isinstance(testaqueue, Queue)


def test_for_front_of_empty():
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


def test_for_back_of_one(one_queue):
    """ This checks the value of the back when enqueue is called
    """
    assert one_queue.back.value == 1


def test_for_size_of_one(one_queue):
    """ This checks the value of the back when enqueue is called
    """
    assert len(one_queue) == 1


def test_for_size_of_empty(empty_queue):
    """ This tests the the size (len) of an empty queue object is None
    The test uses a pytest fixture.
    """
    assert len(empty_queue) == 0


def test_repr_at_empty(empty_queue):
    """ This checks the repr value on an empty queue object
    """
    assert repr(empty_queue) == '<Queue Front: None> <<Queue back: None>'


def test_str_at_empty(empty_queue):
    """This checks that the front node is set to None
    """
    assert str(empty_queue) == '<Queue Front: None>'


def test_for_back_of_one(one_queue):
    """ This checks the value of the back when enqueue is called
    """
    assert one_queue.back.value == 1


def test_of_iterable():
    """
    """
    q = Queue([6, 5, 4])
    assert q.back.value == 4
    assert repr(q) == "<Queue Front: <Node: 6>> <<Queue back: <Node: 4>>"
    q.enqueue(3)
    assert q.back.value == 3
    assert repr(q) == "<Queue Front: <Node: 6>> <<Queue back: <Node: 3>>"


def test_of_iterable_len():
    """This is a test to make sure the queue is iterable
    """
    q = Queue([6, 5, 4])
    assert len(q) == 3
    q.enqueue(3)
    assert len(q) == 4


def test_error():
    """ Assertions about expected exceptions
    """
    with pytest.raises(TypeError):
        Queue('test string for error')

def test_of_dequeue_with_known_check_len():
    """ This is first test of dequeue with a queue of iterated values
    """
    q = Queue([2, 4, 6, 8])
    assert len(q) == 4
    q.dequeue()
    assert len(q) == 3


def test_of_dequeue_with_known_check_value():
    """ This is first test of dequeue with a queue of iterated values
    """
    q = Queue([2, 4, 6, 8])
    assert q.dequeue().value == 2
    assert len(q) == 3


def test_of_dequeue_with_empty(empty_queue):
    """this tests for the Attribute Error with an attempted dequeue on empty
    """
    with pytest.raises(AttributeError):
        empty_queue.dequeue()


def test_of_empty_to_enqueue_to_dequeue():
    """This test check to see if enqueue will add a string character
    """
    q = Queue()
    q.enqueue('test')
    assert q.back.value == "test"
    q.dequeue()
    with pytest.raises(AttributeError):
        q.dequeue()



def test_of_peek(empty_queue):
    """This test checks is the peek function works for an enquque followed by a dequeue
    """
    empty_queue.enqueue(3)
    assert empty_queue.peek().value == 3
    empty_queue.dequeue()
    assert empty_queue.peek() is None


