from docketpy import mathx


def test_square_root():
    print("Testing square_root()...")
    assert mathx.square_root(4) == 2


def test_cube_root():
    assert mathx.cube_root(8) == 2


def test_fourth_root():
    assert mathx.fourth_root(16) == 2


def test_fifth_root():
    assert mathx.fifth_root(32) == 2


def test_sixth_root():
    assert mathx.sixth_root(64) == 2
