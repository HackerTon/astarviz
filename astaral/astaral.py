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
        queue = create_zeros(self.n)
        heap = Heap()

        heap.insert(0, 0)
        dist[0] = 0

        for i in graph.vertices.keys():
            if i != 0:
                dist[i] = 9999
            queue[i] = 0

        if window is None:
            running = True
        else:
            running = window.events()

        while not heap.isEmpty() and running:
            node = heap.find_min()
            u = node.value  # is the index of graph
            while heap.delete_min():
                pass

            # print(node.key, node.value)

            if queue[u] == 0:  # if vertex is visited, we skip
                queue[u] = 1  # mark vertex as visited

                # Color the box inside of GUI engine
                if window is not None:
                    y, x = xy_finder(u, (self.n, self.n))
                    window.boxes[x][y] = 3

                for vertex in graph.vertices[u]:  # visit all adjacent vertices from u
                    z = vertex[0]  # z is node index
                    weight = vertex[1]

                    l2 = l2_distance(
                        xy_finder(z, (self.n, self.n)),
                        [29, 29],
                    )

                    if dist[u] + weight + l2 < dist[z]:
                        dist[z] = dist[u] + weight + l2
                        # print(f"weight {dist[z]} at {z}")
                        heap.insert(dist[z], z)

            time.sleep(0.1)
            running = window.events()

        return dist, queue
