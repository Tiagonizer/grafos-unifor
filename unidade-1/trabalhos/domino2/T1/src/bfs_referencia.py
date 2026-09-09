"""
   Dominó 2 — BFS de referência (Marco 4). NÃO é a solução enviada ao juiz.

   Execução:  python3 bfs_referencia.py < ../dados/testes/arvore.in

   O Marco 4 (acompanhamento/marco-4.md) compara DFS x BFS e explica por
   que a solução final usa DFS: o que interessa ao "nosso caso" é a
   profundidade da cadeia de queda, não a distância mínima até a fonte,
   que é o que a BFS calcula. Este arquivo existe só para deixar essa
   comparação executável e apresentável — ele roda a BFS sobre a mesma
   instância de árvore usada nos Marcos 3 e 4 e imprime nível e
   predecessor de cada peça, reproduzindo as tabelas do Marco 4, §1 e §2.

   BreadthFirstPaths é cópia literal de
   unidade-1/algs4-py/algs4/breadth_first_paths.py. A classe só usa G.V e
   G.adj, então funciona sem alteração tanto em grafo dirigido (Digraph)
   quanto não dirigido (Graph) — não foi adaptada em nada.

   Só funciona com uma única fonte (BreadthFirstPaths(G, s) recebe um
   `s`), diferente da solução final que é multi-fonte; por isso só lê o
   primeiro dominó derrubado à mão de cada caso.
"""
from collections import deque

from main import Digraph


# --- algs4/breadth_first_paths.py ---

class BreadthFirstPaths:

    def __init__(self, G, s):
        self._marked = [False for _ in range(G.V)]
        self.edge_to = [0 for _ in range(G.V)]
        self.s = s
        self.bfs(G, s)

    def bfs(self, G, s):
        self._marked[s] = True
        queue = deque([s])
        while queue:
            v = queue.popleft()
            for w in G.adj[v]:
                if not self._marked[w]:
                    self.edge_to[w] = v
                    self._marked[w] = True
                    queue.append(w)

    def has_path_to(self, v):
        return self._marked[v]

    def path_to(self, v):
        if not self.has_path_to(v):
            return
        path = []
        x = v
        while x != self.s:
            path.append(x)
            x = self.edge_to[x]
        path.append(self.s)
        return reversed(path)


# --- driver: BFS sobre a instância de árvore dos Marcos 3 e 4 ---

if __name__ == '__main__':
    import sys

    dados = sys.stdin.read().split()
    ponteiro = 0

    def prox():
        global ponteiro
        valor = int(dados[ponteiro])
        ponteiro += 1
        return valor

    T = prox()
    for caso in range(1, T + 1):
        n, m, l = prox(), prox(), prox()
        arestas = [(prox(), prox()) for _ in range(m)]
        fontes = [prox() for _ in range(l)]

        # mesmo ajuste de ordem de main.py: cancela a inversão da Bag
        g = Digraph(n + 1)
        for x, y in reversed(arestas):
            g.add_edge(x, y)

        s = fontes[0]
        bfs = BreadthFirstPaths(g, s)

        print("=== Caso %d (fonte = %d) ===" % (caso, s))
        print("v | nivel | predecessor")
        for v in range(1, n + 1):
            if bfs.has_path_to(v):
                caminho = list(bfs.path_to(v))
                nivel = len(caminho) - 1
                pred = bfs.edge_to[v] if v != s else "-"
                print("%d | %d | %s" % (v, nivel, pred))
            else:
                print("%d | inalcancavel | -" % v)
