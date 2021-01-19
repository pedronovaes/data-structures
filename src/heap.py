class Heap:
    def __init__(self, heap, heap_size):
        self.A = [-1] + heap
        self.length = len(heap)
        self.heap_size = heap_size

    def parent(self, i):
        return int(i / 2)

    def left(self, i):
        return 2 * i

    def right(self, i):
        return 2 * i + 1

    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)

        if l <= self.heap_size and self.A[l] > self.A[i]:
            largest = l
        else:
            largest = i

        if r <= self.heap_size and self.A[r] > self.A[largest]:
            largest = r

        # Exchange
        if largest != i:
            temp = self.A[i]
            self.A[i] = self.A[largest]
            self.A[largest] = temp

            self.max_heapify(largest)

    def build_max_heap(self):
        pass

    def min_heapify(self, i):
        pass

    def build_min_heap(self):
        pass

    def heapsort(self):
        pass

    def __str__(self):
        output = ''

        for i in range(1, self.heap_size):
            output += str(self.A[i]) + ' '

        return output
