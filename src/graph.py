import numpy as np
from .queue import Queue


class Graph:
    def __init__(self, num_vertex):
        self.num_vertex = num_vertex
        self.G = np.zeros((self.num_vertex, self.num_vertex), dtype=int)

    def add_edge(self, u, v, w=1, directed=False):
        self.G[u, v] = w

        if not directed:
            self.G[v, u] = w

    def BFS(self, s):
        color = [0] * self.num_vertex
        d = [-1] * self.num_vertex
        pi = [None] * self.num_vertex

        color[s] = 1
        d[s] = 0
        Q = Queue()

        Q.enqueue(s)

        while not Q.is_empty():
            u = Q.dequeue()

            for v in range(0, self.num_vertex):
                if self.G[u, v] == 1 and color[v] == 0:
                    color[v] = 1
                    d[v] = d[u] + 1
                    pi[v] = u
                    Q.enqueue(v)

        return d, pi

    def print_path(self, pi, s, v):
        if v == s:
            print(s)
        elif pi[v] is None:
            print('No path from {} to {} exists'.format(s, v))
        else:
            self.print_path(pi, s, pi[v])
            print(v)
