from .element import Element


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def enqueue(self, x):
        elem = Element(key=x)

        if self.head is None:
            self.head = elem
        else:
            self.tail.next = elem
        self.tail = elem
        self.len += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception('Underflow Error')

        output = self.head.key
        self.head = self.head.next
        self.len -= 1

        return output

    def is_empty(self):
        return self.head is None

    def __str__(self):
        if self.is_empty():
            raise Exception('Empty Queue')

        output = ''
        actual = self.head

        while actual is not None:
            output += str(actual.key) + ' '
            actual = actual.next

        return output
