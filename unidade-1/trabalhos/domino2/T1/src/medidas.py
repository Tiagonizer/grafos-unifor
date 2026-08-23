"""
Script de apoio (Marco 2): calcula graus, densidade e componentes
para validar a representacao escolhida. Nao e enviado ao juiz -
uso: python3 medidas.py < entrada.in
"""
import sys
from collections import deque


def ler_casos():
    dados = sys.stdin.buffer.read().split()
    ponteiro = 0

    def prox():
        nonlocal ponteiro
        valor = dados[ponteiro]
        ponteiro += 1
        return int(valor)

    T = prox()
    casos = []
    for _ in range(T):
        n = prox()
        m = prox()
        l = prox()
        arestas = [(prox(), prox()) for _ in range(m)]
        fontes = [prox() for _ in range(l)]
        casos.append((n, m, l, arestas, fontes))
    return casos


def componentes_fracas(n, arestas):
    pai = list(range(n + 1))

    def find(a):
        while pai[a] != a:
            pai[a] = pai[pai[a]]
            a = pai[a]
        return a

    def uniao(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            pai[ra] = rb

    for x, y in arestas:
        if x != y:
            uniao(x, y)

    return len({find(v) for v in range(1, n + 1)})


def componentes_fortes(n, adj):
    """Kosaraju: duas passagens de DFS iterativa."""
    visitado = [False] * (n + 1)
    ordem = []

    for inicio in range(1, n + 1):
        if visitado[inicio]:
            continue
        pilha = [(inicio, iter(adj[inicio]))]
        visitado[inicio] = True
        while pilha:
            v, it = pilha[-1]
            avancou = False
            for w in it:
                if not visitado[w]:
                    visitado[w] = True
                    pilha.append((w, iter(adj[w])))
                    avancou = True
                    break
            if not avancou:
                ordem.append(v)
                pilha.pop()

    adj_t = [[] for _ in range(n + 1)]
    for v in range(1, n + 1):
        for w in adj[v]:
            adj_t[w].append(v)

    visitado = [False] * (n + 1)
    num_sccs = 0
    for v in reversed(ordem):
        if visitado[v]:
            continue
        num_sccs += 1
        pilha = [v]
        visitado[v] = True
        while pilha:
            atual = pilha.pop()
            for w in adj_t[atual]:
                if not visitado[w]:
                    visitado[w] = True
                    pilha.append(w)

    return num_sccs


def analisar(n, m, l, arestas, fontes):
    adj = [[] for _ in range(n + 1)]
    grau_saida = [0] * (n + 1)
    grau_entrada = [0] * (n + 1)

    for x, y in arestas:
        adj[x].append(y)
        grau_saida[x] += 1
        grau_entrada[y] += 1

    soma_saida = sum(grau_saida)
    soma_entrada = sum(grau_entrada)
    densidade = m / (n * (n - 1)) if n > 1 else 0.0

    print(f"n={n} m={m} l={l}")
    print(f"soma grau_saida={soma_saida}  soma grau_entrada={soma_entrada}  m={m}")
    print(f"densidade m/(n*(n-1))={densidade:.6f}")
    print(f"fontes declaradas={l}  fontes distintas={len(set(fontes))}")
    print(f"componentes fracamente conexos={componentes_fracas(n, arestas)}")
    print(f"componentes fortemente conexos={componentes_fortes(n, adj)}")
    for v in range(1, n + 1):
        print(f"  v={v}  d+={grau_saida[v]}  d-={grau_entrada[v]}")


def main():
    for i, caso in enumerate(ler_casos(), start=1):
        print(f"=== Caso {i} ===")
        analisar(*caso)


if __name__ == "__main__":
    main()
