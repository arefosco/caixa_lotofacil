

from banco_de_dados.banco import dtb, ten_last

starts_with = {
    1: {'qt': 0}, 2: {'qt': 0}, 3: {'qt': 0}, 4: {'qt': 0}, 5: {'qt': 0}
}

finishes_with = {
    15: {'qt': 0}, 16: {'qt': 0}, 17: {'qt': 0}, 18: {'qt': 0}, 19: {'qt': 0}, 20: {'qt': 0}, 21: {'qt': 0},
    22: {'qt': 0}, 23: {'qt': 0}, 24: {'qt': 0}, 25: {'qt': 0}
}

# Contar quantos jogos começam: (1 a 4) e (5 p/ cima)
for game in dtb:
    if game[0] >= 5: starts_with[5]['qt'] += 1
    elif game[0] == 4: starts_with[4]['qt'] += 1
    elif game[0] == 3: starts_with[3]['qt'] += 1
    elif game[0] == 2: starts_with[2]['qt'] += 1
    elif game[0] == 1: starts_with[1]['qt'] += 1

# Contar quantos jogos terminam: (15, 25)
for game in dtb:
    if game[-1] == 15: finishes_with[15]['qt'] += 1
    if game[-1] == 16: finishes_with[16]['qt'] += 1
    if game[-1] == 17: finishes_with[17]['qt'] += 1
    if game[-1] == 18: finishes_with[18]['qt'] += 1
    if game[-1] == 19: finishes_with[19]['qt'] += 1
    if game[-1] == 20: finishes_with[20]['qt'] += 1
    if game[-1] == 21: finishes_with[21]['qt'] += 1
    if game[-1] == 22: finishes_with[22]['qt'] += 1
    if game[-1] == 23: finishes_with[23]['qt'] += 1
    if game[-1] == 24: finishes_with[24]['qt'] += 1
    if game[-1] == 25: finishes_with[25]['qt'] += 1

# Frequências necessárias para calcular a porcentagem em "rank_start" e "rank_end"
absolute_frequency_start = sum([starts_with[key]['qt'] for key in starts_with])
absolute_frequency_finish = sum([finishes_with[key]['qt'] for key in finishes_with])

# Dados não essenciais, usados apenas para gerar relatório de rank
keys_from_start = list(starts_with.keys())
keys_from_finish = list(finishes_with.keys())

# Dados não essenciais, usados apenas para saber os números iniciais dos 10 últimos jogos
ten_last_starting_numbers = [game[0] for game in ten_last]
ten_last_ending_numbers = [game[-1] for game in ten_last]

# 2 list comprehension que transferem dados (ex) (1, 120, 25.0) (Número inicial/final, frequência, porcentagem)
rank_start = [
    (
        key,
        starts_with[key]['qt'],
        float(f"{(starts_with[key]['qt'] * 100) / absolute_frequency_start:.2f}")
    )
    for key in starts_with
]

rank_end = [
    (key, finishes_with[key]['qt'], float(f"{(finishes_with[key]['qt'] * 100) / absolute_frequency_finish:.2f}"))
    for key in finishes_with
]

# Pelo índice 2 (porcentagem) das list comprehension criadas acima, as tuplas são organizadas
rank_start_ordered = sorted(rank_start, key=lambda index: index[2], reverse=True)
rank_end_ordered = sorted(rank_end, key=lambda index: index[2], reverse=True)

"VARS para a função [ proper_gap ]"
# Com base na porcentagem, cada tupla é analisada e se o (índice 2) for acima de 10%, o número é anexado (índice 0)
# EX1: se jogos que iniciam com 1 for maior que 10%, então allowed_at_start = [1]
# EX2: se jogos que terminam com 25 for maior que 10%, então allowed_at_end = [25]
allowed_at_start = []
allowed_at_end = []
[allowed_at_start.append(tuple_[0]) if tuple_[2] > 10 else None for tuple_ in rank_start_ordered]
[allowed_at_end.append(tuple_[0]) if tuple_[2] > 10 else None for tuple_ in rank_end_ordered]

if __name__ == '__main__':
    # for key in starts_with.items():
    #     print(key)
    #
    # for key in finishes_with.items():
    #     print(key)

    # print(absolute_frequency_start)
    # print(absolute_frequency_finish)

    for key in keys_from_start:
        print(f'===== Quantos jogos começaram com {key}? {starts_with[key]["qt"]} jogos =====')

    print('\n')

    for key in keys_from_finish:
        print(f'===== Quantos jogos terminaram com {key}? {finishes_with[key]["qt"]} jogos =====')

    print('\n(Primeiro número, frequência 0/10, porcentagem) dos 10 últimos jogos')
    for number in set(ten_last_starting_numbers):
        print(
            (
                number,
                ten_last_starting_numbers.count(number),
                f'{float(ten_last_starting_numbers.count(number) * 100 / len(ten_last_starting_numbers))}%'
            )
        )

    print('\n(Último número, frequência 0/10, porcentagem) dos 10 últimos jogos')
    for number in set(ten_last_ending_numbers):
        print(
            (
                number,
                ten_last_ending_numbers.count(number),
                f'{float(ten_last_ending_numbers.count(number) * 100 / len(ten_last_ending_numbers))}%'
            )
        )

    print('\n(Número inicial do jogo, Frequência, Porcentagem)')
    print(f"{rank_start_ordered = }")

    print('\n(Número final do jogo, Frequência, Porcentagem)')
    print(f"{rank_end_ordered = }")

    print('\nNúmeros de início de jogo acima de 10%')
    print(f"{allowed_at_start = }")

    print('\nNúmeros de fim de jogo acima de 10%')
    print(f"{allowed_at_end = }")
