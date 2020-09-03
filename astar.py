import argparse
import time

import window
import numpy as np
import random

# from window.window import Window
from astaral.astaral import Astaral


def block2adja(boxex):
    n = len(boxex)

    adja = np.full([n * n, n * n], 999)

    ops = [[-1, 0], [0, 1], [0, -1], [1, 0]]

    # Using scanning window
    for i in range(0, n):
        for j in range(0, n):
            for op in ops:
                x = op[0] + i
                y = op[1] + j

                if 0 <= x < n:
                    if 0 <= y < n:
                        org = i * n + j
                        loc = x * n + y

                        adja[org, loc] = boxex[i][j]

    return adja


def main(args):
    # size = [args.n, args.n]
    size = [10] * 2
    # dispsize = [640 - (640 % size[0]), 640 - (640 % size[1])]

    # print(f'{dispsize}')

    tmparr = np.ones(size, dtype=np.int)

    for _ in range(size[0]):
        rand = random.randint(0, size[0] - 1)
        rand2 = random.randint(0, size[0] - 1)
        tmparr[rand, rand2] = 99

    astar = Astaral(size[0])

    # window = Window('A*', dispsize)
    # window.start()
    running = True

    testarr = block2adja(tmparr)

    current = random.randint(0, 139)
    goal = random.randint(0, 139)

    dist = astar.shortest_path(tmparr, testarr)
    print(dist)

    # while running:
    # window.boxes = tmparr

    # astar.shortest_path_step(window.boxes, testarr, current, goal)
    # astar.shortest_path_step(tmparr, testarr, current, goal)

    # running = window.events()

    # 60FPS
    # time.sleep(1 / 60)


if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument('-n', help='number of box', default=30)
    # args = parser.parse_args()

    main(None)
