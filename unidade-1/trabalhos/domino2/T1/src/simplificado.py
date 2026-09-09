"""
   Dominó 2 — versão simplificada, comentada linha a linha.

   Execução:  python3 simplificado.py < ../dados/testes/instancia_pequena.in

   NÃO é a solução enviada ao juiz (essa é src/main.py, feita só com as
   classes do algs4-py). Este arquivo existe para servir de material de
   estudo: mesmo algoritmo, mesmo resultado, mas com listas Python comuns
   no lugar de Bag/Node/Digraph/DirectedDFS, para que cada passo fique
   visível sem precisar acompanhar várias classes ao mesmo tempo.
"""
import sys


def resolver_um_caso(n, arestas, fontes):
    # 1) Lista de adjacência: adj[x] guarda todo y tal que existe aresta
    #    x -> y ("x derruba y"). n + 1 posições porque as peças são
    #    numeradas de 1 a n (o índice 0 fica sem uso).
    adj = [[] for _ in range(n + 1)]

    # 2) Preenche a lista de adjacência com as m arestas lidas.
    for x, y in arestas:
        adj[x].append(y)  # adj[x].append, não adj[x] e adj[y]: a aresta é
                           # dirigida, só x aponta para y.

    # 3) visitado[v] == True significa "a peça v já caiu". Serve para nunca
    #    contar a mesma peça duas vezes e para nunca entrar em loop
    #    infinito quando o grafo tem ciclo ou laço (x -> x).
    visitado = [False] * (n + 1)

    # 4) pilha é a estrutura da DFS: sempre processamos o último elemento
    #    inserido (pilha.pop() tira do fim). Começa com todas as fontes —
    #    é isso que torna a busca "multi-fonte": uma única pilha,
    #    compartilhada entre todos os pontos de partida.
    pilha = []
    for z in fontes:
        if not visitado[z]:       # ignora fonte repetida na lista de l
            visitado[z] = True    # marca ANTES de empilhar: evita empilhar
            pilha.append(z)       # a mesma peça duas vezes por fontes iguais

    # 5) Laço principal da DFS: enquanto houver peça na pilha para
    #    explorar, tira uma, olha todo mundo que ela derruba diretamente,
    #    e empilha quem ainda não tiver caído.
    while pilha:
        atual = pilha.pop()          # tira o topo da pilha
        for vizinho in adj[atual]:   # todo mundo que 'atual' derruba
            if not visitado[vizinho]:
                visitado[vizinho] = True   # marca no momento de empilhar
                pilha.append(vizinho)      # (não quando desempilha) — assim
                                            # uma peça nunca entra 2x na pilha

    # 6) A resposta é |R(S)|: quantas peças de 1 a n ficaram marcadas.
    return sum(visitado[1:])


def main():
    dados = sys.stdin.read().split()  # lê tudo de uma vez, separa por espaço
    ponteiro = 0                      # posição atual dentro de 'dados'

    def prox():
        # Devolve o próximo número da entrada e avança o ponteiro. Como a
        # entrada é só uma sequência de inteiros (sem estrutura de linhas
        # fixa), ler token a token é mais simples que ler linha a linha.
        nonlocal ponteiro
        valor = int(dados[ponteiro])
        ponteiro += 1
        return valor

    T = prox()               # quantidade de casos de teste
    respostas = []

    for _ in range(T):
        n = prox()
        m = prox()
        l = prox()

        arestas = [(prox(), prox()) for _ in range(m)]  # m pares (x, y)
        fontes = [prox() for _ in range(l)]              # l peças derrubadas

        total_caido = resolver_um_caso(n, arestas, fontes)
        respostas.append(str(total_caido))

    sys.stdout.write("\n".join(respostas) + "\n")


if __name__ == "__main__":
    main()
