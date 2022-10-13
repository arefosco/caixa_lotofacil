

"""
# a_a
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    amount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# a_b
    numbers_dict = {
        1: {'qt': 0}, 2: {'qt': 0}, 3: {'qt': 0}, 4: {'qt': 0}, 5: {'qt': 0}, 6: {'qt': 0}, 7: {'qt': 0},
        8: {'qt': 0}, 9: {'qt': 0}, 10: {'qt': 0}, 11: {'qt': 0}, 12: {'qt': 0}, 13: {'qt': 0}, 14: {'qt': 0},
        15: {'qt': 0}, 16: {'qt': 0}, 17: {'qt': 0}, 18: {'qt': 0}, 19: {'qt': 0}, 20: {'qt': 0}, 21: {'qt': 0},
        22: {'qt': 0}, 23: {'qt': 0}, 24: {'qt': 0}, 25: {'qt': 0}
    }

# a_c
    numbers_dict = {
        1: {'qt': 1566}, 2: {'qt': 1564}, 3: {'qt': 1589}, 4: {'qt': 1576}, 5: {'qt': 1599}, 6: {'qt': 1529},
        7: {'qt': 1538}, 8: {'qt': 1505}, 9: {'qt': 1568}, 10: {'qt': 1630}, 11: {'qt': 1626}, 12: {'qt': 1571},
        13: {'qt': 1603}, 14: {'qt': 1601}, 15: {'qt': 1557}, 16: {'qt': 1519}, 17: {'qt': 1560}, 18: {'qt': 1572},
        19: {'qt': 1569}, 20: {'qt': 1634}, 21: {'qt': 1557}, 22: {'qt': 1567}, 23: {'qt': 1552}, 24: {'qt': 1603},
        25: {'qt': 1620}
    }

# a_d
    rank_frequency = [
        (1, {'qt': 1566}), (2, {'qt': 1564}), (3, {'qt': 1589}), (4, {'qt': 1576}), (5, {'qt': 1599}),
        (6, {'qt': 1529}), (7, {'qt': 1538}), (8, {'qt': 1505}), (9, {'qt': 1568}), (10, {'qt': 1630}),
        (11, {'qt': 1626}), (12, {'qt': 1571}), (13, {'qt': 1603}), (14, {'qt': 1601}), (15, {'qt': 1557}),
        (16, {'qt': 1519}), (17, {'qt': 1560}), (18, {'qt': 1572}), (19, {'qt': 1569}), (20, {'qt': 1634}),
        (21, {'qt': 1557}), (22, {'qt': 1567}), (23, {'qt': 1552}), (24, {'qt': 1603}), (25, {'qt': 1620})
    ]

# a_e
    rank_frequency_ordered = [
        (20, {'qt': 1634}), (10, {'qt': 1630}), (11, {'qt': 1626}), (25, {'qt': 1620}), (13, {'qt': 1603}),
        (24, {'qt': 1603}), (14, {'qt': 1601}), (5, {'qt': 1599}), (3, {'qt': 1589}), (4, {'qt': 1576}),
        (18, {'qt': 1572}), (12, {'qt': 1571}), (19, {'qt': 1569}), (9, {'qt': 1568}), (22, {'qt': 1567}),
        (1, {'qt': 1566}), (2, {'qt': 1564}), (17, {'qt': 1560}), (15, {'qt': 1557}), (21, {'qt': 1557}),
        (23, {'qt': 1552}), (7, {'qt': 1538}), (6, {'qt': 1529}), (16, {'qt': 1519}), (8, {'qt': 1505})
    ]

# a_f
    rank_frequency_ordered_array = [
        [20, {'qt': 1634}], [10, {'qt': 1630}], [11, {'qt': 1626}], [25, {'qt': 1620}], [13, {'qt': 1603}],
        [24, {'qt': 1603}], [14, {'qt': 1601}], [5, {'qt': 1599}], [3, {'qt': 1589}], [4, {'qt': 1576}],
        [18, {'qt': 1572}], [12, {'qt': 1571}], [19, {'qt': 1569}], [9, {'qt': 1568}], [22, {'qt': 1567}],
        [1, {'qt': 1566}], [2, {'qt': 1564}], [17, {'qt': 1560}], [15, {'qt': 1557}], [21, {'qt': 1557}],
        [23, {'qt': 1552}], [7, {'qt': 1538}], [6, {'qt': 1529}], [16, {'qt': 1519}], [8, {'qt': 1505}]
    ]

# a_g
    rank_frequency_ordered_array = [
        [20, {'qt': 1634}, 62.25], [10, {'qt': 1630}, 62.1], [11, {'qt': 1626}, 61.94], [25, {'qt': 1620}, 61.71],
        [13, {'qt': 1603}, 61.07], [24, {'qt': 1603}, 61.07], [14, {'qt': 1601}, 60.99], [5, {'qt': 1599}, 60.91],
        [3, {'qt': 1589}, 60.53], [4, {'qt': 1576}, 60.04], [18, {'qt': 1572}, 59.89], [12, {'qt': 1571}, 59.85],
        [19, {'qt': 1569}, 59.77], [9, {'qt': 1568}, 59.73], [22, {'qt': 1567}, 59.7], [1, {'qt': 1566}, 59.66],
        [2, {'qt': 1564}, 59.58], [17, {'qt': 1560}, 59.43], [15, {'qt': 1557}, 59.31], [21, {'qt': 1557}, 59.31],
        [23, {'qt': 1552}, 59.12], [7, {'qt': 1538}, 58.59], [6, {'qt': 1529}, 58.25], [16, {'qt': 1519}, 57.87],
        [8, {'qt': 1505}, 57.33]
    ]

# a_h
    most_frequent = [20, 10, 11, 25, 13, 24, 14, 5, 3, 4]

# a_i
    most_frequent_amount = 10

# a_j
    less_frequent = {1, 2, 6, 7, 8, 9, 12, 15, 16, 17, 18, 19, 21, 22, 23}

# a_k: Valor 2 não é quebrado, pois o cálculo não deu um número quebrado
    calculus_for_40 = 4.0
    percentage_40 = 4

# a_l: Valor 2 não é quebrado, pois o cálculo não deu um número quebrado
    calculus_for_70 = 7.0
    percentage_70 = 7

# a_m
    percentage_40 = 4
    percentage_70 = 7

# a_n
    percentages = {'40%': 4, '70%': 7}
"""

