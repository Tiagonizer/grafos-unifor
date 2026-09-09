# Dominó 2

Atividade prática da Unidade 1 — **Resolução de Problemas com Grafos**
(CCT/UNIFOR).

O trabalho completo, com código, acompanhamento por marcos, casos de teste
e evidências, está em **[T1/](T1/)**.

## O problema em uma linha

`n` peças de dominó, `m` relações dirigidas "`x` cai ⇒ `y` cai", `l` peças
derrubadas à mão: quantas caem no total?

## A solução em uma linha

Alcançabilidade multi-fonte em um dígrafo — a resposta é `|R(S)|`, obtida
por uma DFS iterativa em `O(V + E)`, reaproveitando a classe `DirectedDFS`
do [algs4-py](../../algs4-py) disponibilizado na disciplina.

| | |
|---|---|
| Modelagem e justificativas | [T1/acompanhamento/](T1/acompanhamento/) |
| Código enviado ao juiz | [T1/src/main.py](T1/src/main.py) |
| Casos de teste | [T1/dados/](T1/dados/) |
| Como rodar | [T1/README.md](T1/README.md) |
