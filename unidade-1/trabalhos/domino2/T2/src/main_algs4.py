import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "..", "..", "algs4-py"))

from algs4.digraph import Digraph
from algs4.directed_cycle import DirectedCycle


class DirectedCycleIterativo(DirectedCycle):

    # ADAPTADO: dfs recursivo do algs4 trocado por pilha (n ate 100.000)
    def dfs(self, G, s):
        if self.has_cycle():
            return

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


if __name__ == '__main__':
    dados = sys.stdin.buffer.read().split()
    n, m = int(dados[0]), int(dados[1])

    g = Digraph(n + 1)
    for i in range(m - 1, -1, -1):
        g.add_edge(dados[2 + 2 * i], dados[3 + 2 * i])

    busca = DirectedCycleIterativo(g)
    if busca.has_cycle():
        print(len(busca.cycle))
        print(" ".join(str(v) for v in busca.cycle))
    else:
        print("IMPOSSIBLE")
