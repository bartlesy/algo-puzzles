class BinHeap(object):
    """min heap implementation"""

    def __init__(self):
        # zero is unused but useful for integer division later
        self.heap_list = [0]
        self.current_size = 0

    def _swap_idx(self, i1, i2):
        self.heap_list[i1], self.heap_list[i2] = (
            self.heap_list[i2],
            self.heap_list[i1],
        )
        return

    def percolate(self, i):
        if not i // 2:
            return
        if self.heap_list[i] < self.heap_list[i // 2]:
            self._swap_idx(i, i // 2)
        self.percolate(i // 2)
        return

    def insert(self, x):
        self.heap_list.append(x)
        self.current_size += 1
        self.percolate(self.current_size)
        return

    def min_child(self, i):
        if (i * 2 + 1) > self.current_size:
            res = i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                res = i * 2
            else:
                res = i * 2 + 1
        return res

    def sink(self, i):
        if (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self._swap_idx(i, mc)
            self.sink(mc)
        return

    def del_min(self):
        # note - min is at 1 because of the placeholder 0
        ret_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[-1]
        self.current_size -= 1
        self.heap_list.pop()
        self.sink(1)
        return ret_val

    def build_heap(self, in_list):
        i = len(in_list) // 2
        self.current_size = len(in_list)
        self.heap_list = [0] + in_list
        while i > 0:
            self.sink(i)
            i -= 1
        return


if __name__ == "__main__":
    bh = BinHeap()
    bh.build_heap([9, 5, 6, 2, 3])
    print(bh.heap_list)
    bh.insert(1)
    print(bh.heap_list)
    bh.insert(2)
    bh.insert(2)
    bh.insert(2)
    print(bh.heap_list)

    while len(bh.heap_list) > 1:
        print(bh.del_min())
