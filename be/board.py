import numpy as np


class Board:

    def __init__(self, board=None):
        if board is None:
            self.board = np.zeros((9, 9))
            self.dim = 3
        else:
            self.board = np.array(board)
            self.dim = int(np.sqrt(self.board.shape[0]))

    def get_square(self, n):
        row_from = self.dim * (n / self.dim)
        row_to = ((n / self.dim) + 1) * self.dim
        col_from = self.dim * (n % self.dim)
        col_to = self.dim * ((n % self.dim) + 1)
        return self.board[row_from:row_to, col_from:col_to]

    def get_row(self, n):
        return self.board[n]

    def get_column(self, n):
        return self.board[:, n]

    def get_penalties_of_row(self, n):
        return self.board[n].shape[0] - np.unique(self.board[n]).shape[0]

    def get_penalties_of_column(self, n):
        return self.board[:, n].shape[0] - np.unique(self.board[:, n]).shape[0]

    def get_penalties_of_square(self, n):
        square = self.get_square(n)
        return square.shape[0]*square.shape[1] - np.unique(square).shape[0]
