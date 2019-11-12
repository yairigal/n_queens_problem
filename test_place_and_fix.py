from place_and_fix import QueenMatrix


def test_is_threat():
    # 0  1  2  3
    # 4  5  6  7
    # 8  9  10 11
    # 12 13 14 15

    q = QueenMatrix(4)
    queen = 0, 0
    assert q.is_threat(*queen, 3, 3)
    assert q.is_threat(*queen, 0, 3)
    assert q.is_threat(*queen, 3, 0)
    assert q.is_threat(*queen, 2, 2)
    assert not q.is_threat(*queen, 3, 2)

    queen = 2, 2
    assert q.is_threat(*queen, 0, 2)
    assert q.is_threat(*queen, 1, 2)
    assert q.is_threat(*queen, 3, 2)
    assert q.is_threat(*queen, 2, 3)
    assert q.is_threat(*queen, 2, 1)
    assert q.is_threat(*queen, 2, 0)
    assert q.is_threat(*queen, 0, 0)
    assert q.is_threat(*queen, 1, 1)
    assert q.is_threat(*queen, 1, 3)
    assert q.is_threat(*queen, 3, 1)
    assert not q.is_threat(*queen, 0, 1)
    assert not q.is_threat(*queen, 3, 0)
    assert not q.is_threat(*queen, 0, 3)


def test_queen_generation():
    q = QueenMatrix(8)
    q.queens
    assert q.steps == 8
    assert sorted(q.queens) == [0, 1, 2, 3, 4, 5, 6, 7]

    q = QueenMatrix(4)
    q.queens
    assert q.steps == 4
    assert sorted(q.queens) == [0, 1, 2, 3]

