from .element import Element


class Stack:
    def __init__(self):
        self.head = None
        self.len = 0

    def push(self, x):
        elem = Element(key=x, next=self.head)
        self.head = elem
        self.len += 1

    def pop(self):
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
            raise Exception('Empty Stack')

        output = ''
        actual = self.head

        while actual is not None:
            output += str(actual.key) + ' '
            actual = actual.next

        return output
