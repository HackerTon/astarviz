import numpy as np

# convert block format to linkedlist
# adjacent format graph
def block2adja(box, size):
    ops = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    height, width = size

    vertices = {i: [] for i in range(width * height)}

    for i in range(width):
        for j in range(height):
            vertex = (j * width) + i

            if box[i, j] != 99:
                for op in ops:
                    x = i + op[0]
                    y = j + op[1]

                    vertexb = (y * width) + x

                    if 0 <= x < width and 0 <= y < height and box[x, y] != 99:
                        vertices[vertex].append((vertexb, 5))

    return vertices


class Graph:
    def __init__(self, box) -> None:
        self.size = (len(box), len(box[0]))
        self.vertices = block2adja(box, self.size)