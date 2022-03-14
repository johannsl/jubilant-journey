from func_game_2 import play_bowling


# Simple score tests
def test0():
    score = play_bowling([1, 1] + [0] * 18)
    assert score == 2


def test1():
    score = play_bowling([10] + [0] * 18)
    assert score == 10


# Spare tests
def test2():
    score = play_bowling([5, 5, 5, 5] + [0] * 16)
    assert score == 25


def test3():
    score = play_bowling([1, 9, 0, 9] + [0] * 16)
    assert score == 19


def test4():
    score = play_bowling([5, 5, 10] + [0] * 16)
    assert score == 30


def test5():
    score = play_bowling([10, 10] + [0] * 16)
    # assert score == 20
    assert score == 30


# Strike tests
def test6():
    score = play_bowling([1, 1, 1, 1, 1, 1] + [0] * 14)
    assert score == 6


def test7():
    score = play_bowling([3, 3, 3, 3, 3, 3] + [0] * 14)
    assert score == 18


def test8():
    score = play_bowling([10, 10, 10] + [0] * 14)
    assert score == 60


def test9():
    score = play_bowling([10, 5, 5, 5, 5] + [0] * 14)
    assert score == 45


def test10():
    score = play_bowling([10, 0, 0, 0, 0] + [0] * 14)
    assert score == 10


def test11():
    score = play_bowling([1, 9, 10, 1, 1] + [0] * 14)
    assert score == 34


# Tenth frame tests
def test12():
    score = play_bowling([0] * 18 + [1, 1])
    assert score == 2


def test13():
    score = play_bowling([0] * 18 + [5, 5, 0])
    assert score == 10


def test14():
    score = play_bowling([0] * 18 + [5, 5, 1])
    assert score == 11


def test15():
    score = play_bowling([0] * 18 + [5, 5, 10])
    assert score == 20


def test16():
    score = play_bowling([0] * 18 + [10, 5, 5])
    assert score == 20


def test17():
    score = play_bowling([0] * 18 + [10, 5, 10])
    assert score == 25


def test18():
    score = play_bowling([0] * 18 + [10, 10, 10])
    assert score == 30


# Full game tests
def test19():
    score = play_bowling([0] * 20)
    assert score == 0


def test20():
    score = play_bowling([1] * 20)
    assert score == 20


def test21():
    score = play_bowling([5] * 21)
    assert score == 150


def test22():
    score = play_bowling([10] * 12)
    assert score == 300


def test23():
    score = play_bowling([9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9])
    assert score == 190


def test24():
    score = play_bowling([10, 0, 0, 10, 0, 0, 10, 0, 0, 10, 0, 0, 10, 0, 0])
    assert score == 50


def test25():
    score = play_bowling([10, 10, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    assert score == 120


def test26():
    score = play_bowling([0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 1])
    assert score == 101


def test27():
    score = play_bowling([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 1, 1, 2, 2, 3, 3, 4, 4, 10, 10, 10])
    assert score == 115


def test28():
    score = play_bowling([1, 4, 4, 5, 6, 4, 5, 5, 10, 0, 1, 7, 3, 6, 4, 10, 2, 8, 6])
    assert score == 133


def test29():
    score = play_bowling([8, 0, 7, 0, 5, 3, 9, 1, 9, 1, 10, 8, 0, 5, 1, 3, 7, 9, 0])
    assert score == 122


def test30():
    score = play_bowling([8, 2, 9, 0, 4, 4, 7, 2, 9, 0, 10, 10, 8, 0, 3, 5, 9, 1, 7])
    assert score == 133
