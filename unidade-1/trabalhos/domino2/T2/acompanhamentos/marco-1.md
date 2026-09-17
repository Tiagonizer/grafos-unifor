### Marco 1 — Problema e conhecimento prévio

Grupo B - Problema E - Round Trip II

O problema pede pra achar um ciclo em um grafo direcionado: uma volta que sai de uma cidade, passa por outras (todas diferentes) e volta pra cidade inicial. Se não existir nenhum ciclo, a resposta é "IMPOSSIBLE".

- **Entrada:** `n` cidades e `m` voos (arestas), seguidos de `m` pares `a b` indicando um voo de `a` para `b`.
- **Saída:** a quantidade de cidades na rota e a sequência de cidades do ciclo encontrado.

- **Modelagem:** cada cidade é um vértice e cada voo é uma aresta direcionada de `a` para `b`.

- **Classificação do grafo:** direcionado, não ponderado, simples, pode ou não ser conexo e pode ou não ter ciclo (é justamente isso que precisamos descobrir).

- **Ideia de solução:** dá pra usar DFS marcando os vértices em três estados (não visitado, na pilha atual, já finalizado). Se durante a DFS encontrarmos um vizinho que está na pilha atual, achamos um ciclo — daí é só reconstruir o caminho. Complexidade O(V+E).
