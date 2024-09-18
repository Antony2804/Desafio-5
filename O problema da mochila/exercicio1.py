import random

def avaliar_fitness(cromossomo, pesos, valores, peso_maximo):
    valor_total = 0
    peso_total = 0
    
    for i in range(len(cromossomo)):
        if cromossomo[i] == 1:
            peso_total += pesos[i]
            valor_total += valores[i]
    
    if peso_total > peso_maximo:
        return 0  
    return valor_total

def gerar_cromossomo(n):
    return [random.randint(0, 1) for _ in range(n)]

def crossover(pai1, pai2):
    ponto_corte = random.randint(1, len(pai1) - 1)
    filho1 = pai1[:ponto_corte] + pai2[ponto_corte:]
    filho2 = pai2[:ponto_corte] + pai1[ponto_corte:]
    return filho1, filho2

def mutacao(cromossomo, taxa_mutacao=0.01):
    for i in range(len(cromossomo)):
        if random.random() < taxa_mutacao:
            cromossomo[i] = 1 - cromossomo[i] 
    return cromossomo

def algoritmo_genetico(pesos, valores, peso_maximo, num_geracoes, num_individuos):
    num_itens = len(pesos)
    
    populacao = [gerar_cromossomo(num_itens) for _ in range(num_individuos)]
    melhor_individuo_geracao = []
    
    for geracao in range(num_geracoes):

        fitness = [avaliar_fitness(cromossomo, pesos, valores, peso_maximo) for cromossomo in populacao]
        
        melhor_fitness = max(fitness)
        melhor_individuo = populacao[fitness.index(melhor_fitness)]
        melhor_individuo_geracao.append(melhor_individuo)
        
        nova_populacao = []
        while len(nova_populacao) < num_individuos:
            pai1 = torneio(populacao, fitness)
            pai2 = torneio(populacao, fitness)
            filho1, filho2 = crossover(pai1, pai2)
            nova_populacao.extend([mutacao(filho1), mutacao(filho2)])
        
        populacao = nova_populacao[:num_individuos]
    
    fitness_final = [avaliar_fitness(cromossomo, pesos, valores, peso_maximo) for cromossomo in populacao]
    melhor_fitness_final = max(fitness_final)
    melhor_solucao = populacao[fitness_final.index(melhor_fitness_final)]
    
    return melhor_solucao, melhor_individuo_geracao

def torneio(populacao, fitness):
    competidores = random.sample(list(zip(populacao, fitness)), 3)
    competidores.sort(key=lambda x: x[1], reverse=True)
    return competidores[0][0]

pesos = [2, 3, 6, 7, 5]
valores = [6, 5, 8, 9, 7]
peso_maximo = 15
num_geracoes = 100
num_individuos = 10

melhor_solucao, melhores_por_geracao = algoritmo_genetico(pesos, valores, peso_maximo, num_geracoes, num_individuos)

print("Melhor solução:", melhor_solucao)
print("Melhores indivíduos por geração:", melhores_por_geracao)