from banco_de_dados.banco import dtb
from collections import Counter

# a_a: Dados criados e a serem inseridos em "numbers_dict"
numbers = list(range(1, 26))
number = 0
amount = []
[amount.append(number) for n in range(25)]

# a_b: Criação de um dicionário sem digitar dados manualmente (usando os dados acima) (que serão alterados abaixo)
numbers_dict = {}
for index in range(len(numbers)):
    numbers_dict[numbers[index]] = {'qt': amount[index]}

# a_c: Cada número de jogo do banco é analizado. e cada chave recebe incremento conforme cada número é achado num jogo
for index, tuple_ in enumerate(dtb):
    for number in tuple_:
        if number == 1: numbers_dict[number]['qt'] += 1
        elif number == 2: numbers_dict[number]['qt'] += 1
        elif number == 3: numbers_dict[number]['qt'] += 1
        elif number == 4: numbers_dict[number]['qt'] += 1
        elif number == 5: numbers_dict[number]['qt'] += 1
        elif number == 6: numbers_dict[number]['qt'] += 1
        elif number == 7: numbers_dict[number]['qt'] += 1
        elif number == 8: numbers_dict[number]['qt'] += 1
        elif number == 9: numbers_dict[number]['qt'] += 1
        elif number == 10: numbers_dict[number]['qt'] += 1
        elif number == 11: numbers_dict[number]['qt'] += 1
        elif number == 12: numbers_dict[number]['qt'] += 1
        elif number == 13: numbers_dict[number]['qt'] += 1
        elif number == 14: numbers_dict[number]['qt'] += 1
        elif number == 15: numbers_dict[number]['qt'] += 1
        elif number == 16: numbers_dict[number]['qt'] += 1
        elif number == 17: numbers_dict[number]['qt'] += 1
        elif number == 18: numbers_dict[number]['qt'] += 1
        elif number == 19: numbers_dict[number]['qt'] += 1
        elif number == 20: numbers_dict[number]['qt'] += 1
        elif number == 21: numbers_dict[number]['qt'] += 1
        elif number == 22: numbers_dict[number]['qt'] += 1
        elif number == 23: numbers_dict[number]['qt'] += 1
        elif number == 24: numbers_dict[number]['qt'] += 1
        elif number == 25: numbers_dict[number]['qt'] += 1

# a_d: As chaves e valores são convertidos em tuplas por causa de "Counter", mas não estão ordenados (ainda)
rank_frequency = list(Counter(numbers_dict).items())

