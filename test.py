import unittest

from pqueue.pqueue import Heap


class Test(unittest.TestCase):
    def test_heap(self):
        heap = Heap()

        for i in range(10):
            heap.insert(i, "1")

        heap.decrease_key(5, 100)
        test = [x for x in range(10) if x != 5]
        test.append(100)

        while not heap.isEmpty():
            self.assertEqual(heap.find_min().key, test.pop(0))
            heap.delete_min()
