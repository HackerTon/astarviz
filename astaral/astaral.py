import math
import time
from typing import List, Set

import numpy as np
from graph import Graph
from window import Window

# TODO: Add a new table for storing the current to neighbor weight


def create_zeros(n):
    return np.zeros([n**2])


# find xy coordinate from vertex
def xy_finder(vertex, size: tuple):
    return [vertex // size[0], vertex % size[1]]


def l2_distance(origin: List, target: List):
    x_ = origin[0] - target[0]
    y_ = origin[1] - target[1]

    return math.sqrt(x_**2 + y_**2)


def l1_distance(origin: List, target: List):
    x_ = origin[0] - target[0]
    y_ = origin[1] - target[1]
    return math.sqrt(abs(x_) + abs(y_))


# slow search in array
def find_min(open_node: Set, score: List):
    origin_min = float("+inf")
    index = None
    for node in open_node:
        if score[node] < origin_min:
            origin_min = score[node]
            index = node
    return index


class Astaral:
    def __init__(self, n=13):
        self.n = n

    # total swiping of all blocks
    # check for every single block in the map
    def shortest_path(
        self,
        window: Window,
        graph: Graph,
        initial_node: int,
        final_node: int,
    ):
        score = create_zeros(self.n)
        score_with_h = create_zeros(self.n)
        open_nodes = {x for x in range(self.n * self.n)}

        # fill the dist array with zeroes
        for i in graph.vertices.keys():
            score[i] = float("+inf")
            score_with_h[i] = float("+inf")
        score[initial_node] = 0
        score_with_h[initial_node] = 0

        if window is None:
            running = True
        else:
            running = window.events()

        while len(open_nodes) != 0 and running:
            current_node = find_min(open_nodes, score)

            # # exit if final node is found
            if current_node == final_node:
                break

            # Color the box inside of GUI engine
            if window is not None:
                y, x = xy_finder(current_node, (self.n, self.n))
                window.boxes[x][y] = 3

            # mark u as visited
            open_nodes.remove(current_node)

            # visit all adjacent vertices from u
            for neighbor_node, _F in graph.vertices[current_node]:
                # weight has recalculate with l1
                weight = l1_distance(
                    xy_finder(current_node, (self.n, self.n)),
                    xy_finder(neighbor_node, (self.n, self.n)),
                )

                alt_distance = score[current_node] + weight
                if alt_distance < score[neighbor_node]:
                    l2 = 50 * l1_distance(
                        xy_finder(neighbor_node, (self.n, self.n)),
                        xy_finder(final_node, (self.n, self.n)),
                    )

                    score[neighbor_node] = alt_distance
                    score_with_h[neighbor_node] = alt_distance + l2
                    open_nodes.add(neighbor_node)

            time.sleep(0.01)
            running = window.events()
        return score, score_with_h, open_nodes
