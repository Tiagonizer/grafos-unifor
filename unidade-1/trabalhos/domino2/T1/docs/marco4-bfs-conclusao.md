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

## 4. Escolha justificada

1. **Informação extra:** se fosse necessário saber "em que onda cada peça
   cai", só a BFS responde isso diretamente através do nível/distância.
2. **Naturalidade da implementação:** BFS com `deque`/`popleft()` é
   iterativa por construção — não existe versão recursiva natural de BFS,
   então o risco de estouro de pilha já não existe de saída.
3. **Decisão final:** com `n` até `10.000` e a possibilidade de uma cadeia
   longa (`1->2->3->...->10000`), uma DFS recursiva quebraria em Python.
   A BFS nunca teria esse risco, mesmo na forma mais direta de implementação.

Para este problema, DFS e BFS empatam em corretude e complexidade — ambas
calculam `|R(S)|` em `O(n+m)`. A escolha pela BFS se justifica pela
robustez: sua implementação iterativa natural elimina o risco de estouro de
pilha presente na DFS recursiva, no pior caso permitido pelo enunciado (`n`
até `10.000`).

## 5. Adaptação para múltiplas fontes

A BFS de livro-texto processa uma única fonte. O problema tem `l` fontes
simultâneas (todos os dominós batidos à mão caem "ao mesmo tempo"), então a
adaptação coloca todas as fontes na fila antes de iniciar o laço principal —
sem isso, tratar as fontes uma a uma criaria níveis de distância artificiais
entre elas, quando na prática todas caem na mesma "onda" inicial.

## 6. Integração

A versão final (`src/solucao.py`) já implementa exatamente essa BFS
multifonte, substituindo a DFS didática usada no Marco 3: vetor `caido`
(equivalente ao vetor de visitados), fila `deque` inicializada com todas as
`l` fontes, e contagem de `total` incrementada a cada vértice inserido na
fila. Não há mais nenhuma DFS na versão de submissão — o Marco 3 permaneceu
apenas como material didático em `docs/marco3-dfs.md`.

## 7. Testes

| instância                                              | fontes  | esperado | resultado |
|----------------------------------------------------------|---------|----------|-----------|
| sample do enunciado (`tests/sample.in`)                   | `{2}`   | 2        | OK        |
| árvore, Marco 3/4 (`tests/arvore.in`)                      | `{1}`   | 7        | OK        |
| grafo com ciclo (`tests/instancia_pequena.in`)             | `{1,6}` | 6        | OK        |
| casos de borda (`tests/casos_de_borda.in`)                 | várias  | `0,0,2,3,4` | OK    |

`bash tests/run_tests.sh` reporta `OK` nas quatro instâncias.

## 8. Complexidade

`O(n + m)` de tempo — cada vértice entra na fila no máximo uma vez, cada
aresta é examinada no máximo uma vez — e `O(n + m)` de espaço (lista de
adjacência + vetor de visitados + fila). Com `n, m <= 10.000`, é folgado
mesmo multiplicado pelo número de casos de teste `T`.

## 9. Submissão

_A preencher após submissão no juiz._

## 10. Conclusão

O problema foi modelado como grafo dirigido (queda de dominó implica queda
do próximo), representado por lista de adjacência pela esparsidade típica
das instâncias (`m` da ordem de `n`, não de `n²`). DFS e BFS resolvem o
problema de forma equivalente em corretude e complexidade — ambas calculam
`|R(S)|` em `O(n+m)` — e a BFS venceu na versão de submissão por robustez de
implementação (iterativa por construção, sem risco de estouro de pilha),
não por ser um algoritmo "melhor" em abstrato.
