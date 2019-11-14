from main import QueenMatrix


# HELP FUNCTION
def create_game_with_queens(new_queens):
    n = len(new_queens)
    q = QueenMatrix(n)
    queens = q.queens
    for i in range(n):
        queens[i] = new_queens[i]

    return q


# TESTS

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
    q.queens  # generate queens
    assert q.steps == 8
    assert sorted(q.queens) == [0, 1, 2, 3, 4, 5, 6, 7]

    q = QueenMatrix(4)
    q.queens  # generate queens
    assert q.steps == 4
    assert sorted(q.queens) == [0, 1, 2, 3]


def test_is_done():
    # X * * *
    # * * X *
    # * X * *
    # * * * X
    q = create_game_with_queens([0, 2, 1, 3])
    assert not q.done

    # * X * *
    # * * * X
    # X * * *
    # * * X *
    q = create_game_with_queens([1, 3, 0, 2])
    assert q.done

    winning_sequences = [
        [3, 6, 2, 7, 1, 4, 0, 5],
        [4, 1, 3, 6, 2, 7, 5, 0],
        [3, 1, 6, 2, 5, 7, 4, 0],
        [3, 5, 7, 2, 0, 6, 4, 1],
        [2, 5, 7, 0, 3, 6, 4, 1],
        [4, 2, 7, 3, 6, 0, 5, 1],
        [4, 6, 3, 0, 2, 7, 5, 1],
        [3, 0, 4, 7, 5, 2, 6, 1],
        [2, 5, 3, 0, 7, 4, 6, 1],
        [5, 1, 6, 0, 3, 7, 4, 2],
        [3, 6, 0, 7, 4, 1, 5, 2],
        [5, 3, 6, 0, 7, 1, 4, 2]
    ]

    losing_sequences = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [5, 5, 5, 5, 5, 5, 5, 5],
        [7, 7, 7, 7, 7, 7, 7, 7],
        [0, 1, 2, 3, 4, 5, 6, 7],
        [7, 6, 5, 4, 3, 2, 1, 0]
    ]

    for state in winning_sequences:
        q = create_game_with_queens(state)
        assert q.done

    for state in losing_sequences:
        q = create_game_with_queens(state)
        assert not q.done


def test_cost():
    # * X * *
    # * * * X
    # X * * *
    # * * X *
    q = create_game_with_queens([1, 3, 0, 2])
    assert q.cost(0, 0) == 2
    assert q.cost(0, 1) == 1
    assert q.cost(1, 1) == 3
    assert q.cost(2, 1) == 3
    assert q.cost(2, 3) == 4
