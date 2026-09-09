import sys


def resolver_um_caso(n, arestas, fontes):
    adj = [[] for _ in range(n + 1)]
    for x, y in arestas:
        adj[x].append(y)

    visitado = [False] * (n + 1)

    pilha = []
    for z in fontes:
        if not visitado[z]:
            visitado[z] = True
            pilha.append(z)

    while pilha:
        atual = pilha.pop()
        for vizinho in adj[atual]:
            if not visitado[vizinho]:
                visitado[vizinho] = True
                pilha.append(vizinho)

    return sum(visitado[1:])


def main():
    dados = sys.stdin.read().split()
    ponteiro = 0

    def prox():
        nonlocal ponteiro
        valor = int(dados[ponteiro])
        ponteiro += 1
        return valor

    T = prox()
    respostas = []

    for _ in range(T):
        n = prox()
        m = prox()
        l = prox()

        arestas = [(prox(), prox()) for _ in range(m)]
        fontes = [prox() for _ in range(l)]

        total_caido = resolver_um_caso(n, arestas, fontes)
        respostas.append(str(total_caido))

    sys.stdout.write("\n".join(respostas) + "\n")


if __name__ == "__main__":
    main()
