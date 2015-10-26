
import numpy as np
import unittest
from board import Board


class TestSquaresOfBoard(unittest.TestCase):
    def setUp(self):
        board = np.array([[0, 0, 0, 1, 1, 1, 2, 2, 2],
                          [0, 0, 0, 1, 1, 1, 2, 2, 2],
                          [0, 0, 0, 1, 1, 1, 2, 2, 2],
                          [3, 3, 3, 4, 4, 4, 5, 5, 5],
                          [3, 3, 3, 4, 4, 4, 5, 5, 5],
                          [3, 3, 3, 4, 4, 4, 5, 5, 5],
                          [6, 6, 6, 7, 7, 7, 8, 8, 8],
                          [6, 6, 6, 7, 7, 7, 8, 8, 8],
                          [6, 6, 6, 7, 7, 7, 8, 8, 8]])
        self.b = Board(board)

    def test_get_square_0(self):
        self.assertTrue((self.b.get_square(0) == 0).all())

    def test_get_square_1(self):
        self.assertTrue((self.b.get_square(1) == 1).all())

    def test_get_square_2(self):
        self.assertTrue((self.b.get_square(2) == 2).all())

    def test_get_square_3(self):
        self.assertTrue((self.b.get_square(3) == 3).all())

    def test_get_square_4(self):
        self.assertTrue((self.b.get_square(4) == 4).all())

    def test_get_square_5(self):
        self.assertTrue((self.b.get_square(5) == 5).all())

    def test_get_square_6(self):
        self.assertTrue((self.b.get_square(6) == 6).all())

    def test_get_square_7(self):
        self.assertTrue((self.b.get_square(7) == 7).all())

    def test_get_square_8(self):
        self.assertTrue((self.b.get_square(8) == 8).all())


class TestRowsOfBoard(unittest.TestCase):
    def setUp(self):
        board = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [2, 2, 2, 2, 2, 2, 2, 2, 2],
                          [3, 3, 3, 3, 3, 3, 3, 3, 3],
                          [4, 4, 4, 4, 4, 4, 4, 4, 4],
                          [5, 5, 5, 5, 5, 5, 5, 5, 5],
                          [6, 6, 6, 6, 6, 6, 6, 6, 6],
                          [7, 7, 7, 7, 7, 7, 7, 7, 7],
                          [8, 8, 8, 8, 8, 8, 8, 8, 8]])
        self.b = Board(board)

    def test_get_row_0(self):
        self.assertTrue((self.b.get_row(0) == 0).all())

    def test_get_row_1(self):
        self.assertTrue((self.b.get_row(1) == 1).all())

    def test_get_row_2(self):
        self.assertTrue((self.b.get_row(2) == 2).all())

    def test_get_row_3(self):
        self.assertTrue((self.b.get_row(3) == 3).all())

    def test_get_row_4(self):
        self.assertTrue((self.b.get_row(4) == 4).all())

    def test_get_row_5(self):
        self.assertTrue((self.b.get_row(5) == 5).all())

    def test_get_row_6(self):
        self.assertTrue((self.b.get_row(6) == 6).all())

    def test_get_row_7(self):
        self.assertTrue((self.b.get_row(7) == 7).all())

    def test_get_row_8(self):
        self.assertTrue((self.b.get_row(8) == 8).all())


class TestColumnsOfBoard(unittest.TestCase):
    def setUp(self):
        board = np.array([[0, 1, 2, 3, 4, 5, 6, 7, 8],
                          [0, 1, 2, 3, 4, 5, 6, 7, 8],
                          [0, 1, 2, 3, 4, 5, 6, 7, 8],
                          [0, 1, 2, 3, 4, 5, 6, 7, 8],
                          [0, 1, 2, 3, 4, 5, 6, 7, 8],
                          [0, 1, 2, 3, 4, 5, 6, 7, 8],
                          [0, 1, 2, 3, 4, 5, 6, 7, 8],
                          [0, 1, 2, 3, 4, 5, 6, 7, 8],
                          [0, 1, 2, 3, 4, 5, 6, 7, 8]])
        self.b = Board(board)

    def test_get_column_0(self):
        self.assertTrue((self.b.get_column(0) == 0).all())

    def test_get_column_1(self):
        self.assertTrue((self.b.get_column(1) == 1).all())

    def test_get_column_2(self):
        self.assertTrue((self.b.get_column(2) == 2).all())

    def test_get_column_3(self):
        self.assertTrue((self.b.get_column(3) == 3).all())

    def test_get_column_4(self):
        self.assertTrue((self.b.get_column(4) == 4).all())

    def test_get_column_5(self):
        self.assertTrue((self.b.get_column(5) == 5).all())

    def test_get_column_6(self):
        self.assertTrue((self.b.get_column(6) == 6).all())

    def test_get_column_7(self):
        self.assertTrue((self.b.get_column(7) == 7).all())

    def test_get_column_8(self):
        self.assertTrue((self.b.get_column(8) == 8).all())


class TestPenaltiesOfBoard(unittest.TestCase):
    def setUp(self):
        board = np.array([[0, 1, 2, 3, 4, 1, 6, 7, 8],
                          [0, 1, 8, 3, 8, 5, 1, 7, 8],
                          [0, 1, 2, 3, 4, 5, 6, 7, 8],
                          [0, 1, 2, 3, 4, 5, 6, 7, 8],
                          [0, 1, 2, 3, 4, 5, 6, 7, 8],
                          [0, 1, 2, 3, 4, 5, 6, 7, 8],
                          [0, 1, 2, 3, 4, 5, 6, 7, 8],
                          [0, 1, 2, 3, 4, 5, 6, 7, 8],
                          [0, 1, 2, 3, 4, 5, 6, 7, 8]])
        self.b = Board(board)

    def test_compute_penalties_of_row_0_return_1(self):
        self.assertEquals(self.b.get_penalties_of_row(0), 1)

    def test_compute_penalties_of_row_1_return_3(self):
        self.assertEquals(self.b.get_penalties_of_row(1), 3)

    def test_compute_penalties_of_row_2_return_0(self):
        self.assertEquals(self.b.get_penalties_of_row(2), 0)

    def test_compute_penalties_of_column_0_return_8(self):
        self.assertEquals(self.b.get_penalties_of_column(0), 8)

    def test_compute_penalties_of_column_2_return_7(self):
        self.assertEquals(self.b.get_penalties_of_column(2), 7)

    def test_compute_penalties_of_square_0_return_5(self):
        self.assertEquals(self.b.get_penalties_of_square(0), 5)

if __name__ == '__main__':
    unittest.main()
