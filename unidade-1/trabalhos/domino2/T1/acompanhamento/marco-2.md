# Marco 2 — Representação

## 1. Alternativas de representação

| Estrutura            | Memória          | Consulta "quem `x` derruba?" | Consulta "existe aresta `x->y`?" |
|-----------------------|------------------|-------------------------------|-----------------------------------|
| Lista de arestas       | `O(m)`           | `O(m)` (varrer tudo)           | `O(m)`                             |
| Matriz de adjacência   | `O(n^2)`         | `O(n)` (varrer a linha)        | `O(1)`                             |
| Lista de adjacência    | `O(n + m)`       | `O(d^+(x))` (grau de saída)    | `O(d^+(x))`                        |

A lista de arestas é descartada porque a simulação da queda precisa,
repetidamente, da pergunta "quem `x` derruba diretamente?" — com lista de
arestas isso custa `O(m)` por consulta, tornando a busca `O(n*m)` no pior
caso.

A matriz de adjacência custaria `O(n^2)` de memória: com `n <= 10.000`,
isso são até `10^8` células, o que já é pesado em memória e tempo de
alocação/leitura, para um grafo onde a maior parte das células seria zero
(ver densidade abaixo).

## 2. Escolha: lista de adjacência

**Estrutura escolhida:** lista de adjacência de sucessores, um vetor de `n+1`
listas (índice `0` não usado), onde `adj[x]` contém todo `y` tal que existe
aresta `x -> y`.

**Justificativa por densidade.** O número máximo de arestas dirigidas
simples entre `n` vértices distintos é `n*(n-1)`. No pior caso do problema
(`n = m = 10.000`), a densidade é:

```
m / (n*(n-1)) = 10.000 / (10.000 * 9.999) ≈ 10^-4
```

ou seja, o grafo é extremamente esparso — cada vértice derruba, em média,
no máximo uma outra peça (`m/n <= 1`). Uma matriz alocaria `10^8` células
para guardar, no pior caso, `10^4` arestas reais: `99,99%` de desperdício.
A lista de adjacência gasta memória proporcional só ao que existe:
`O(n + m)`.

**Grau médio de saída.** Como `m <= n` não é garantido pelo enunciado (na
verdade `m` pode ir até `10.000` independente de `n`), o que importa é a
razão `m/n`; no pior caso declarado (`n = m = 10.000`) o grau médio de saída
é `1`, reforçando que o grafo é esparso e a lista de adjacência é a
estrutura correta.

## 3. Leitura da entrada e construção

```python
n = prox(); m = prox(); l = prox()

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    x = prox(); y = prox()
    adj[x].append(y)   # aresta dirigida x -> y
```

Código completo em [src/solucao.py](../src/solucao.py); leitura auxiliar de
medidas estruturais em [src/medidas.py](../src/medidas.py).

## 4. Medidas estruturais da instância pequena

Grafo: `n=7, m=8`, arestas `1->2, 2->3, 3->1, 3->4, 4->4, 5->4, 6->7, 7->6`,
fontes `{1, 6}` (ver [Marco 1](marco1-modelagem.md), seção 6).

| v | d+(v) | d-(v) |
|---|-------|-------|
| 1 | 1     | 1     |
| 2 | 1     | 1     |
| 3 | 2     | 1     |
| 4 | 1     | 3     |
| 5 | 1     | 0     |
| 6 | 1     | 1     |
| 7 | 1     | 1     |

- **Densidade:** `m/(n*(n-1)) = 8/42 ≈ 0,190476`.
- **Fontes:** `2` declaradas, `2` distintas (sem repetição neste caso; ver
  caso de borda `D` em [tests/casos_de_borda.in](../tests/casos_de_borda.in)
  para fonte repetida).
- **Componentes fracamente conexas:** `2` — `{1,2,3,4,5}` e `{6,7}` (ligação
  por `3->4` e `5->4`; o laço `4->4` não afeta a contagem).
- **Componentes fortemente conexas:** `4` — `{1,2,3}` (ciclo), `{4}` (laço,
  trivialmente forte), `{5}` (isolado), `{6,7}` (ciclo mútuo).

Saída real de [src/medidas.py](../src/medidas.py) sobre
[tests/instancia_pequena.in](../tests/instancia_pequena.in):

```
n=7 m=8 l=2
soma grau_saida=8  soma grau_entrada=8  m=8
densidade m/(n*(n-1))=0.190476
fontes declaradas=2  fontes distintas=2
componentes fracamente conexos=2
componentes fortemente conexos=4
```

## 5. Validação da representação

Identidade que toda lista de adjacência deve satisfazer:

```
soma dos graus de saída = soma dos graus de entrada = m
```

Para a instância pequena: `soma(d+) = 1+1+2+1+1+1+1 = 8`, `soma(d-) =
1+1+1+3+0+1+1 = 8`, e `m = 8`. As três batem, confirmando que cada uma das
`8` arestas lidas foi contabilizada exatamente uma vez como saída (na
origem) e uma vez como entrada (no destino) — nenhuma aresta foi perdida ou
duplicada na construção de `adj`.
