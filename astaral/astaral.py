import time
import numpy as np
from pqueue.pqueue import Heap
from window.window import Window


def create_zeros(n):
    return np.zeros([n ** 2])


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
    def shortest_path(self, window: Window = None, graph: dict = None):
        dist = create_zeros(self.n)
        queue = create_zeros(self.n)
        heap = Heap()

        heap.insert(0, 0)
        dist[0] = 0

        for i in graph.keys():
            if i != 0:
                heap.insert(9999, i)
                dist[i] = 9999

            queue[i] = 0

        if window is None:
            running = True
        else:
            running = window.events()

        while not heap.isEmpty() and running:
            node = heap.find_min()
            u = node.value  # is the index of graph
            heap.delete_min()

            if queue[u] == 0:  # if vertex is visited, we skip
                queue[u] = 1  # mark vertex as visited

                # Color the box inside of GUI engine
                if window is not None:
                    y = u // self.n
                    x = u % self.n
                    window.boxes[x][y] = 3

                for vertex in graph[u]:  # visit all adjacent vertices from u
                    z = vertex[0]  # z is node index
                    weight = vertex[1]

                    if dist[u] + weight < dist[z]:
                        dist[z] = dist[u] + weight
                        heap.insert(dist[z], z)

            time.sleep(0.1)
            running = window.events()

        return dist, queue
