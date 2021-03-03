# linked list
# list
# dictionary(hashmap)
# queue  and stack

# linked list
# merge two sorted linked list in reverse order.
# e.g  a: 5->10->15->40
#         b: 2->3->20

# answer = 40->20->15->10->5->2

# Node of a linked list
class Node:
    def __init__(self, next=None, data=None):
        self.next = next
        self.data = data

    # Given two non-empty linked lists 'a' and 'b'


def SortedMerge(a, b):
    if a is None and b is None:
        return

    res = None

    while a is not None and b is not None:
        if a.key <= b.key:
            temp = a.next
            a.next = res
            res = a
            a = temp
        else:
            temp = b.next
            b.next = res
            res = b
            b = temp
    while a.next is not None:
        temp = a.next
        a.next = res
        res = a
        a = temp
    while b.next is not None:
        temp = b.next
        b.next = res
        res = b
        b = temp
    return res
#
