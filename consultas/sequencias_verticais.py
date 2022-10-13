

from banco_de_dados.banco import dtb
from collections import Counter


def sequence_vertical(game):
    line1, line2, line3, line4, line5 = 0, 0, 0, 0, 0

    line1_numbers = [1, 6, 11, 16, 21]
    line2_numbers = [2, 7, 12, 17, 22]
    line3_numbers = [3, 8, 13, 18, 23]
    line4_numbers = [4, 9, 14, 19, 24]
    line5_numbers = [5, 10, 15, 20, 25]

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

    game_vertical = [line1, line2, line3, line4, line5]

    if 0 not in game_vertical:
        return {'blank_free': True, 'sequence': game_vertical}
    return {'blank_free': False, 'sequence': game_vertical}


ten_last = [dtb[-1], dtb[-2], dtb[-3], dtb[-4], dtb[-5], dtb[-6], dtb[-7], dtb[-8], dtb[-9], dtb[-10]]
ten_last_sequence_vertical = [sequence_vertical(game=game)['sequence'] for game in ten_last]

sequence_vertical_all_games = []
sequence_vertical_all_games_box = []

"1. Recebe dados para serem exibidos aqui (rank_str)"
for index in dtb:
    sequence_vertical_all_games.append(str(sequence_vertical(game=index)['sequence']))
rank_str = Counter([str(list_) for list_ in sequence_vertical_all_games])

"2. Recebe dados para serem exibidos aqui e fora daqui (rank)"
for index in dtb:
    sequence_vertical_all_games_box.append(sequence_vertical(game=index)['sequence'])
rank = Counter([tuple(list_) for list_ in sequence_vertical_all_games_box])

"Resultado de 1"
rank_10 = dict(rank_str.most_common(10))
rank_10_list = dict(rank.most_common(10))
rank_25 = dict(rank_str.most_common(25))

print('========== RANK GLOBAL ========== ')
print(rank_str)

print('========== CONSULTA: top 10 mais comuns (em var) ==========')
top_10_sequence_vertical_box = tuple(rank_10_list.keys())
print(top_10_sequence_vertical_box)

print('========== CONSULTA: top 10 mais comuns ==========')
for index in range(len(rank_10)):
    print(f'{tuple(rank_10.keys())[index]}: {tuple(rank_10.values())[index]}')

print('========== CONSULTA: top 25 mais comuns ==========')
for index in range(len(rank_25)):
    print(f'{tuple(rank_25.keys())[index]}: {tuple(rank_25.values())[index]}')

print('========== Sequências verticais dos 10 últimos jogos ==========')
print(ten_last_sequence_vertical)
