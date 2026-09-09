"""
   Dominó 2 — medidas do grafo (Marco 2). Não é enviado ao juiz.

   Execução:  python3 medidas.py < ../dados/testes/instancia_pequena.in

   Imprime, para cada caso de teste, as medidas que validam a
   representação: graus de entrada e saída, densidade, componentes
   fracamente conexas e componentes fortemente conexas.

   Digraph vem de main.py; UF, DepthFirstOrder e KosarajuSCC são cópias
   literais de unidade-1/algs4-py/algs4/ (ver tabela no README).
"""
import sys
from collections import deque

from main import Digraph


# --- algs4/uf.py ---

class UF:

    def __init__(self, n):
        self.count = n
        self.id = list(range(n))
        self.sz = [1] * n

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def find(self, p):
        while self.id[p] != p:
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]
        return p

    def union(self, p, q):
        pId = self.find(p)
        qId = self.find(q)
        if pId == qId:
            return
        if self.sz[pId] < self.sz[qId]:
            self.id[pId] = qId
            self.sz[qId] += self.sz[pId]
        else:
            self.id[qId] = pId
            self.sz[pId] += self.sz[qId]
        self.count -= 1


# --- algs4/depth_first_order.py ---

class DepthFirstOrder:

    def __init__(self, G):
        self.marked = [False for _ in range(G.V)]
        self.pre = deque()
        self.post = deque()
        for w in range(G.V):
            if not self.marked[w]:
                self.dfs(G, w)

    def dfs(self, G, v):
        self.pre.append(v)
        self.marked[v] = True

        for w in G.adj[v]:
            if not self.marked[w]:
                self.dfs(G, w)
        self.post.append(v)

    def reverse_post(self):
        return reversed(self.post)

    def reversePost(self):
        return self.reverse_post()


# --- algs4/kosaraju_scc.py ---

class KosarajuSCC:
    def __init__(self, G):
        self.marked = [False for _ in range(G.V)]
        self.id = [0 for _ in range(G.V)]
        self.count = 0

        order = DepthFirstOrder(G.reverse())
        for v in order.reverse_post():
            if not self.marked[v]:
                self.dfs(G, v)
                self.count += 1

    def dfs(self, G, v):
        self.marked[v] = True
        self.id[v] = self.count
        for w in G.adj[v]:
            if not self.marked[w]:
                self.dfs(G, w)

    def strongly_connected(self, v, w):
        return self.id[v] == self.id[w]


# --- medidas da instância ---

if __name__ == '__main__':
    sys.setrecursionlimit(30000)

    dados = sys.stdin.read().split()
    ponteiro = 0

    def prox():
        global ponteiro
        valor = int(dados[ponteiro])
        ponteiro += 1
        return valor

    for caso in range(1, prox() + 1):
        n, m, l = prox(), prox(), prox()

        arestas = [(prox(), prox()) for _ in range(m)]

        g = Digraph(n + 1)
        grau_entrada = [0] * (n + 1)
        for x, y in reversed(arestas):
            g.add_edge(x, y)
            grau_entrada[y] += 1

        fontes = [prox() for _ in range(l)]

        uf = UF(n + 1)
        for v in range(1, n + 1):
            for w in g.adj[v]:
                uf.union(v, w)
        fracas = len({uf.find(v) for v in range(1, n + 1)})

        scc = KosarajuSCC(g)
        fortes = len({scc.id[v] for v in range(1, n + 1)})

        soma_saida = sum(g.degree(v) for v in range(1, n + 1))
        soma_entrada = sum(grau_entrada[1:])
        densidade = m / (n * (n - 1)) if n > 1 else 0.0

        print("=== Caso %d ===" % caso)
        print("n=%d m=%d l=%d" % (n, m, l))
        print("soma grau_saida=%d  soma grau_entrada=%d  m=%d"
              % (soma_saida, soma_entrada, m))
        print("densidade m/(n*(n-1))=%.6f" % densidade)
        print("fontes declaradas=%d  fontes distintas=%d" % (l, len(set(fontes))))
        print("componentes fracamente conexos=%d" % fracas)
        print("componentes fortemente conexos=%d" % fortes)
        for v in range(1, n + 1):
            print("  v=%d  d+=%d  d-=%d" % (v, g.degree(v), grau_entrada[v]))
