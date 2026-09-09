# Resolução de Problemas com Grafos — UNIFOR

Repositório dos trabalhos, algoritmos e atividades práticas da disciplina
de **Resolução de Problemas com Grafos** do CCT/UNIFOR.

* **Professor:** Prof. Me. Ricardo Carubbi
* **Linguagem:** Python 3

---

## Estrutura

```
unidade-1/
├── algs4-py/                    subconjunto de grafos do "Algorithms, 4th Ed."
│                                (Sedgewick & Wayne) usado como referência
└── trabalhos/
    └── domino2/
        └── T1/                  Trabalho 1 — Dominó 2
            ├── acompanhamento/  marcos 1 a 4
            ├── src/             main.py (juiz) e medidas.py (apoio)
            ├── dados/           casos de teste
            ├── evidencias/      comprovante de Accepted
            └── apresentacao/    slides
```

## Referência de implementação

[`unidade-1/algs4-py`](unidade-1/algs4-py) é o recorte de grafos do
`algs4` disponibilizado pelo professor: grafos dirigidos e não dirigidos,
árvores geradoras mínimas e caminhos mínimos. Ele define o padrão que os
trabalhos seguem — grafo como vetor de `Bag`, e cada algoritmo como uma
classe que computa no construtor e expõe o resultado por consultas
(`marked(v)`, `count`, `path_to(v)`, …).

Os exemplos do `algs4-py` esperam arquivos de entrada em `algs4-py/../dataset/`,
pasta que **não** está versionada aqui; para rodá-los é preciso baixar os
`tinyG.txt`, `tinyDG.txt`, `tinyCG.txt` etc. do projeto original.

## Trabalhos

| trabalho | problema | técnica |
|---|---|---|
| [T1 — Dominó 2](unidade-1/trabalhos/domino2/T1/) | reação em cadeia de dominós | alcançabilidade multi-fonte por DFS, `O(V+E)` |
