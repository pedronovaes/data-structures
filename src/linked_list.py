from .element import Element


class LinkedList:
    def __init__(self):
        self.head = None
        self.len = 0

    def insert(self, x):
        elem = Element(key=x, next=self.head)
        self.head = elem
        self.len += 1

    def search(self, k):
        actual = self.head

        while actual is not None or actual.key != k:
            actual = actual.next

        return actual is not None

    def delete(self, x):
        if self.is_empty():
            raise Exception('Underflow Error')

        if self.head.key == x:
            self.head = self.head.next
        else:
            actual = self.head

            while actual.next is not None and actual.next.key != x:
                actual = actual.next

            if actual.next is None:
                return
            else:
                actual.next = actual.next.next

    def is_empty(self):
        return self.head is None

    def __str__(self):
        if self.is_empty():
            raise Exception('Empty List')

        output = ''
        actual = self.head

        while actual is not None:
            output += str(actual.key) + ' '
            actual = actual.next

        return output
