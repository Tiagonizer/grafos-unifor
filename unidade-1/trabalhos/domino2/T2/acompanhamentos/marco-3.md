### Marco 3 — Estratégia algorítmica

- **Propriedade estrutural:** o problema pede pra achar um ciclo num grafo direcionado. O critério pra reconhecer o ciclo durante a DFS é: ao visitar os adjacentes de um vértice `v`, se um deles (`w`) já foi visitado **e ainda está na pilha da recursão atual** (`on_stack[w] = true`), então existe um ciclo passando por `w` e `v`. Se o adjacente já foi visitado mas não está mais na pilha, não é ciclo, só um caminho que já terminou.

- **Implementações de referência (`algs4`):**
  - `Digraph` — constrói o grafo dirigido a partir da entrada.
  - `Bag` — estrutura usada internamente pelo `Digraph` para guardar a lista de adjacência de cada vértice.
  - `DirectedCycle` — roda a DFS e identifica o ciclo, populando as estruturas auxiliares `marked`, `on_stack` e `edge_to`; quando acha um `on_stack[w] = true`, reconstrói o ciclo andando por `edge_to` de volta até `w`.

- **Instância pequena:**

  ```
  INPUT          OUTPUT
  4 5            4
  1 3            2 1 3 2
  2 1
  2 4
  3 2
  3 4
  ```

  Lista de adjacência: `1 → [3]`, `2 → [1, 4]`, `3 → [2, 4]`, `4 → []`.

  Rastreamento da DFS (iniciando em 1):

  | Passo | Ação | marked | on_stack | edge_to |
  |---|---|---|---|---|
  | 0 | estado inicial | [F,F,F,F] | [F,F,F,F] | [-,-,-,-] |
  | 1 | DFS(1) | [V,F,F,F] | [V,F,F,F] | [-,-,-,-] |
  | 2 | visita 3 (não marcado) → DFS(3) | [V,F,V,F] | [V,F,V,F] | [-,-,1,-] |
  | 3 | visita 2 (não marcado) → DFS(2) | [V,V,V,F] | [V,V,V,F] | [-,3,1,-] |
  | 4 | visita 1: marcado e on_stack → **ciclo!** | [V,V,V,F] | [V,V,V,F] | [-,3,1,-] |

  No passo 4 o ciclo é reconstruído andando de `v=2` por `edge_to` até chegar em `w=1`: empilha `2`, depois `3`, depois `1` (fecha o laço), e por fim `2` de novo — dando a saída `2 1 3 2`.

- **Complexidade:** tempo O(V+E), porque a DFS visita cada vértice e cada aresta uma única vez. Memória O(V) de estruturas auxiliares (`marked`, `on_stack`, `edge_to` e a pilha de recursão), fora da representação do próprio grafo que já custa O(V+E) na lista de adjacência.
