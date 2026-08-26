# Marco 3 — Aplicação básica de DFS

Instância de exemplo (árvore, sem ciclos): `n=7, m=6, l=1`. Arestas
`1->2, 1->3, 3->4, 4->5, 4->6, 4->7`. Fonte: `{1}`.

## 1. Execução manual da DFS

Ordem de visita (percorrendo `adj[v]` em ordem crescente):

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

A versão final da solução usa DFS **iterativa com pilha explícita** em vez
de recursiva, porque `n` pode chegar a `10.000` e uma DFS recursiva em
Python arrisca estourar a pilha de chamadas em grafos com caminhos longos
(o limite padrão de recursão do interpretador é bem menor que `10.000`).
Os tempos de descoberta/término (seção 4) são removidos da versão de
submissão, pois não são necessários para calcular `|R(S)|` — a versão final
guarda apenas o vetor de visitados, reduzindo memória e trabalho por
vértice.
