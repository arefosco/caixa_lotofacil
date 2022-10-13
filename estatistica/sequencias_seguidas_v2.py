

from banco_de_dados.banco import dtb


def avoid_large_odd_even_sequence(game_var):
    box = []

    # Um jogo analizado "self.game" têm seus números pares convertidos em 'p' e ímpares em 'i'
    odd, even = 'p', 'i'
    [box.append(odd) if not number % 2 else box.append(even) for number in game_var]

    # A partir do jogo, é criada uma variável string somente com letras 'p' e 'i'
    box = "".join(box)

    return box


# Onde os resultados serão inseridos
rank = []

for game in dtb:
    # Após cada análise, se insere em "rank" o resultado se o jogo possui ou não uma linha em branco
    rank.append(avoid_large_odd_even_sequence(game))

# Possibilidades: até doze pares seguidos / até 13 ímpares seguidos / 2 seguidos é muito comum, então se começa por 3
chances = [
    'ppp', 'pppp', 'ppppp', 'pppppp', 'ppppppp', 'pppppppp', 'ppppppppp', 'pppppppppp', 'ppppppppppp', 'pppppppppppp',
    'iii', 'iiii', 'iiiii', 'iiiiii', 'iiiiiii', 'iiiiiiii', 'iiiiiiiii', 'iiiiiiiiii', 'iiiiiiiiiii', 'iiiiiiiiiiii',
    'iiiiiiiiiiiii'
]

# Atributos usados nos índices (0, 1, 2) da tupla "rank_ordered" (quantidades serão editadas abaixo)
counters = {
    'odd_3': {'qt': 0, 'id': 3, 'type': 'pares'}, 'odd_4': {'qt': 0, 'id': 4, 'type': 'pares'},
    'odd_5': {'qt': 0, 'id': 5, 'type': 'pares'}, 'odd_6': {'qt': 0, 'id': 6, 'type': 'pares'},
    'odd_7': {'qt': 0, 'id': 7, 'type': 'pares'}, 'odd_8': {'qt': 0, 'id': 8, 'type': 'pares'},
    'odd_9': {'qt': 0, 'id': 9, 'type': 'pares'}, 'odd_10': {'qt': 0, 'id': 10, 'type': 'pares'},
    'odd_11': {'qt': 0, 'id': 11, 'type': 'pares'}, 'odd_12': {'qt': 0, 'id': 12, 'type': 'pares'},
    'even_3': {'qt': 0, 'id': 3, 'type': 'ímpares'}, 'even_4': {'qt': 0, 'id': 4, 'type': 'ímpares'},
    'even_5': {'qt': 0, 'id': 5, 'type': 'ímpares'}, 'even_6': {'qt': 0, 'id': 6, 'type': 'ímpares'},
    'even_7': {'qt': 0, 'id': 7, 'type': 'ímpares'}, 'even_8': {'qt': 0, 'id': 8, 'type': 'ímpares'},
    'even_9': {'qt': 0, 'id': 9, 'type': 'ímpares'}, 'even_10': {'qt': 0, 'id': 10, 'type': 'ímpares'},
    'even_11': {'qt': 0, 'id': 11, 'type': 'ímpares'}, 'even_12': {'qt': 0, 'id': 12, 'type': 'ímpares'},
    'even_13': {'qt': 0, 'id': 13, 'type': 'ímpares'}
}

for code in rank:
    if chances[0] in code: counters['odd_3']['qt'] += 1
    if chances[1] in code: counters['odd_4']['qt'] += 1
    if chances[2] in code: counters['odd_5']['qt'] += 1
    if chances[3] in code: counters['odd_6']['qt'] += 1
    if chances[4] in code: counters['odd_7']['qt'] += 1
    if chances[5] in code: counters['odd_8']['qt'] += 1
    if chances[6] in code: counters['odd_9']['qt'] += 1
    if chances[7] in code: counters['odd_10']['qt'] += 1
    if chances[8] in code: counters['odd_11']['qt'] += 1
    if chances[9] in code: counters['odd_12']['qt'] += 1

for code in rank:
    if chances[10] in code: counters['even_3']['qt'] += 1
    if chances[11] in code: counters['even_4']['qt'] += 1
    if chances[12] in code: counters['even_5']['qt'] += 1
    if chances[13] in code: counters['even_6']['qt'] += 1
    if chances[14] in code: counters['even_7']['qt'] += 1
    if chances[15] in code: counters['even_8']['qt'] += 1
    if chances[16] in code: counters['even_9']['qt'] += 1
    if chances[17] in code: counters['even_10']['qt'] += 1
    if chances[18] in code: counters['even_11']['qt'] += 1
    if chances[19] in code: counters['even_12']['qt'] += 1
    if chances[20] in code: counters['even_13']['qt'] += 1

# Valor necessário para calcular as porcentagens nos índices (3, 4) da tupla "rank_ordered"
absolute_freq = sum([counters[key]['qt'] for key in counters])

# (qtd. repetições, classe (se par/ímpar), qtd. repetições do padrão, porcentagem, porcentagem string)
rank_ordered = [
    (counters[key]['id'],
     counters[key]['type'],
     counters[key]['qt'],
     float(f"{(counters[key]['qt'] * 100) / absolute_freq:.2f}"),
     f"{float((counters[key]['qt'] * 100) / absolute_freq):.2f}%",
     ) for key in counters
]

# Rank de tuplas mostrando as sequências de pares e ímpares mais comuns (pelo índice 3 = porcentagem)
research = sorted(rank_ordered, key=lambda index: index[3], reverse=True)

sequences_above_10_percent = []
sequences_below_10_percent = []
[sequences_below_10_percent.append(tuple_i) if tuple_i[3] < 10 else sequences_above_10_percent.append(tuple_i)
 for tuple_i in research]

"VAR referência p/ [ avoid_large_odd_even_sequence ]"
worst_sequences = []
for tuple_i in sequences_below_10_percent:
    if tuple_i[1] == 'ímpares': worst_sequences.append('i' * tuple_i[0])
    elif tuple_i[1] == 'pares': worst_sequences.append('p' * tuple_i[0])

# Por último, vamos separar as melhores
best_sequences = list(set(chances).difference(set(worst_sequences)))

if __name__ == '__main__':
    print(counters)
    print(rank_ordered)
    print(research)
    print(absolute_freq)

    print('\nSequências mais comuns de pares e ímpares seguidos')
    for data in research:
        print(data)

    print(f"{sequences_above_10_percent = }")
    print(f"{sequences_below_10_percent = }")

    # Sequências mais comuns de pares e ímpares seguidos (em código)
    print(f"\n{len(sequences_above_10_percent)} sequências conseguiram percentual acima de 10%")
    print(f"{best_sequences = }")

    # Sequências menos comuns de pares e ímpares seguidos (em código)'
    print(f"\n{len(sequences_below_10_percent)} sequências conseguiram percentual abaixo de 10%")
    print(f"{worst_sequences = }")
