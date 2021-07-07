import math
import time
from typing import List

import numpy as np
from graph import Graph
from pqueue.pqueue import Heap
from window import Window


def create_zeros(n):
    return np.zeros([n ** 2])


# find xy coordinate from vertex
def xy_finder(vertex, size: tuple):
    return [vertex // size[0], vertex % size[1]]


def l2_distance(origin: List, target: List):
    x_ = origin[0] - target[0]
    y_ = origin[1] - target[1]

    return math.sqrt(x_ ** 2 + y_ ** 2)


def l1_distance(origin: List, target: List):
    x_ = origin[0] - target[0]
    y_ = origin[1] - target[1]

    return math.sqrt(abs(x_) + abs(y_))


# slow search in array
def find_min(prev: List, dist: List):
    origin_min = float("+inf")
    index = None
    for i in range(len(prev)):
        if prev[i] == 0 and dist[i] < origin_min:
            dist[i] = i
            index = i

    return index


class Astaral:
    def __init__(self, n=13):
        self.n = n
        self.u = None
        self.count = 0
        self.dist = None
        self.queue = None
        self.list = []

    # total swiping of all blocks
    # check for every single block in the map
    def shortest_path(self, window: Window, graph: Graph):
        dist = create_zeros(self.n)
        prev = [0] * self.n * self.n
        heap = Heap()

        initial_node = self.n * 15 + 15
        # heap.insert(0, initial_node)

        # fill the dist array with zeroes
        for i in graph.vertices.keys():
            dist[i] = float("+inf")
        dist[initial_node] = 0

        if window is None:
            running = True
        else:
            running = window.events()

        while 0 in prev and running:
            # node = heap.find_min()
            # heap.delete_min()
            u = find_min(prev, dist)

            # u = node.value  # is the index of graph

            # Color the box inside of GUI engine
            if window is not None:
                y, x = xy_finder(u, (self.n, self.n))
                window.boxes[x][y] = 3

            # visit all adjacent vertices from u
            for vertex in graph.vertices[u]:
                # z is node index
                z = vertex[0]
                weight = vertex[1]

                l2 = l1_distance(
                    xy_finder(z, (self.n, self.n)),
                    [29, 29],
                )

                alt_distance = dist[u] + weight

                if alt_distance < dist[z]:
                    dist[z] = alt_distance + l2
                    # heap.insert(dist[z], z)

                # u index is marked
                # u is no longer visited
                prev[u] = 1

            time.sleep(0.1)
            running = window.events()

        return dist, prev
