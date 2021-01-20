# data-structures

This repo contains the Python implementation of the main dynamic data structures, like linked lists, stacks, queues, and heaps. Beyond that, this repo contains some graph algorithms.

### data structure info

**Stack** implements a *last-in, first-out* (LIFO) policy. The *insert* operation on a stack is often called `push`, and the *delete* operation, which does not take an element argument, is often called `pop`. Both operation take `O(1)` time.

**Queue** implements a *first-in, first-out* (FIFO) policy. The FIFO property of a queue causes it to operate like a line of customers waiting to pay a cashier. We call the *insert* operation on a queue `enqueue`, and we call the *delete* operation `dequeue`. Like the stack operation pop, dequeue takes no element argument. Each operation takes `O(1)` time.

**Linked List** is a data structure in which the objects are arranged in a linear order. Unlike an array, however, in which the linear order is determined by the array indices, the order in a linked list is determined by a pointer in each object. A list may have one of several forms. It may be either singly linked or doubly linked, it may be sorted or not, and it may be circular or not. In a singly linked list, `insert` operation takes `O(1)` time while `search` and `delete` operations take `O(n)` time.

**Heap** is an array object that we can view as a nearly complete binary tree. Each node of the tree corresponds to an element of the array. The tree is completely filled on all levels except possibly the lowest, which is filled from the left up to a point.

Suppose A is a heap. The root of the tree is `A[i]`, and given an index `i` of a node, we can easily compute the indices f its parent, left child, and right child. There area two kinds of binary heaps: *max-heaps* and *min-heaps*. In both kinds, the values in the nodes satisfy a heap property, the specifics of which depend on the kind of the heap. In a max-heap, the max-heap property is that for every node `i` other than the root, `A[parent(i)] >= A[i]`, that is, the value of a node is at most the value of its parent. For the **heapsort algorithm**, we use ma-heaps. Min-heaps commonly implement priority queues. A **priority queue** is a data structure for maintaining a set `S` of elements, each with an associated value called a key. Among their other applications, we can use max-priority queues to schedule jobs on a shared computer. A min-priority queue can be used in an event-driven simulator and some graph algorithms.

The following pseudo-code implements the heapsort:

```
HEAPSORT(A):
    BUILD-MAX-HEAP(A)
    for i = A.length downto 2:
        exchange A[1] with A[i]
        A.heap-size = A.heap-size - 1
        MAX_HEAPIFY(A, 1)
```

The HEAPSORT procedure takes time `O(n lg n)`, since the call to BUILD-MAX-HEAP takes time `O(n)` and each of the `n - 1` calls to MAX-HEAPIFY takes time `O(lg n)`.

**Breadth-First Search** (BFS) is one of the simplest algorithms for searching a graph and the archetype for many important graph algorithms. Given a graph `G = (V, E)` and a distinguished source vertex `s`, breadth-first search systematically explores the edges of G to "discover" every vertex that is reachable form `s`. It computes the distance (smallest number of edges) from `s` to each reachable vertex. The total running time of the BFS procedure is `O(V + E)` using adjacency-list representation. The algorithm also uses a first-in, first-out queue `Q` to manage the set of gray vertices.

A **Topological Sort** of a directed acyclic graph (DAG) `G = (V, E)` is a linear ordering of all its vertices such that if `G` contains an edge `(u, v)`, then `u` appears before `v` in the ordering. We can view a topological sort of a graph as an ordering of its vertices along a horizontal line so that all directed edges go from left to right. Many applications use directed acyclic graphs to indicate precedences among events. We can perform a topological sort in time `O(V + E)`, since depth-first search takes `O(V + E)` time and it takes `O(1)` time to insert each of the `|V|` vertices onto the front of the linked list.

The following simple algorithm topologically sorts a dag:

```
TOPOLOGICAL-SORT(G):
    call DFS(G) to compute finishing times v.f for each vertex v
    as each vertex is finished, insert it onto the front of a linked list
    return the linked list of vertices
```

A **Minimum Spanning Tree** (MST) is a subset of the edges of a connected, edge-weighted undirected graph that connects all the vertices together, without any cycles and with the minimum possible total edge weight. Two famous algorithms for solving this problem are: Kruskal's algorithm and Prim's algorithm. We can easily make each of them run in time `O(E lg V)`using ordinary binary heaps.

The generic method manages a set of edges `A`, maintaining the following loop invariant: *Prior to each iteration, A is a subset of some minimum spanning tree*. At each step, we determine an edge `(u, v)` that we can add to `A` without violating this invariant, in the sense that, `A U {(u, v)}` is also a subset of a minimum spanning tree. We call such an edge a *safe edge* for `A`, since we can add it safely to `A` while maintaining the invariant.

This is an implementation of Kruskal's algorithm:

```
MST-KRUSKAL(G, w):
    A = empty set
    for each vertex v that belongs to G.V:
        MAKE-SET(v)
    sort the edges of G.E into nondecreasing order by weight w
    for each edge (u, v) that belongs to G.E, taken in nondecreasing order by weight:
        if FIND-SET(u) != FIND-SET(v):
        A = A U {(u, v)}
        UNION(u, v)
    return A
```

The total running time of Kruskal's algorithm is `O(E lg V)`.

**Dijkstra's algorithm** solves the **single-source shortest paths** problem on a weighted, directed graph `G = (V, E)` for the case in which all edge weights are nonnegative. This algorithm maintains a set `S` of vertices whose final shortest-path weights from the source `s` have already been determined. The algorithm repeatedly selects the vertex `u that belongs to V - S` with the minimum shortest-path estimate, adds `u` to `S`, and relaxes all edges leaving `u`. In the following implementation, we use a min-priority queue `Q` of vertices, keyed by their `d` values:

```
DIJKSTRA(G, w, s):
    INITIALIZE-SINGLE-SOURCE(G, s)
    S = empty set
    Q = G.V
    while Q is not empty:
    u = EXTRACT-MIN(Q)
    S = S U {u}
    for each vertex v that belongs to G.Adj[u]:
        RELAX(u, v, w)
```

where

```
INITIALIZE-SINGLE-SOURCE(G, s):
    for each vertex v that belongs to G.V:
        v.d = inf
        v.pi = NIL
    s.d = 0
```

and

```
RELAX(u, v, w):
if v.d > u.d + w(u, v):
    v.d = u.d + w(u, v)
    v.pi = u
```

The running time of Dijkstra's algorithm depends on how we implement the min-priority queue. One option takes `O(V^2)` time. We can achieve a running time of `O(V lg V + E)` by implementing the min-priority queue with a Fibonacci heap.

### implementations

- [X] stack
- [X] queue
- [X] linked list
- [ ] heap
- [ ] priority queue
- [ ] breadth-first search
- [ ] depth-first search
- [ ] topological sort
- [ ] minimum spanning tree (Kruskal's implementation)
- [ ] shortest-path (Dijkstra's implementation)
