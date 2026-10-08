class Node:

    def __init__(self, item, next_node):
        self.item = item
        self.next = next_node


class LinkIterator:

    def __init__(self, current):
        self.current = current

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration()
        else:
            item = self.current.item
            self.current = self.current.next
            return item


class Bag:

    def __init__(self):
        self.first = None
        self.n = 0

    def __str__(self):
        return " ".join(str(i) for i in self)

    def __iter__(self):
        return LinkIterator(self.first)

    def size(self):
        return self.n

    def is_empty(self):
        return self.first is None

    def add(self, item):
        oldfirst = self.first
        self.first = Node(item, oldfirst)
        self.n += 1


class Digraph:

    def __init__(self, v=0, **kwargs):
        self.V = v
        self.E = 0
        self.adj = [Bag() for _ in range(self.V)]

        if 'file' in kwargs:
            in_file = kwargs['file']
            self.V = int(in_file.readline())
            self.adj = [Bag() for _ in range(self.V)]
            E = int(in_file.readline())
            for i in range(E):
                v, w = in_file.readline().split()
                self.add_edge(int(v), int(w))

    def __str__(self):
        s = "%d vertices, %d edges\n" % (self.V, self.E)
        s += "\n".join("%d: %s" % (v, " ".join(str(w)
                                               for w in self.adj[v])) for v in range(self.V))
        return s

    def add_edge(self, v, w):
        v, w = int(v), int(w)
        self.adj[v].add(w)
        self.E += 1

    def degree(self, v):
        return self.adj[v].size()

    def max_degree(self):
        max_deg = 0
        for v in range(self.V):
            max_deg = max(max_deg, self.degree(v))
        return max_deg

    def number_of_self_loops(self):
        count = 0
        for v in range(self.V):
            for w in self.adj[v]:
                if w == v:
                    count += 1
        return count

    def reverse(self):
        R = Digraph(self.V)
        v = 0
        while v < self.V:
            for w in self.adj[v]:
                R.add_edge(w, v)
            v += 1
        return R


class DirectedCycle:

    def __init__(self, G):
        self._marked = [False for _ in range(G.V)]
        self.edge_to = [False for _ in range(G.V)]
        self.on_stack = [False for _ in range(G.V)]
        self.cycle = None
        for v in range(G.V):
            if self.has_cycle():
                return
            if not self._marked[v]:
                self.dfs(G, v)

    # ADAPTADO: dfs recursivo do algs4 trocado por pilha (n ate 100.000)
    def dfs(self, G, s):
        self._marked[s] = True
        self.on_stack[s] = True
        pilha = [(s, iter(G.adj[s]))]

        while pilha:
            v, vizinhos = pilha[-1]
            w = next(vizinhos, None)

            if w is None:
                self.on_stack[v] = False
                pilha.pop()
            elif not self._marked[w]:
                self.edge_to[w] = v
                self._marked[w] = True
                self.on_stack[w] = True
                pilha.append((w, iter(G.adj[w])))
            elif self.on_stack[w]:
                cycle = []
                x = v
                while x != w:
                    cycle.append(x)
                    x = self.edge_to[x]
                cycle.append(w)
                cycle.append(v)
                self.cycle = list(reversed(cycle))
                return

    def marked(self, v):
        return self._marked[v]

    def has_cycle(self):
        return self.cycle is not None


if __name__ == '__main__':
    import sys

    dados = sys.stdin.buffer.read().split()
    n, m = int(dados[0]), int(dados[1])

    g = Digraph(n + 1)
    for i in range(m - 1, -1, -1):
        g.add_edge(dados[2 + 2 * i], dados[3 + 2 * i])

    busca = DirectedCycle(g)
    if busca.has_cycle():
        print(len(busca.cycle))
        print(" ".join(str(v) for v in busca.cycle))
    else:
        print("IMPOSSIBLE")
