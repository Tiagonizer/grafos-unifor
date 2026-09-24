### Marco 2 — Componentes conexas

- **Caso particular:** grafo simples e não dirigido com 6 vértices e as arestas `{1,2},{1,3},{2,3},{2,4},{3,4},{5,6}`. Dá pra ver duas componentes só de olhar: `{1,2,3,4}` (todos ligados entre si) e `{5,6}` (isolados do resto).

  Lista de adjacência:

  | Vértice | Adjacentes |
  |---|---|
  | 1 | 2, 3 |
  | 2 | 1, 3, 4 |
  | 3 | 1, 2, 4 |
  | 4 | 2, 3 |
  | 5 | 6 |
  | 6 | 5 |

- **Excentricidade, raio, diâmetro e centro:** a excentricidade de um vértice é a maior distância dele até outro vértice da mesma componente. Na componente `{1,2,3,4}` os vértices 2 e 3 têm excentricidade 1 (mais "centrais") e 1, 4 têm excentricidade 2 — então raio = 1, diâmetro = 2 e centro = `{2,3}`. Na componente `{5,6}` os dois têm excentricidade 1, então raio = diâmetro = 1 e centro = `{5,6}`.

- **Algoritmo:** uma DFS que percorre todos os vértices de 1 a n; sempre que acha um vértice ainda não visitado, começa uma nova componente e marca (com o mesmo id) tudo que alcançar a partir dele. No exemplo, rodando a partir do vértice 1 marca `{1,2,3,4}` como componente 1, e depois, a partir do 5, marca `{5,6}` como componente 2.

  Execução manual (`visitado`, `componente_id` e `count` de componentes já fechadas):

  | Passo | Vértice visitado | visitado | componente_id | count |
  |---|---|---|---|---|
  | 0 | — | [F,F,F,F,F,F] | [0,0,0,0,0,0] | 0 |
  | 1 | 1 | [V,F,F,F,F,F] | [1,0,0,0,0,0] | 0 |
  | 2 | 2 | [V,V,F,F,F,F] | [1,1,0,0,0,0] | 0 |
  | 3 | 3 | [V,V,V,F,F,F] | [1,1,1,0,0,0] | 0 |
  | 4 | 4 | [V,V,V,V,F,F] | [1,1,1,1,0,0] | 1 |
  | 5 | 5 | [V,V,V,V,V,F] | [1,1,1,1,2,0] | 1 |
  | 6 | 6 | [V,V,V,V,V,V] | [1,1,1,1,2,2] | 2 |

  `count` sobe pra 1 quando a DFS a partir do vértice 1 termina (fechou a componente `{1,2,3,4}`) e sobe pra 2 quando termina a DFS a partir do 5 (fechou `{5,6}`).

- **Complexidade:** O(V+E), porque cada vértice é visitado uma vez e cada aresta é olhada no máximo duas vezes (uma por extremidade). Depois de rodar a DFS uma vez, responder "u e v estão na mesma componente?" fica O(1), só comparando `componente[u] == componente[v]`. Já calcular a excentricidade de todos exige uma BFS a partir de cada vértice, custando O(V·(V+E)).
