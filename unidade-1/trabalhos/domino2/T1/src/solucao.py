import sys
from collections import deque


def resolver():
    dados = sys.stdin.buffer.read().split()
    ponteiro = 0

    def prox():
        nonlocal ponteiro
        valor = dados[ponteiro]
        ponteiro += 1
        return int(valor)

    T = prox()
    saidas = []

    for _ in range(T):
        n = prox()
        m = prox()
        l = prox()

        adj = [[] for _ in range(n + 1)]
        for _ in range(m):
            x = prox()
            y = prox()
            adj[x].append(y)

        caido = [False] * (n + 1)
        fila = deque()
        total = 0

        for _ in range(l):
            z = prox()
            if not caido[z]:
                caido[z] = True
                total += 1
                fila.append(z)

        while fila:
            atual = fila.popleft()
            for vizinho in adj[atual]:
                if not caido[vizinho]:
                    caido[vizinho] = True
                    total += 1
                    fila.append(vizinho)

        saidas.append(str(total))

    sys.stdout.write("\n".join(saidas) + "\n")


if __name__ == "__main__":
    resolver()
