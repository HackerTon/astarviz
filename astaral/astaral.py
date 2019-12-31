import numpy as np


def minDistance(dist, queue):
    mini = 999
    miniindex = 0

    for j in range(len(dist)):
        if queue[j] == 0 and dist[j] <= mini:
            mini = dist[j]
            miniindex = j

    return miniindex


class Astaral:
    def __init__(self, n=13):
        self.n = n
        self.u = None
        self.count = 0
        self.dist = None
        self.queue = None
        self.list = []

    def shortest_path(self, map=None, graph=None, current=None, goal=None):
        dist = np.zeros([self.n * self.n], dtype=np.int)
        queue = np.zeros([self.n * self.n], dtype=np.int)

        for i in range(len(dist)):
            dist[i] = 999
            queue[i] = 0

        dist[0] = 0
        print(map)

        for i in range(len(dist) - 1):
            u = minDistance(dist, queue)
            queue[u] = 1

            x = int(u / self.n)
            y = u % self.n

            print(x, y)

            map[x][y] = 1

            for j in range(len(dist)):
                if queue[j] == 0 and graph[u][j] != 999 and dist[u] != 999 and (dist[u] + graph[u][j]) < dist[j]:
                    dist[j] = dist[u] + graph[u][j]

        return dist

    def shortest_path_step(self, map=None, graph=None, current=None, goal=None):
        if self.count == 0:
            self.dist = np.zeros([self.n * self.n], dtype=np.int)
            self.queue = np.zeros([self.n * self.n], dtype=np.int)

            for i in range(len(self.dist)):
                self.dist[i] = 999
                self.queue[i] = 0

            self.dist[current] = 0

        self.count += 1

        if self.count < len(self.dist):
            self.u = minDistance(self.dist, self.queue)
            self.queue[self.u] = 1

            previous = self.dist[goal]

            x = int(self.u / self.n)
            y = self.u % self.n

            for j in range(len(self.dist)):
                if self.queue[j] == 0 and graph[self.u][j] != 999 and self.dist[self.u] != 999 and (
                        self.dist[self.u] + graph[self.u][j]) < self.dist[j]:
                    self.dist[j] = self.dist[self.u] + graph[self.u][j]

            if map[x][y] != 99:
                map[x][y] = 2

            if self.u == goal:
                map[x][y] = 3
                self.count = len(self.dist)

            if self.queue[goal] != 1 and previous != self.dist[goal]:
                self.list.append(self.u)

        return True
