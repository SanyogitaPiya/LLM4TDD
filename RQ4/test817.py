def test3():
        str = "ACGTACGTACGTACGTACGT"
        assert code187(str) == ["ACGTACGTAC","CGTACGTACG","GTACGTACGT","TACGTACGTA"]


def test4():
        str = "ACGTACGTACGTACGTACGTACGTACGTACGT"
        assert code187(str) == ["ACGTACGTAC","CGTACGTACG","GTACGTACGT","TACGTACGTA"]

def test6():
        str = "ACGTACGTACGTACGTACGTACGTA"
        assert code187(str) == ["ACGTACGTAC","CGTACGTACG","GTACGTACGT","TACGTACGTA"]

def test1():
        str = "ACGT"
        assert code187(str) == []
def test2():
        str = "ACGTACGTAC"
        assert code187(str) == []

def test5():
        str = "ACGAATTCCGTA"
        assert code187(str) == []