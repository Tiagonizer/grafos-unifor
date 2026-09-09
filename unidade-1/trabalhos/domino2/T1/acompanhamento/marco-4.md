# Marco 4 — BFS e conclusão

Mesma instância do Marco 3 (árvore, sem ciclos): `n=7, m=6, l=1`. Arestas
`1->2, 1->3, 3->4, 4->5, 4->6, 4->7`. Fonte: `{1}`.

## 1. Execução manual da BFS

Fila (FIFO): a fonte entra primeiro; a cada passo retira-se o vértice da
frente e inserem-se no fim todos os vizinhos ainda não visitados.

| passo | fila antes  | retira | insere      |
|-------|-------------|--------|-------------|
| 1     | `[1]`       | 1      | 2, 3        |
| 2     | `[2, 3]`    | 2      | —           |
| 3     | `[3]`       | 3      | 4           |
| 4     | `[4]`       | 4      | 5, 6, 7     |
| 5     | `[5, 6, 7]` | 5      | —           |
| 6     | `[6, 7]`    | 6      | —           |
| 7     | `[7]`       | 7      | —           |

Ordem de visita: `1, 2, 3, 4, 5, 6, 7` — coincide com a ordem da DFS nesta
instância específica, por ser uma árvore rasa; não é uma propriedade geral.

## 2. Níveis, distâncias e predecessores

| v | nível (distância da fonte) | predecessor |
|---|-----------------------------|-------------|
| 1 | 0                           | —           |
| 2 | 1                           | 1           |
| 3 | 1                           | 1           |
| 4 | 2                           | 3           |
| 5 | 3                           | 4           |
| 6 | 3                           | 4           |
| 7 | 3                           | 4           |

Diferente da DFS, o nível em que a BFS descobre um vértice é garantidamente
a menor distância possível até ele a partir da fonte. Nesta instância a
garantia não chega a ser "testada", pois o grafo é uma árvore: só existe um
caminho de `1` até qualquer outro vértice, então não há caminho alternativo
mais curto para comparar. A diferença só ficaria visível num grafo com
múltiplos caminhos até o mesmo vértice.

## 3. Comparação DFS × BFS

| critério                    | DFS                                 | BFS                              |
|------------------------------|--------------------------------------|-----------------------------------|
| estrutura de dados           | pilha (ou recursão)                  | fila                              |
| ordem de visita (esta instância) | 1,2,3,4,5,6,7                    | 1,2,3,4,5,6,7 (coincidem aqui)    |
| `R(S)` calculado             | `{1..7}`                             | `{1..7}` — idêntico                |
| complexidade                 | `O(n+m)`                              | `O(n+m)` — idêntica                |
| informação extra             | tempos de descoberta/término, detecta ciclo | distância mínima até a fonte |
| garante caminho mais curto   | não                                    | sim                                |
| risco de estouro de pilha    | sim, se recursiva                     | não, fila nunca recursiona         |

Para a pergunta do problema ("quantos dominós caem"), DFS e BFS sempre dão a
mesma resposta, pois ambas calculam `|R(S)|`. A escolha entre elas não é
questão de corretude nem de complexidade, e sim de robustez de implementação
e do que sobra de informação extra.


## 4. Complexidade

`O(n + m)` de tempo — cada vértice entra na fila no máximo uma vez, cada
aresta é examinada no máximo uma vez — e `O(n + m)` de espaço (lista de
adjacência + vetor de visitados + fila). Com `n, m <= 10.000`, é folgado
mesmo multiplicado pelo número de casos de teste `T`.


## 5. Conclusão

O problema foi modelado como grafo dirigido (queda de dominó implica queda
do próximo), representado por lista de adjacência pela esparsidade típica
das instâncias (`m` da ordem de `n`, não de `n²`). DFS e BFS resolvem o
problema de forma equivalente em corretude e complexidade — ambas calculam
`|R(S)|` em `O(n+m)`.

Para o **nosso caso**, a escolha recai sobre a **DFS**: além de contar
`|R(S)|`, o que nos interessa é a *profundidade* da propagação — quão longe,
em número de dominós encadeados, uma batida inicial consegue chegar. A DFS
explora cada ramo até o fim antes de retroceder, então o nível da pilha (ou
da recursão) no momento em que um vértice é descoberto corresponde ao
comprimento do caminho percorrido desde a fonte, e o maior valor atingido é
a profundidade máxima da cadeia. A BFS, por avançar em ondas, entrega a
distância mínima até a fonte, não o encadeamento mais profundo que estamos
querendo medir.

Na prática a DFS é implementada de forma **iterativa com pilha explícita**
(não recursiva), pois `n` pode chegar a `10.000` e uma cadeia longa
(`1->2->...->10000`) estouraria a pilha de chamadas do Python. Assim
mantém-se a robustez de uma implementação iterativa sem abrir mão da
informação de profundidade que motivou a escolha.
