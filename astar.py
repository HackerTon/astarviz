import argparse
import random

import numpy as np

from astaral.astaral import Astaral
from window.window import Window


def block2adja(box):
    ops = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    height = len(box)
    width = len(box[0])

    vertices = {i: [] for i in range(width * height)}

    for i in range(width):
        for j in range(height):
            vertex = (j * width) + i

            if box[i, j] != 99:
                for op in ops:
                    x = i + op[0]
                    y = j + op[1]

                    vertexb = (y * width) + x

                    if 0 <= x < width and 0 <= y < height and box[x, y] != 99:
                        vertices[vertex].append((vertexb, 5))

    return vertices


def main(args):
    size = [args.n, args.n]

    tmparr = np.ones(size, dtype=np.int)

    for _ in range(10):
        rand = random.randint(0, size[0] - 1)
        rand2 = random.randint(0, size[0] - 1)
        tmparr[rand, rand2] = 99

    astar = Astaral(size[0])

    testarr = block2adja(tmparr)

    window = Window(size[0])
    window.start()
    window.boxes = tmparr

    astar.shortest_path(window, testarr)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', help='number of box', default=30)
    args = parser.parse_args()

    main(args)

# %%
