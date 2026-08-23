# Marco 1 — Modelagem

## 1. Enunciado resumido

O juiz descreve um conjunto de `n` peças de dominó numeradas de `1` a `n`.
Existem `m` relações do tipo "se a peça `x` cai, ela derruba a peça `y`"
(uma por linha, sentido único de `x` para `y`). Em seguida, `l` peças são
derrubadas manualmente. Pergunta-se: quantas peças caem no total, contando
tanto as derrubadas à mão quanto as derrubadas em reação em cadeia?

A entrada contém `T` casos de teste; para cada um, imprime-se uma linha com
o total de peças caídas.

## 2. Formato de entrada e saída

```
T
n m l
x_1 y_1
...
x_m y_m
z_1
...
z_l
```
(bloco `n m l` + `m` arestas + `l` fontes, repetido `T` vezes)

Saída: `T` linhas, uma por caso, com o total de peças caídas.

## 3. Restrições

- `1 <= n, m, l <= 10.000` (por caso de teste).
- `T` não tem limite declarado no enunciado.
- O enunciado **não proíbe**:
  - laços, isto é `x == y` (uma peça "derruba a si mesma" — sem efeito
    prático, mas válido de aparecer na entrada);
  - arestas paralelas (o mesmo par `(x, y)` repetido);
  - ciclos (`x` derruba `y`, `y` derruba `x`, direta ou indiretamente);
  - fontes repetidas na lista de `l` valores;
  - `m = 0` (nenhuma relação de queda) ou `l = 0` (nenhuma peça derrubada
    à mão, resposta sempre `0`).

Como nada disso é proibido, a solução precisa ser correta mesmo nesses
casos — ver [tests/casos_de_borda.in](../tests/casos_de_borda.in).

## 4. Vértices e arestas

- **Vértices:** as `n` peças de dominó, numeradas de `1` a `n`.
- **Arestas:** um par **ordenado** `(x, y)` para cada linha `x y` da
  entrada, representando "a queda de `x` provoca a queda de `y`".

## 5. Tipo do grafo

Grafo **dirigido**, não ponderado, possivelmente cíclico, possivelmente
desconexo, admitindo laços e arestas paralelas.

A direção é essencial e não pode ser descartada: a relação "`x` derruba `y`"
é **assimétrica** — `x` derrubar `y` não implica que `y` derrube `x`. Um
grafo não dirigido (ou uma estrutura como union-find, que só enxerga
componentes conexas simétricas) fundiria `x` e `y` no mesmo grupo e
contaria `y` como caído sempre que `x` cair, mesmo quando a aresta real é
só `x -> y`. Isso dá resposta errada sempre que existe um vértice com grau
de entrada positivo e grau de saída zero (ou, de forma geral, sempre que a
aresta não é retribuída) — exatamente o caso do vértice `5` na instância de
validação abaixo.

## 6. Instância pequena de validação

```
1
7 8 2
1 2
2 3
3 1
3 4
4 4
5 4
6 7
7 6
1
6
```

`n=7, m=8, l=2`. Arestas: `1->2, 2->3, 3->1, 3->4, 4->4, 5->4, 6->7, 7->6`.
Fontes (derrubadas à mão): `1` e `6`.

Cálculo manual do conjunto alcançável `R({1,6})`:

- A partir de `1`: `1 -> 2 -> 3`; de `3` saem duas arestas, `3 -> 1` (já
  visitado, fecha o ciclo `1,2,3`) e `3 -> 4`; de `4` sai só `4 -> 4`
  (laço, não leva a lugar novo).
- A partir de `6`: `6 -> 7 -> 6` (ciclo entre os dois, nada de novo).

Conjunto alcançável: `{1, 2, 3, 4, 6, 7}`, tamanho **6**.

O vértice `5` **não cai**: ele aponta para `4` (`5 -> 4`), mas nada aponta
para `5` (grau de entrada zero) e `5` não está entre as fontes. Isso ilustra
exatamente por que a direção da aresta importa — ver seção 5.

Essa instância foi escolhida de propósito para cobrir, em um único caso:
ciclo (`1 -> 2 -> 3 -> 1`), laço (`4 -> 4`), vértice inalcançável com grau
de entrada zero (`5`) e uma componente separada do resto do grafo (`6 <-> 7`).
Arquivos correspondentes: [tests/instancia_pequena.in](../tests/instancia_pequena.in)
e [tests/instancia_pequena.out](../tests/instancia_pequena.out).

## 7. Hipótese inicial de solução

O problema equivale a uma **busca de alcançabilidade multi-fonte**: seja `S`
o conjunto de peças derrubadas à mão; a resposta é `|R(S)|`, onde `R(S)` é o
conjunto de vértices alcançáveis a partir de `S` por caminhos de comprimento
`>= 0` (as próprias fontes contam, mesmo sem nenhuma aresta de saída).

Isso é calculável com uma única busca em grafo (BFS ou DFS) iniciada
simultaneamente em todos os vértices de `S`, marcando visitados para nunca
contar a mesma peça duas vezes e nunca entrar em loop infinito diante de
ciclos ou laços. Complexidade esperada: `O(n + m)` por caso de teste, tempo
e espaço — compatível com os limites `n, m <= 10.000`.
