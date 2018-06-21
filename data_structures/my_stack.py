class ListNode(object):

    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node
        return


class MyStack(object):

    def __init__(self, vals=[]):
        if not vals:
            self.head = None
        else:
            vals = [ListNode(x) for x in vals]
            self.head = vals[0]
            for n1, n2 in zip(vals, vals[1:]):
                n1.next = n2
        return

    def push(self, val):
        if not self.head:
            self.head = ListNode(val)
        else:
            node = ListNode(val)
            node.next = self.head
            self.head = node
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


if __name__ == '__main__':

    mq = MyStack()
    for x in range(10):
        mq.push(x)
    print(mq)
    print(mq.pop())
    mq.push(420)
    print(mq)
    print(mq.pop())
    print(mq.pop())
    print(mq.pop())
    print(mq)
