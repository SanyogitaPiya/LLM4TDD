import pytest
from problem1805 import code1805
# #Partition 1 - Valid Additive Sequence
def test1():
        str = "a123bc34d8ef34"
        assert code1805(str) == 3
def test2():
        str = "a1b01c001"
        assert code1805(str) == 1
def test3():
        str = "leet1234code234"
        assert code1805(str) == 2


def test4():
        str = "abcdef"
        assert code1805(str) == 0

def test5():
        str = "12345678"
        assert code1805(str) == 1