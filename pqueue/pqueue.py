from typing import List


class Node:
    def __init__(self, key, value, leftchild, sibling):
        self.key = key
        self.value = value
        self.leftchild = leftchild
        self.sibling = sibling

    def addChild(self, node):
        if self.leftchild is None:
            self.leftchild = node
        else:
            node.sibling = self.leftchild
            self.leftchild = node


class Heap:
    def __init__(self):
        self.head = None

    def find_min(self) -> Node:
        return self.head

    def isEmpty(self):
        return True if self.head is None else False

    @staticmethod
    def _merge(nodeA: Node, nodeB: Node):
        if nodeA is None:
            return nodeB
        if nodeB is None:
            return nodeA

        if nodeA.key < nodeB.key:
            nodeA.addChild(nodeB)
            return nodeA
        else:
            nodeB.addChild(nodeA)
            return nodeB

    @staticmethod
    def _twopassmerge(node: Node):
        if node is None or node.sibling is None:
            return node
        else:
            heapA = node
            heapB = node.sibling
            newNode = node.sibling.sibling

            heapA.sibling = None
            heapB.sibling = None

            points: List = []
            while True:
                if newNode is None or newNode.sibling is None:
                    while len(points) != 0:
                        node = points.pop(-1)

                        newNode = Heap._merge(node, newNode)
                    break

                loopa = newNode

                points.append(newNode)

                newNode = newNode.sibling
                loopa.sibling = None

            return Heap._merge(Heap._merge(heapA, heapB), newNode)

    def insert(self, key, value):
        self.head = Heap._merge(self.head, Node(key, value, None, None))

    def delete_min(self):
        if not self.head is None:
            self.head = Heap._twopassmerge(self.head.leftchild)
            return True

        return False


# Test code
# heap = Heap()

# heap.insert(10, 1)
# heap.insert(11, 10)
# heap.insert(5, 20)
# heap.insert(9, 50)
# heap.insert(8, 10)
# heap.insert(7, 50)

# print(heap.find_min())
# heap.delete_min()
# print(heap.find_min().key)
