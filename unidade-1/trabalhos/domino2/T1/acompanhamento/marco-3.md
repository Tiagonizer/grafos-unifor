# Marco 3 — Aplicação básica de DFS

Instância de exemplo (árvore, sem ciclos): `n=7, m=6, l=1`. Arestas
`1->2, 1->3, 3->4, 4->5, 4->6, 4->7`. Fonte: `{1}`.

## 1. Execução manual da DFS

Ordem de visita (percorrendo `adj[v]` em ordem crescente):

> **Nota de implementação.** `Bag` (`algs4/bag.py`) insere cada aresta na
> *frente* de uma lista ligada, então iterar `adj[v]` devolve as arestas na
> ordem **inversa** à de inserção. Em [src/main.py](../src/main.py), as
> arestas de cada caso são inseridas de trás para frente (`for x, y in
> reversed(arestas)`) justamente para cancelar essa inversão — o resultado
> é que `adj[v]` acaba na mesma ordem em que as arestas foram lidas da
> entrada, que nesta instância já é a ordem crescente usada abaixo.

| ordem | vértice visitado |
|-------|-------------------|
| 1     | 1                 |
| 2     | 2                 |
| 3     | 3                 |
| 4     | 4                 |
| 5     | 5                 |
| 6     | 6                 |
| 7     | 7                 |

Caminho: `1 -> 2` (volta, sem sucessores), `1 -> 3 -> 4 -> 5` (volta),
`4 -> 6` (volta), `4 -> 7` (volta), fim.

## 2. Estados de visita

- **Branco:** vértice ainda não descoberto pela busca.
- **Cinza:** vértice descoberto, mas com a busca ainda "dentro" dele (está
  na pilha de recursão/pilha explícita, ainda tem sucessores por explorar).
- **Preto:** vértice e todos os seus descendentes já foram totalmente
  explorados.

O cinza importa para detectar ciclo: se, ao explorar `v`, encontramos uma
aresta `v -> u` onde `u` já está **cinza**, isso significa que `u` é
ancestral de `v` na busca atual — logo existe um caminho `u -> ... -> v -> u`,
um ciclo. Aresta para vértice **preto** não indica ciclo (é um cruzamento
para uma subárvore já concluída); nesta instância não há nenhuma, pois é uma
árvore.

## 3. Árvore de busca resultante

```
1
├── 2
└── 3
    └── 4
        ├── 5
        ├── 6
        └── 7
```

## 4. Tempos de descoberta e término

| v | descoberta | término |
|---|------------|---------|
| 1 | 1          | 14      |
| 2 | 2          | 3       |
| 3 | 4          | 13      |
| 4 | 5          | 12      |
| 5 | 6          | 7       |
| 6 | 8          | 9       |
| 7 | 10         | 11      |

## 5. Alcançabilidade

`R({1}) = {1, 2, 3, 4, 5, 6, 7}`, `|R(S)| = 7`.

Como o grafo é uma árvore enraizada em `1`, toda peça é descendente de `1`
por exatamente um caminho, e a DFS a partir de `1` visita todo vértice
alcançável exatamente uma vez. Isso bate com a resposta esperada do
problema: **7** peças caem.

## 6. Predecessores

| v | predecessor (pai na DFS) |
|---|----------------------------|
| 1 | — (raiz)                  |
| 2 | 1                          |
| 3 | 1                          |
| 4 | 3                          |
| 5 | 4                          |
| 6 | 4                          |
| 7 | 4                          |

## 7. Aplicabilidade ao problema

O problema só pergunta "quantas peças caem", ou seja, a resposta é
`|R(S)|` — o tamanho do conjunto de vértices visitados pela DFS a partir das
fontes `S`. Tempos de descoberta/término, árvore de busca e predecessores
(seções 3, 4 e 6) são informação extra que a DFS produz como subproduto do
algoritmo clássico, mas o problema não usa nada disso: basta contar quantos
vértices deixaram de ser brancos.

## 8. Adaptação parcial

A solução final não reimplementa a DFS: usa a classe `DirectedDFS` de
`algs4/directed_dfs.py`, que já resolve exatamente "alcançabilidade a
partir de um conjunto de fontes" em um dígrafo. A classe é copiada sem
nenhuma alteração — inclusive a DFS **recursiva** do original.

O que a solução adapta é só o entorno:

- Os tempos de descoberta e término (seção 4) não são calculados. O
  problema pede apenas `|R(S)|`, e `DirectedDFS` guarda somente o vetor de
  visitados; o total sai de uma varredura de `marked(v)` no fim.
- Como `n` pode chegar a `10.000`, uma cadeia `1 -> 2 -> ... -> 10000`
  daria `10.000` chamadas aninhadas, acima do limite padrão de recursão do
  CPython (`1.000`). Em vez de reescrever a DFS, o programa principal eleva
  `sys.setrecursionlimit` e roda a solução numa thread com pilha maior
  (`threading.stack_size`) — assim a classe do algs4 continua intacta.

Código em [src/main.py](../src/main.py).
