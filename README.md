# data-structures

This repo contains the Python implementation of the main dynamic data structures, like linked lists, stacks, queues, and heaps. Beyond that, this repo contains some graph algorithms.

### data structure info

**Stack** implements a *last-in, first-out* (LIFO) policy. The *insert* operation on a stack is often called `push`, and the *delete* operation, which does not take an element argument, is often called `pop`. Both operation take `O(1)` time.

**Queue** implements a *first-in, first-out* (FIFO) policy. The FIFO property of a queue causes it to operate like a line of customers waiting to pay a cashier. We call the *insert* operation on a queue `enqueue`, and we call the *delete* operation `dequeue`. Like the stack operation pop, dequeue takes no element argument. Each operation takes `O(1)` time.

**Linked List** is a data structure in which the objects are arranged in a linear order. Unlike an array, however, in which the linear order is determined by the array indices, the order in a linked list is determined by a pointer in each object. A list may have one of several forms. It may be either singly linked or doubly linked, it may be sorted or not, and it may be circular or not. In a singly linked list, `insert` operation takes `O(1)` time while `search` and `delete` operations take `O(n)` time.

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
