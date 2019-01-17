from .hash_table import Hashtable
import pytest


def test_to_see_if_import_works():
    assert Hashtable


def test_sum_hash():
    testtable = Hashtable()

    assert testtable.sum_hash('word') == 60


def test_repr():
    testtable = Hashtable()

    assert repr(testtable) == 'bucket size : 64'


def test_str():
    testtable = Hashtable()

    assert str(testtable) == 'bucket size : 64'


def test_put_method():
    testtable = Hashtable()
    testtable.put('tester', 'testerval')
    assert testtable.get('tester') == 'testerval'

