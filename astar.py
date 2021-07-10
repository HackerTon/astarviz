import argparse
import random
from time import sleep

import numpy as np

from astaral import Astaral
from graph import Graph
from window import Window


def main(args):
    size = [int(args.n), int(args.n)]
    tmparr = np.ones(size, dtype=np.int)

    # set random spot as blockage
    for _ in range(int(args.b)):
        rand = random.randint(0, size[0] - 1)
        rand2 = random.randint(0, size[0] - 1)
        tmparr[rand, rand2] = Graph.BLOCK

    # make sure the last block is always free
    tmparr[size[0] - 1, size[1] - 1] = Graph.NON_BLOCK

    astar = Astaral(size[0])
    graph = Graph(tmparr)

    window = Window(size[0])
    window.start()
    window.boxes = tmparr

    dist, prev = astar.shortest_path(window, graph, 0, size[0] * size[1] - 1)

    print("Program Ended!")
    print("Type 'e' to delete")
    while input() != "e":
        sleep(1)
    window.stop()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", help="number of box", default=30)
    parser.add_argument("-b", help="number of blackbox", default=250)
    args = parser.parse_args()

    main(args)
