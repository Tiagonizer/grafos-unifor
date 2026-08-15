import sys

def resolver():
    """
    Passo 1: Ler os dados de entrada
    """    
    entrada = sys.stdin.read().split()
    if not entrada: 
        return

    ponteiro = 0
    casos_de_teste = int(entrada[ponteiro])
    ponteiro += 1

    for _ in range(casos_de_teste):
        n = int(entrada[ponteiro])
        m = int(entrada[ponteiro + 1])
        l = int(entrada[ponteiro + 2])
        ponteiro += 3

        """
        Passo 2: Montar a Lista de Adjacência (DENTRO do for de testes)
        """
        # Criamos n+1 listas vazias (exemplo para n=3: [[], [], [], []])
        adj = [[] for _ in range(n + 1)]

        # Lemos as 'm' conexões (arestas)
        for _ in range(m):
            x = int(entrada[ponteiro])
            y = int(entrada[ponteiro + 1])
            # Como a queda é direcionada (x derruba y), só colocamos y na lista de x
            adj[x].append(y)
            ponteiro += 2

        """
        Passo 3: Simular a queda dos dominós (DENTRO do for de testes)
        """
        caido = [False] * (n + 1)
        total_caidos = 0

        # Lemos os 'l' dominós empurrados manualmente
        for _ in range(l):
            z = int(entrada[ponteiro])
            ponteiro += 1

            # Se a peça 'z' ainda não caiu, nós derrubamos ela
            if not caido[z]:
                caido[z] = True
                total_caidos += 1
                pilha = [z]

                # Enquanto houver dominós caindo na reação em cadeia
                while pilha:
                    atual = pilha.pop()  # Pega o último dominó que caiu

                    # Olha todos os vizinhos que o dominó 'atual' derruba
                    for vizinho in adj[atual]:
                        if not caido[vizinho]:
                            caido[vizinho] = True
                            total_caidos += 1
                            pilha.append(vizinho) # Guarda para olhar os vizinhos dele depois

        # Imprime o resultado do caso de teste atual
        print(total_caidos)

# Ponto de entrada: manda o programa executar a função resolver()
if __name__ == "__main__":
    resolver()