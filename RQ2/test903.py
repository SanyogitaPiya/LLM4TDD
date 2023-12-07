import pytest
from code1 import a
#Increasing segment:These are segments of consecutive 'I' characters in the string s. In these segments, each subsequent integer should be larger than the previous one.
def test1():
        str = "III"
        assert a(str) == 4

#Decreasing segment: These are segments of consecutive 'D' characters in the string s. In these segments, each subsequent integer should be smaller than the previous one.
def test2():
        str = "DDD"
        assert a(str) == 3
#Increasing and Decreasing segments:The permutation starts with increasing, then decreasing, increasing, and finally increasing segments.
def test3():
        str = "IDID"
        assert a(str) == 4

#The permutation starts with increasing, then decreasing, then decreasing, and finally increasing segments.
def test4():
        str = "IDDI"
        assert a(str) == 4