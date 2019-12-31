import argparse
import time
import numpy as np
import random

from window.window import Window
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
    size = [args.n, args.n]
    dispsize = [640 - (640 % size[0]), 640 - (640 % size[1])]

    print(f'{dispsize}')

    tmparr = np.ones([args.n, args.n], dtype=np.int)

    for i in range(50):
        rand = random.randint(1, 12)
        rand2 = random.randint(1, 12)
        tmparr[rand, rand2] = 99

    astar = Astaral(args.n)

    window = Window('A*', dispsize)
    running = True
    window.start()

    testarr = block2adja(tmparr)

    while running:
        window.boxes = tmparr

        astar.shortest_path_step(window.boxes, testarr, random.randint(0, 139), random.randint(0, 139))

        print(astar.list)

        running = window.events()

        # 60FPS
        time.sleep(1 / 60)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', help='number of box', default=13)
    args = parser.parse_args()

    main(args)
