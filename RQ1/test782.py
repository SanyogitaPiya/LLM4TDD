def test_2x2_chessboard():
    b = [[0, 1], [1, 0]]
    assert solution.movesToChessboard(b) == 0

def test_3x3_chessboard():
    b = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
    assert solution.movesToChessboard(b) == 0

def test_4x4_chessboard():
    b = [[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]]
    assert solution.movesToChessboard(b) == 0

def test_1x1_chessboard():
    b = [[0]]
    assert solution.movesToChessboard(b) == 0

def test_non_square_chessboard():
    b = [[0, 1, 0], [1, 0, 1]]
    assert solution.movesToChessboard(b) == -1

def test_one_type_of_piece():
    b = [[0, 0], [0, 0]]
    assert solution.movesToChessboard(b) == 0

def test_7x7_chessboard():
    b = [[0, 1, 0, 1, 0, 1, 0],
         [1, 0, 1, 0, 1, 0, 1],
         [0, 1, 0, 1, 0, 1, 0],
         [1, 0, 1, 0, 1, 0, 1],
         [0, 1, 0, 1, 0, 1, 0],
         [1, 0, 1, 0, 1, 0, 1],
         [0, 1, 0, 1, 0, 1, 0]]
    assert solution.movesToChessboard(b) == 0

def test_custom_case():
    b = [[0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1]]
    assert solution.movesToChessboard(b) == 2