

from banco_de_dados.banco import dtb
from collections import Counter


def sequence_horizontal(game):

    line1, line2, line3, line4, line5 = 0, 0, 0, 0, 0

    line1_numbers = [*range(1, 6)]    # 1, 2, 3, 4, 5
    line2_numbers = [*range(6, 11)]   # 6, 7, 8, 9, 10
    line3_numbers = [*range(11, 16)]  # 11, 12, 13, 14, 15
    line4_numbers = [*range(16, 21)]  # 16, 17, 18, 19, 20
    line5_numbers = [*range(21, 26)]  # 21, 22, 23, 24, 25

    for number in game:
        if number in line1_numbers:
            line1 += 1
        elif number in line2_numbers:
            line2 += 1
        elif number in line3_numbers:
            line3 += 1
        elif number in line4_numbers:
            line4 += 1
        elif number in line5_numbers:
            line5 += 1

    game_horizontal = [line1, line2, line3, line4, line5]

    if 0 not in game_horizontal:
        return {'blank_free': True, 'sequence': game_horizontal}
    return {'blank_free': False, 'sequence': game_horizontal}


ten_last = [dtb[-1], dtb[-2], dtb[-3], dtb[-4], dtb[-5], dtb[-6], dtb[-7], dtb[-8], dtb[-9], dtb[-10]]
ten_last_sequence_horizontal = [sequence_horizontal(game=game)['sequence'] for game in ten_last]

sequence_horizontal_all_games = []
sequence_horizontal_all_games_box = []

"1. Recebe dados para serem exibidos aqui (rank_str)"
for index in dtb:
    sequence_horizontal_all_games.append(str(sequence_horizontal(game=index)['sequence']))
rank_str = Counter([str(list_) for list_ in sequence_horizontal_all_games])

"2. Recebe dados para serem exibidos aqui e fora daqui (rank)"
for index in dtb:
    sequence_horizontal_all_games_box.append(sequence_horizontal(game=index)['sequence'])
rank = Counter([tuple(list_) for list_ in sequence_horizontal_all_games_box])

"Resultado de 1"
rank_10 = dict(rank_str.most_common(10))
rank_10_list = dict(rank.most_common(10))
rank_25 = dict(rank_str.most_common(25))

print('========== RANK GLOBAL ========== ')
print(rank_str)

print('========== CONSULTA: top 10 mais comuns (em var) ==========')
top_10_sequence_horizontal_box = tuple(rank_10_list.keys())
print(top_10_sequence_horizontal_box)

print('========== CONSULTA: top 10 mais comuns ==========')
for index in range(len(rank_10)):
    print(f'{tuple(rank_10.keys())[index]}: {tuple(rank_10.values())[index]}')

print('========== CONSULTA: top 25 mais comuns ==========')
for index in range(len(rank_25)):
    print(f'{tuple(rank_25.keys())[index]}: {tuple(rank_25.values())[index]}')

print('========== Sequências horizontais dos 10 últimos jogos ==========')
print(ten_last_sequence_horizontal)
