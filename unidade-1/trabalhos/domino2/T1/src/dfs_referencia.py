import sys
import threading

from main import Digraph


class DepthFirstPaths:

    def __init__(self, G, s):
        self.marked = [False for _ in range(G.V)]
        self.edge_to = [0 for _ in range(G.V)]
        self.s = s
        self.dfs(G, s)

    def dfs(self, G, v):
        self.marked[v] = True
        for w in G.adj[v]:
            if not self.marked[w]:
                self.edge_to[w] = v
                self.dfs(G, w)

    def has_path_to(self, v):
        return self.marked[v]

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


def main():
    numeros = iter(map(int, sys.stdin.read().split()))
    next(numeros)
    n, m, l = next(numeros), next(numeros), next(numeros)
    arestas = [(next(numeros), next(numeros)) for _ in range(m)]
    fontes = [next(numeros) for _ in range(l)]

    g = Digraph(n + 1)
    for x, y in arestas:
        g.add_edge(x, y)

    s = fontes[0]
    busca = DepthFirstPaths(g, s)

    vertices = range(1, n + 1)
    marked = ["T" if busca.has_path_to(v) else "F" for v in vertices]
    edge_to = [str(busca.edge_to[v]) if v != s and busca.has_path_to(v) else "-"
               for v in vertices]

    print("algoritmo = DFS")
    print("fonte = %d" % s)
    print()
    print("lista de adjacencia:")
    for v in vertices:
        print("  %d -> %s" % (v, ", ".join(str(w) for w in g.adj[v])))
    print()
    print("v       : " + " ".join(str(v) for v in vertices))
    print("marked  : " + " ".join(marked))
    print("edge_to : " + " ".join(edge_to))
    print()
    print("total de pecas que caem = %d" % sum(1 for v in vertices if busca.has_path_to(v)))


sys.setrecursionlimit(30000)
threading.stack_size(64 * 1024 * 1024)
t = threading.Thread(target=main)
t.start()
t.join()
