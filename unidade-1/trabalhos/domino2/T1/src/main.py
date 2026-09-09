"""
   Dominó 2 — T1 / Unidade 1 — Resolução de Problemas com Grafos (UNIFOR)

   Execução:  python3 main.py < ../dados/testes/sample.in

   Alcançabilidade multi-fonte em um dígrafo: dadas as peças derrubadas à
   mão (conjunto S), conta quantas caem no total, |R(S)|. O(V + E).

   As classes abaixo são cópias literais do subconjunto de grafos do
   "Algorithms, 4th Edition" (Sedgewick & Wayne) disponibilizado na
   disciplina em unidade-1/algs4-py/algs4/:

       Node, LinkIterator ... utils/linklist.py
       Bag ................. bag.py
       Digraph ............. digraph.py
       DirectedDFS ......... directed_dfs.py

   Estão copiadas aqui, e não importadas, porque o juiz aceita o envio de
   um único arquivo. Nenhuma delas foi modificada.
"""

# --- algs4/utils/linklist.py ---

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


# --- algs4/bag.py ---

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


# --- algs4/digraph.py ---

class Digraph:

    def __init__(self, v=0, **kwargs):
        self.V = v
        self.E = 0
        self.adj = [Bag() for _ in range(self.V)]

        if 'file' in kwargs:
            # init a digraph by a file input
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


# --- algs4/directed_dfs.py ---

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


# --- leitura da entrada do problema ---

if __name__ == '__main__':
    import sys

    # A DFS do algs4 é recursiva e o enunciado permite n <= 10.000, ou seja,
    # uma cadeia 1->2->...->10000 chega a 10.000 chamadas aninhadas. O limite
    # padrão do CPython é 1.000; a thread abaixo roda a solução com limite e
    # pilha maiores, sem precisar alterar a classe DirectedDFS.
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

            # O algs4 numera vértices de 0 a V-1 e o enunciado numera as
            # peças de 1 a n: alocamos n + 1 e deixamos o índice 0 sem uso.
            arestas = [(prox(), prox()) for _ in range(m)]

            # Bag.add insere sempre na frente da lista ligada (Node(item,
            # first)), então iterar um Bag devolve os itens na ordem
            # INVERSA à de inserção. Para que a ordem de visita da DFS siga
            # a ordem em que as arestas foram lidas — como documentado no
            # Marco 3 —, inserimos as arestas de trás para frente: a
            # inversão da leitura mais a inversão da Bag se cancelam.
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
