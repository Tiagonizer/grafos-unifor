# Unidade 1 - Atividade Prática: Dominó 2

Documentação da representação e modelagem computacional para o problema **Dominó 2**.

---

### 1. Grafo Construído
* **Tipo de Grafo:** Grafo Direcionado (Dígrafo).
* **Vértices ($V$):** $n$ peças de dominó, numeradas de $1$ a $n$.
* **Arestas ($E$):** Pares ordenados $(x, y)$, onde a queda da peça $x$ provoca a queda da peça $y$ (sentido único $x \to y$).

---

### 2. Representação Computacional e Justificativa de Custo
* **Estrutura Escolhida:** Lista de Adjacência.
* **Justificativa de Espaço:** $O(V + E)$. Como $n, m \le 10.000$, a lista gasta memória proporcional apenas às conexões existentes. Uma Matriz de Adjacência alocaria $O(V^2) = 10^8$ posições sem necessidade.
* **Complexidade de Tempo (Busca DFS):** $O(V + E)$, garantindo tempo de execução linear e instantâneo no envio.

---

### 3. Entrada Processada e Algoritmo
1. Leitura dos inteiros $n, m, l$.
2. Montagem do vetor de listas de adjacência `adj` de tamanho $n + 1$.
3. Leitura dos $l$ dominós derrubados manualmente.
4. Aplicação de uma Busca em Profundidade (DFS Iterativo) a partir dos nós iniciais para marcar o array de visitados e contabilizar os dominós caídos sem duplicações.

---

### 4. Medidas Pertinentes do Grafo
* **Ordem ($|V|$):** Número total de dominós ($n$).
* **Tamanho ($|E|$):** Número total de reações em cadeia ($m$).
* **Grau de Saída ($d^+_v$):** Quantidade de dominós que a peça $v$ derruba diretamente.
* **Grau de Entrada ($d^-_v$):** Quantidade de dominós capazes de derrubar a peça $v$ diretamente.

---

### 5. Validação da Instância Pequena (Exemplo 1)
* **Entrada:** $n = 3, m = 2, l = 1$ | Arestas: $(1 \to 2), (2 \to 3)$ | Manual: $2$
* **Execução:**
  1. Início pelo nó manual $2 \rightarrow$ `caido[2] = True` (Contador = 1).
  2. Aresta $2 \to 3 \rightarrow$ marca `caido[3] = True` (Contador = 2).
  3. Nó $3$ possui grau de saída zero $\rightarrow$ finaliza.
* **Resultado Obtido:** `2` (Validado com a saída esperada).