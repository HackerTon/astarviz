import numpy as np
from pqueue.pqueue import Heap


def mindistance(dist, queue):
    minimum = 999
    minimum_index = 0

    for j in range(len(dist)):
        if queue[j] == 0 and dist[j] <= minimum:
            minimum = dist[j]
            minimum_index = j

    return minimum_index


def create_zeros(n):
    return np.zeros([n**2])


class Astaral:
    def __init__(self, n=13):
        self.n = n
        self.u = None
        self.count = 0
        self.dist = None
        self.queue = None
        self.list = []

    def shortest_path(self, map=None, graph=None):
        dist = create_zeros(self.n)
        queue = create_zeros(self.n)
        heap = Heap()

        heap.insert(0, 0)
        dist[0] = 0

        for i in range(1, len(dist) - 1):
            heap.insert(999, i)

            dist[i] = 999
            queue[i] = 0

        while not heap.isEmpty():
            u = heap.find_min().value
            heap.delete_min()

            # if vertext is visited, we skip
            if queue[u] == 0:
                queue[u] = 1  # mark vertext as visited

                x = u // self.n
                y = u % self.n

                map[x][y] = 1

                for j in range(len(dist)):
                    if queue[j] == 0 and graph[u][j] != 999 and dist[u] != 999 and (dist[u] + graph[u][j]) < dist[j]:
                        dist[j] = dist[u] + graph[u][j]

                        heap.insert(dist[j], j)

        return dist, queue

    def shortest_path_step(self, map=None, graph=None, current=None, goal=None):
        if self.count == 0:
            self.dist = np.zeros([self.n * self.n], dtype=np.int)
            self.queue = np.zeros([self.n * self.n], dtype=np.int)
            self.list = np.full([self.n * self.n], -1)

            for i in range(len(self.dist)):
                self.dist[i] = 999
                self.queue[i] = 0

            self.dist[current] = 0

        self.count += 1

        sx = goal // 13
        sy = goal - (sx * 13)

        map[sx, sy] = 3

        if self.count < len(self.dist):
            self.u = mindistance(self.dist, self.queue)
            self.queue[self.u] = 1

            previous = self.dist[goal]

            x = int(self.u / self.n)
            y = self.u % self.n

            for j in range(len(self.dist)):
                if self.queue[j] == 0 and graph[self.u][j] != 999 and self.dist[self.u] != 999 and (
                        self.dist[self.u] + graph[self.u][j]) < self.dist[j]:
                    self.dist[j] = self.dist[self.u] + graph[self.u][j]

                    self.list[j] = self.u

            if map[x][y] != 99:
                map[x][y] = 2

            if self.u == goal:
                map[x][y] = 3
                self.count = len(self.dist)

        return True
