from typing import List


class Node:
    def __init__(self, key, value, leftchild, sibling, parent=None):
        self.key = key
        self.value = value
        self.leftchild = leftchild
        self.sibling = sibling
        self.parent = parent

    def addChild(self, node):
        if self.leftchild is None:
            self.leftchild = node
            node.parent = self
        else:
            node.sibling = self.leftchild
            self.leftchild.parent = node
            self.leftchild = node


class Heap:
    def __init__(self):
        self.head: Node = None
        self.nodes = dict()
        self.head = None

    def find_min(self) -> Node:
        return self.head

    def isEmpty(self):
        return True if self.head is None else False

    def _merge(self, nodeA: Node, nodeB: Node):
        if nodeA is None:
            return nodeB
        if nodeB is None:
            return nodeA

        # node B becomes the child
        # of head
        if nodeA.key < nodeB.key:
            nodeA.addChild(nodeB)
            return nodeA
        # head
        # head becomes the child of
        else:
            nodeB.addChild(nodeA)
            return nodeB

    def _twopassmerge(self, node: Node):
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
                # if we reached the end of the list in sibling
                # we merge every node from the rightmost node.
                if newNode is None or newNode.sibling is None:
                    while not len(points) == 0:
                        # get the rightmost node
                        # store in array
                        # [n, n+1, n+2, -> rightmost]
                        node = points.pop(-1)

                        newNode = self._merge(node, newNode)
                    break

                loopa = newNode

                points.append(newNode)
                newNode = newNode.sibling
                loopa.sibling = None

            return self._merge(self._merge(heapA, heapB), newNode)

    def insert(self, key, value):
        self.nodes[key] = Node(key, value, None, None)
        self.head = self._merge(self.head, self.nodes[key])

    def delete_min(self):
        if not self.head is None:
            self.nodes.pop(self.head.key)
            self.head = self._twopassmerge(self.head.leftchild)

            return True

        return False

    def decrease_key(self, orig_key, next_key):
        if self.head.key == orig_key or next_key < self.head.key:
            self.head.key = next_key
        else:
            # find the node with the orig_key
            parent_node: Node = self.nodes[orig_key].parent
            node = None

            if parent_node.leftchild is not None:
                if parent_node.leftchild.key == orig_key:
                    node = parent_node.leftchild
                    parent_node.leftchild = None
            elif parent_node.sibling is not None:
                if parent_node.sibling.key == orig_key:
                    node = parent_node.sibling
                    parent_node.sibling = None
            else:
                # uncaught error, must investigate
                raise "Error"

            node.key = next_key
            self.nodes[node.key] = node
            # node.parent = None
            siblings = self._twopassmerge(node.sibling)
            node.sibling = None

            self.head = self._merge(self.head, node)
            self.head = self._merge(self.head, siblings)