# a_e: Então serão ordenados aqui (por agora serem tuplas)
# a_e: Porém, é desejado que cada tupla tenha um terceiro índice aninhado desejado ao cálculo da porcentagem
# a_e: Por serem tuplas, não aceitam dados novos, então se deve converter todas as tuplas para listas
rank_frequency_ordered = sorted(rank_frequency, key=lambda the_index: the_index[1]['qt'], reverse=True)

# a_f: Conversão de cada tupla p/ lista p/ receber porcentagem
rank_frequency_ordered_array = [list(tuple_) for tuple_ in rank_frequency_ordered]

# a_g: ANTES: Converte [5, 841] em [5, 841, 32.79] (em cada índice, que é uma tupla, adicionar novo dado: porcentagem)
for index, data in enumerate(rank_frequency_ordered_array):
    rank_frequency_ordered_array[index].append(
        float(f"{(rank_frequency_ordered_array[index][1]['qt'] * 100) / len(dtb):.2f}")
    )

"VAR usada em [ numbers_frequency ]"
# a_h: São anexados à "most_frequent" os números que atingirem + de 60% de frequência na história da loteria
# a_h: Neste caso, é adicionado o índice 0, que corresponde apenas ao número, chamado via índice 2 (porcentagem)
most_frequent = []
[most_frequent.append(tuple_i[0]) if tuple_i[2] > 60 else None for tuple_i in rank_frequency_ordered_array]

# a_i: Dado essencial para calcular porcentagem abaixo (será explicado abaixo)
most_frequent_amount = len(most_frequent)

# a_j: Separar os números fora dos mais comuns dos mais comuns (apenas para info, não é usada)
less_frequent = set(numbers).difference(set(most_frequent))

# Exemplo do que será feito em [ numbers_frequency ], onde "example" é o self.game
example = [1, 2, 6, 7, 8, 9, 12, 15, 16, 17, 18, 19, 20, 24, 25]
similarity = len(set(example).intersection(set(most_frequent)))

"EXEMPLO QUANDO 40% DOS NÚMEROS FOR UM NÚMERO QUEBRADO"
# broken_number = 9
# amount_extracted = (40 * broken_number) / 100
# amount_extracted_str = str(amount_extracted)
# # Tratar o valor para quando for quebrado (pegar apenas o índice 0 do resultado do cálculo)
# amount = None
# if len(amount_extracted_str) > 1:
#     amount = int(amount_extracted_str[0])
""

# a_k: Usando "a_i", se pode saber quanto é 40% de "a_h" e depois convertido em string p/ tratamento
percentage_40 = None
calculus_for_40 = (40 * most_frequent_amount) / 100
result_40 = str(calculus_for_40)

# a_l: Usando "a_i", se pode saber quanto é 70% de "a_h" e depois convertido em string p/ tratamento
percentage_70 = None
calculus_for_70 = (70 * most_frequent_amount) / 100
result_70 = str(calculus_for_70)

# a_m: Tratar as quantidades que representam as porcentagens para quando for quebrado
# a_m: É pego apenas o índice 0 do resultado do cálculo, que representa a parte inteira, que é reconvertida p/ inteiro
if len(result_40) > 1: percentage_40 = int(result_40[0])
if len(result_70) > 1: percentage_70 = int(result_70[0])

# a_n: Os dados, após tratados, são inseridos num dicionário para terem maior legibilidade
percentages = {'40%': percentage_40, '70%': percentage_70}

if __name__ == '__main__':
    print(numbers_dict)

    print(f"{rank_frequency =  }")
    print(f"{rank_frequency_ordered = }")
    print(f"{rank_frequency_ordered_array = }")
    print('Os números abaixo têm frequência acima de 60% (podem mudar a cada jogo)')
    print(f"{most_frequent = }")
    print('Quantidade de números comuns atualmente na lista?')
    print(f"{most_frequent_amount = }")

    print(f"{less_frequent = }")
    print(f"{similarity = }")

    print(f"\nProgresso do tratamento do valor correspondente a 40% da lista de números mais frequentes")
    print(f"{calculus_for_40 = }")
    print(f"{result_40 = }")
    print(f"{percentage_40 = }")

    print(f"\nProgresso do tratamento do valor correspondente a 70% da lista de números mais frequentes")
    print(f"{calculus_for_70 = }")
    print(f"{result_70 = }")
    print(f"{percentage_70 = }")
