import random

def fitness(cromossomo, pesos_valores, peso_max):
    valor_total = 0
    peso_total = 0
    
    for i in range(len(cromossomo)):
        if cromossomo[i] == 1:
            peso_total += pesos_valores[i][0]
            valor_total += pesos_valores[i][1]
    
    if peso_total > peso_max:
        return 0 
    else:
        return valor_total

def gerar_cromossomo(tamanho):
    return [random.randint(0, 1) for _ in range(tamanho)]

def selecao_via_torneio(populacao, fitness_scores, k=3):
    torneio = random.sample(list(zip(populacao, fitness_scores)), k)
    return max(torneio, key=lambda x: x[1])[0]

def crossover(pai1, pai2):
    ponto_de_corte = random.randint(1, len(pai1) - 1)
    filho1 = pai1[:ponto_de_corte] + pai2[ponto_de_corte:]
    filho2 = pai2[:ponto_de_corte] + pai1[ponto_de_corte:]
    return filho1, filho2

def mutacao(cromossomo, taxa_mutacao=0.01):
    for i in range(len(cromossomo)):
        if random.random() < taxa_mutacao:
            cromossomo[i] = 1 - cromossomo[i] 
    return cromossomo

def algoritmo_genetico(pesos_valores, peso_max, num_cromossomos, num_geracoes):
    populacao = [gerar_cromossomo(len(pesos_valores)) for _ in range(num_cromossomos)]
    
    resultado_por_geracao = []
    
    for geracao in range(num_geracoes):
        fitness_scores = [fitness(cromo, pesos_valores, peso_max) for cromo in populacao]
        
        melhor_individuo = max(populacao, key=lambda cromo: fitness(cromo, pesos_valores, peso_max))
        melhor_valor = fitness(melhor_individuo, pesos_valores, peso_max)
        resultado_por_geracao.append([melhor_valor, melhor_individuo])
        
        nova_populacao = []
        
        while len(nova_populacao) < num_cromossomos:
            pai1 = selecao_via_torneio(populacao, fitness_scores)
            pai2 = selecao_via_torneio(populacao, fitness_scores)
            filho1, filho2 = crossover(pai1, pai2)
            filho1 = mutacao(filho1)
            filho2 = mutacao(filho2)
            nova_populacao.extend([filho1, filho2])
        
        populacao = nova_populacao[:num_cromossomos]  
    
    return resultado_por_geracao

pesos_e_valores = [[2, 10], [4, 30], [6, 300], [8, 10], [8, 30], [8, 300], [12, 50], [25, 75], [50, 100], [100, 400]]
peso_maximo = 100
numero_de_cromossomos = 150
geracoes = 50

resultado = algoritmo_genetico(pesos_e_valores, peso_maximo, numero_de_cromossomos, geracoes)

for i, (valor, individuo) in enumerate(resultado[:10]):
    print(f"Geração {i + 1}: Valor = {valor}, Indivíduo = {individuo}")
