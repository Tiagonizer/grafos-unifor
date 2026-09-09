class Node:

    def __init__(self, item, next_node):
        self.item = item
        self.next = next_node


class LinkIterator:

    def __init__(self, current):
        self.current = current

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


class DirectedDFS:

    def __init__(self, G, sources):
        self._marked = [False for _ in range(G.V)]
        for s in sources:
            s = int(s)
            if not self._marked[s]:
                self.dfs(G, s)

    def dfs(self, G, v):
        self._marked[v] = True
        for w in G.adj[v]:
            if not self._marked[w]:
                self.dfs(G, w)

    def marked(self, v):
        return self._marked[v]


if __name__ == '__main__':
    import sys
    import threading

    def resolver():
        dados = sys.stdin.read().split()
        ponteiro = 0

        def prox():
            nonlocal ponteiro
            valor = int(dados[ponteiro])
            ponteiro += 1
            return valor

        respostas = []
        for _ in range(prox()):
            n, m, l = prox(), prox(), prox()
            arestas = [(prox(), prox()) for _ in range(m)]

            g = Digraph(n + 1)
            for x, y in reversed(arestas):
                g.add_edge(x, y)

            fontes = [prox() for _ in range(l)]

            busca = DirectedDFS(g, fontes)
            respostas.append(str(sum(1 for v in range(1, n + 1)
                                     if busca.marked(v))))

        sys.stdout.write("\n".join(respostas) + "\n")

    sys.setrecursionlimit(30000)
    threading.stack_size(64 * 1024 * 1024)
    t = threading.Thread(target=resolver)
    t.start()
    t.join()
