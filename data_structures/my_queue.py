from queue import Queue


class ListNode(object):
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node
        return


class MyQueue(object):
    def __init__(self, vals=[]):
        if not vals:
            self.head = None
            self.tail = None
        else:
            vals = [ListNode(x) for x in vals]
            self.head = vals[0]
            for n1, n2 in zip(vals, vals[1:]):
                n1.next = n2
            self.tail = n2 if n2 else self.head
        return

    def put(self, val):
        if not self.head:
            self.head = ListNode(val)
            self.tail = self.head
        else:
            self.tail.next = ListNode(val)
            self.tail = self.tail.next
        return

    def pop(self):
        popped = self.head
        self.head = popped.next
        popped.next = None
        return popped.val

    def __repr__(self):
        node = self.head
        out = []
        while node:
            out.append(node.val)
            node = node.next
        return str(out)


if __name__ == "__main__":

    mq = MyQueue()
    q = Queue()
    for x in range(10):
        mq.put(x)
        q.put(x)
    print(mq)
    print(q)
    print(mq.pop())
    print(q.get())
    mq.put(204)
    q.put(204)
    print(mq)
    print(str(q))
    print(mq.pop())
    print(mq.pop())
    print(mq.pop())
    print(q.get())
    print(q.get())
    print(q.get())
    print(mq)
    print(str(q))
