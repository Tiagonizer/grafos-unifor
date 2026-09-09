# T1 — Dominó 2

Trabalho 1 da Unidade 1 de **Resolução de Problemas com Grafos** (CCT/UNIFOR).

O problema descreve `n` peças de dominó e `m` relações do tipo "se a peça
`x` cai, ela derruba a peça `y`". Dadas `l` peças derrubadas à mão,
pergunta-se quantas caem no total. Modelado como **alcançabilidade
multi-fonte em um dígrafo**: a resposta é `|R(S)|`, o número de vértices
alcançáveis a partir do conjunto de fontes `S`, calculado por uma DFS em
`O(V + E)`.

## Estrutura

```
T1/
├── README.md
├── acompanhamento/       marcos 1 a 4 (modelagem, representação, DFS, BFS)
├── src/
│   ├── main.py             solução enviada ao juiz (DFS, só classes do algs4)
│   ├── dfs_referencia.py   DFS didática: imprime adjacência, marked e edge_to
│   └── bfs_referencia.py   BFS didática: mesmo formato do dfs_referencia.py
├── evidencias/           comprovante de "Accepted" no juiz
├── apresentacao/         slides
└── dados/
    ├── casos-de-teste.txt   casos comentados
    └── testes/              pares .in/.out + run_tests.sh
```

## Reuso do algs4

Todo o código vem do subconjunto de grafos disponibilizado pelo professor
em [`unidade-1/algs4-py`](../../../algs4-py) — recorte Python de
*Algorithms, 4th Edition* (Sedgewick & Wayne). As classes são **cópias
literais**, sem nenhuma alteração:

| classe | origem no algs4-py | papel aqui |
|---|---|---|
| `Node`, `LinkIterator` | `algs4/utils/linklist.py` | lista ligada da `Bag` |
| `Bag` | `algs4/bag.py` | lista de sucessores de um vértice |
| `Digraph` | `algs4/digraph.py` | o grafo (vetor de `Bag`) |
| `DirectedDFS` | `algs4/directed_dfs.py` | alcançabilidade multi-fonte (`main.py`) |
| `DepthFirstPaths` | `algs4/depth_first_paths.py` | DFS de fonte única (`dfs_referencia.py`) |
| `BreadthFirstPaths` | `algs4/breadth_first_paths.py` | BFS de fonte única (`bfs_referencia.py`) |

As classes usadas pela solução estão copiadas dentro de `src/main.py`, e
não importadas, porque o juiz aceita o envio de um único arquivo.
`src/dfs_referencia.py` e `src/bfs_referencia.py` importam `Digraph` de
`main.py` e só acrescentam a classe de busca correspondente.

O único código escrito por nós é a leitura da entrada e a impressão do
resultado, no bloco `if __name__ == '__main__'` de cada arquivo. Dois
pontos desse bloco merecem nota:

- O `algs4` numera vértices de `0` a `V-1` e o enunciado numera as peças de
  `1` a `n`; construímos `Digraph(n + 1)` e deixamos o índice `0` sem uso,
  mantendo a classe intacta.
- A `DirectedDFS` do algs4 é recursiva e `n` pode chegar a `10.000`. Em vez
  de reescrevê-la, o programa eleva `sys.setrecursionlimit` e roda a
  solução numa thread com pilha maior. Ver
  [acompanhamento/marco-3.md](acompanhamento/marco-3.md), §8.
- `Bag.add` insere na frente da lista ligada, então iterar `adj[v]` devolve
  as arestas na ordem inversa à de leitura. As arestas são inseridas de
  trás para frente (`reversed(arestas)`) para cancelar essa inversão e
  manter a ordem de visita descrita no Marco 3.

## Como executar

```sh
cd src

# resolve uma entrada (saída = um número por caso, formato do juiz)
python3 main.py < ../dados/testes/sample.in

# DFS didática: lista de adjacência, marked e edge_to
python3 dfs_referencia.py < ../dados/testes/arvore.in

# BFS didática: mesmo formato, para comparar com a DFS
python3 bfs_referencia.py < ../dados/testes/arvore.in

# suíte de testes
bash ../dados/testes/run_tests.sh
```

Saída esperada da suíte:

```
OK   arvore
OK   casos_de_borda
OK   instancia_pequena
OK   sample
```

## Desempenho

Pior caso sintético — 50 casos de teste, cada um com `n = m = 10.000` em
uma única cadeia `1->2->...->10000`, que é a maior profundidade de recursão
possível: **0,82 s** e sem estouro de pilha. A `Bag` (lista ligada) é mais
pesada que uma lista Python nativa, mas com os limites do enunciado a folga
é grande.

## Acompanhamento

| marco | conteúdo |
|---|---|
| [Marco 1](acompanhamento/marco-1.md) | modelagem: vértices, arestas, tipo do grafo, instância de validação |
| [Marco 2](acompanhamento/marco-2.md) | representação: lista de adjacência vs. matriz, densidade, medidas |
| [Marco 3](acompanhamento/marco-3.md) | DFS: execução manual, estados branco/cinza/preto, tempos, alcançabilidade |
| [Marco 4](acompanhamento/marco-4.md) | BFS, comparação DFS × BFS e conclusão |
