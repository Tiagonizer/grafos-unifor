### Marco 4 — Implementação final e conclusão

- **Solução final:** feita em Python, em [src/main.py](../src/main.py). O programa lê `n` e `m`, monta um `Digraph` com `n + 1` vértices (as cidades vão de 1 a `n`, então o vértice 0 fica sem uso), adiciona uma aresta para cada voo e roda o `DirectedCycle`. Se achar ciclo, imprime o tamanho e as cidades; senão imprime `IMPOSSIBLE`. Na instância do Marco 3 a saída é `4` e `2 1 3 2`, igual ao rastreamento feito à mão.

- **Classes reutilizadas (sem alteração):**
  - `Digraph` — o grafo dirigido.
  - `Bag` — a lista de adjacência de cada vértice.
  - `Node` e `LinkIterator` — a lista encadeada usada pelo `Bag`.

  Foram copiadas do `algs4` para dentro do `main.py` só porque o CSES aceita o envio de um único arquivo. A versão [src/main_algs4.py](../src/main_algs4.py) faz a mesma coisa importando direto do `algs4`.

- **Classe modificada:** `DirectedCycle`.
  - O método `dfs` era recursivo e passou a usar uma pilha (lista do Python). **Motivo:** `n` chega a 100.000, e num grafo em "fila" (1→2→3→...→n) a recursão teria 100.000 chamadas, o que estoura o limite do Python.
  - O construtor agora para de buscar assim que acha o primeiro ciclo. **Motivo:** o problema só pede um ciclo.

- **Como ficou a adaptação:** cada item da pilha guarda o vértice e em qual vizinho dele a busca parou. Empilhar um vértice equivale a chamar `dfs(w)`, e desempilhar equivale ao fim da chamada (é quando `on_stack[v]` volta a ser falso). O critério não mudou: se o vizinho `w` já está marcado e `on_stack[w]` é verdadeiro, achamos o ciclo, e ele é reconstruído pelo `edge_to` como no original. As estruturas `marked`, `on_stack` e `edge_to` são as mesmas do Marco 3.
