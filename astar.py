import argparse
import random

import numpy as np

from astaral import Astaral
from graph import Graph
from window import Window


def main(args):
    size = [int(args.n), int(args.n)]
    tmparr = np.ones(size, dtype=np.int)

    # set random spot as blockage
    for _ in range(10):
        rand = random.randint(0, size[0] - 1)
        rand2 = random.randint(0, size[0] - 1)
        tmparr[rand, rand2] = 99

    astar = Astaral(size[0])
    graph = Graph(tmparr)

    window = Window(size[0])
    window.start()
    window.boxes = tmparr

    dist, queue = astar.shortest_path(window, graph)
    # print(dist, queue)
    # window.stop()
    window.stop()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", help="number of box", default=30)
    args = parser.parse_args()

    main(args)
