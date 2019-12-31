import numpy as np


class Wgraph:
    def __init__(self, size=None):
        if size is None:
            size = [13, 13]

        self.board = np.zeros(size)

    def __getitem__(self, item):
        return self.board[item[0]][item[1]]

    def read(self):
        return self.board
