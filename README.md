1. Algoritmo Genético - Função Cúbica
Este programa usa um Algoritmo Genético (AG) para minimizar a função cúbica 
𝑓(𝑥)= 𝑥3 − 6𝑥+14 O AG é uma técnica de otimização inspirada na evolução natural. O objetivo é encontrar o valor de x que minimiza a função.

Funções principais:
funcao_objetivo(x):
Calcula o valor da função cúbica para um determinado valor de x.
Entrada: Um valor real x.
Saída: O valor de f(x) calculado.

decodificar_individuo(individuo_bin, intervalo=(-10, 10)):
Converte um indivíduo representado como um vetor binário (sequência de 0s e 1s) em um valor real dentro de um intervalo.
Entrada: Um indivíduo em binário e um intervalo (ex.: (-10, 10)).
Saída: O valor decimal correspondente a esse binário dentro do intervalo.

gerar_individuo(tamanho_cromossomo):
Cria um cromossomo (um indivíduo) aleatório de uma população, representado como uma lista de bits (0s e 1s).
Entrada: O tamanho do cromossomo.
Saída: Um vetor binário aleatório.

gerar_populacao(tamanho_populacao, tamanho_cromossomo):
Gera uma população inicial de indivíduos (cromossomos) aleatórios.
Entrada: O número de indivíduos e o tamanho do cromossomo.
Saída: Uma lista contendo a população.

selecao_torneio(populacao, fitness, tamanho_torneio=3):
Realiza a seleção de indivíduos para cruzamento usando o método de torneio, onde indivíduos competem entre si, e o melhor é selecionado.
Entrada: População, fitness de cada indivíduo e o tamanho do torneio.
Saída: O melhor indivíduo (cromossomo) entre os competidores.

crossover(pai1, pai2, tipo_crossover=1):
Realiza o cruzamento (crossover) entre dois pais para gerar novos filhos, combinando partes dos cromossomos.
Entrada: Dois cromossomos (pais) e o tipo de crossover (1 ponto ou 2 pontos de corte).
Saída: Dois novos cromossomos (filhos).

mutacao(individuo, taxa_mutacao):
Aplica mutação a um cromossomo, alterando bits aleatoriamente com uma certa taxa.
Entrada: Um cromossomo e a taxa de mutação.
Saída: O cromossomo com possíveis mutações.

aplicar_elitismo(populacao, fitness, percentual_elite):
Mantém os melhores indivíduos da população para garantir que as boas soluções não se percam ao longo das gerações.
Entrada: População, fitness e o percentual de elite.
Saída: Os melhores indivíduos da população.

algoritmo_genetico():
Executa o ciclo completo do AG, incluindo geração de população, seleção, cruzamento, mutação e elitismo (se habilitado).
Entrada: Parâmetros como tamanho da população, número de gerações, taxa de mutação, entre outros.
Saída: Exibe o melhor valor encontrado em cada geração e o melhor valor final.

------------------------------------------------------------------------------------------------------------------------------------------

2. Algoritmo Genético - Problema da Mochila (Knapsack Problem)
Este programa resolve o problema da mochila usando AG. O objetivo é maximizar o valor dos itens dentro de uma mochila sem exceder seu limite de peso.

Funções principais:

fitness(cromossomo, pesos_valores, peso_max):
Calcula o valor total e o peso total de um cromossomo (representação dos itens que foram colocados na mochila). Se o peso exceder o máximo permitido, o fitness será zero.
Entrada: Um cromossomo, uma lista de pesos e valores dos itens e o peso máximo permitido.
Saída: O valor total dos itens na mochila se o peso for válido, caso contrário, retorna 0.

gerar_cromossomo(tamanho):
Gera um cromossomo aleatório representando uma seleção de itens (0 ou 1 para cada item).
Entrada: O tamanho do cromossomo (número de itens).
Saída: Um cromossomo aleatório.

selecao_via_torneio(populacao, fitness_scores, k=3):
Seleciona um cromossomo usando o método de torneio, como no AG anterior.
Entrada: População, fitness de cada indivíduo e o tamanho do torneio.
Saída: O cromossomo vencedor do torneio.

crossover(pai1, pai2):
Faz o cruzamento de dois pais, gerando dois filhos.
Entrada: Dois cromossomos pais.
Saída: Dois cromossomos filhos.

mutacao(cromossomo, taxa_mutacao=0.01):
Aplica mutação a um cromossomo, trocando bits aleatoriamente com uma certa taxa.
Entrada: Um cromossomo e a taxa de mutação.
Saída: O cromossomo possivelmente mutado.

algoritmo_genetico(pesos_valores, peso_max, num_cromossomos, num_geracoes):
Executa o AG para o problema da mochila. A cada geração, gera novos indivíduos e avalia seus fitness.
Entrada: Lista de pesos e valores dos itens, peso máximo da mochila, número de cromossomos (indivíduos) e número de gerações.
Saída: Exibe o melhor valor encontrado em cada geração.

Comandos pra executar:
1. Instalar o Python
Certifique-se de que o Python está instalado em seu sistema. Para verificar, abra o terminal e digite:
python --version
Depois abra os 2 arquivos.
