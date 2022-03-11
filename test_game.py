from game import Game
from helper import helper


# Simple score tests
def test0():
    game = Game(2)
    game.roll(1)
    game.roll(1)
    assert game.score == 2


def test1():
    game = Game(2)
    game.roll(10)
    assert game.score == 10


# Spare tests
def test2():
    game = Game(3)
    game.roll(5)
    game.roll(5)
    game.roll(5)
    game.roll(5)
    assert game.score == 25


def test3():
    game = Game(3)
    game.roll(1)
    game.roll(9)
    game.roll(0)
    game.roll(9)
    assert game.score == 19


def test4():
    game = Game(3)
    game.roll(5)
    game.roll(5)
    game.roll(10)
    assert game.score == 30


def test5():
    game = Game(3)
    helper(game, [10, 10])
    # assert game.score == 20
    assert game.score == 30


# Strike tests
def test6():
    game = Game(4)
    helper(game, [1, 1, 1, 1, 1, 1])
    assert game.score == 6


def test7():
    game = Game(4)
    helper(game, [3, 3, 3, 3, 3, 3])
    assert game.score == 18


def test8():
    game = Game(4)
    helper(game, [10, 10, 10])
    assert game.score == 60


def test9():
    game = Game(4)
    helper(game, [10, 5, 5, 5, 5])
    assert game.score == 45


def test10():
    game = Game(4)
    helper(game, [10, 0, 0, 0, 0])
    assert game.score == 10


def test11():
    game = Game(4)
    helper(game, [1, 9, 10, 1, 1])
    assert game.score == 34


# Tenth frame tests
def test12():
    game = Game(1)
    helper(game, [1, 1])
    assert game.score == 2


def test13():
    game = Game(1)
    helper(game, [5, 5, 0])
    assert game.score == 10


def test14():
    game = Game(1)
    helper(game, [5, 5, 1])
    assert game.score == 11


def test15():
    game = Game(1)
    helper(game, [5, 5, 10])
    assert game.score == 20


def test16():
    game = Game(1)
    helper(game, [10, 5, 5])
    assert game.score == 20


def test17():
    game = Game(1)
    helper(game, [10, 5, 10])
    assert game.score == 25


def test18():
    game = Game(1)
    helper(game, [10, 10, 10])
    assert game.score == 30


# Full game tests
def test19():
    game = Game(10)
    helper(game, [0] * 20)
    assert game.score == 0


def test20():
    game = Game(10)
    helper(game, [1] * 20)
    assert game.score == 20


def test21():
    game = Game(10)
    helper(game, [5] * 21)
    assert game.score == 150


def test22():
    game = Game(10)
    helper(game, [10] * 12)
    assert game.score == 300


def test23():
    game = Game(10)
    helper(game, [9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9])
    assert game.score == 190


def test24():
    game = Game(10)
    helper(game, [10, 0, 0, 10, 0, 0, 10, 0, 0, 10, 0, 0, 10, 0, 0])
    assert game.score == 50


def test25():
    game = Game(10)
    helper(game, [10, 10, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    assert game.score == 120


def test26():
    game = Game(10)
    helper(game, [0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 1])
    assert game.score == 101


def test27():
    game = Game(10)
    helper(game, [1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 1, 1, 2, 2, 3, 3, 4, 4, 10, 10, 10])
    assert game.score == 115


def test28():
    game = Game(10)
    helper(game, [1, 4, 4, 5, 6, 4, 5, 5, 10, 0, 1, 7, 3, 6, 4, 10, 2, 8, 6])
    assert game.score == 133
