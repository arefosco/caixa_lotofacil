

from banco_de_dados.banco import dtb
from collections import Counter

divisible_by_3_most_common = ()


def get_divisible_by_3_test(the_game):
    # divisible_by_3 = [3, 6, 9, 12, 15, 18, 21, 24]
    box = []
    for number in the_game:
        if not number % 3:
            box.append(number)

    return {'amount_found': len(box), 'found': box}


# TODO: Para usar no algoritmo, onde "right_amount" é o "ALVO" neste documento
def get_divisible_by_3(the_game, right_amount: tuple):
    # divisible_by_3 = [3, 6, 9, 12, 15, 18, 21, 24]
    box = []
    for number in the_game:
        if not number % 3:
            box.append(number)

    if len(box) in right_amount:
        return {'amount_found': len(box), 'found': box, 'acceptable': True}
    if len(box) not in right_amount:
        return {'amount_found': len(box), 'found': box, 'acceptable': False}


ten_last = [dtb[-1], dtb[-2], dtb[-3], dtb[-4], dtb[-5], dtb[-6], dtb[-7], dtb[-8], dtb[-9], dtb[-10]]
ten_last_divisible3_amount = [get_divisible_by_3_test(the_game=game)['amount_found'] for game in ten_last]

divisible3_all_games = []
divisible3_all_games_box = []

"1. Recebe dados para serem exibidos aqui (rank_str)"
for index in dtb:
    divisible3_all_games.append(str(get_divisible_by_3_test(the_game=index)['amount_found']))
rank_str = Counter([str(int_) for int_ in divisible3_all_games])

"2. Recebe dados para serem exibidos aqui e fora daqui (rank)"
for index in dtb:
    divisible3_all_games_box.append(get_divisible_by_3_test(the_game=index)['amount_found'])
rank = Counter([int_ for int_ in divisible3_all_games_box])

"Resultado de 1"
rank_10 = dict(rank_str.most_common(10))
rank_10_list = dict(rank.most_common(10))
divisible_by_3_top3 = dict(rank.most_common(3))

print('========== RANK GLOBAL ========== ')
print(rank_str)

print('========== CONSULTA: top 10 mais comuns (em var) ==========')
top_10_divisible3_box = tuple(rank_10_list.keys())
print(top_10_divisible3_box)

# TODO: ALVO
print('========== CONSULTA: top 3 mais comuns (em var) ==========')
divisible_by_3_top3_tuple = tuple(divisible_by_3_top3.keys())
print(divisible_by_3_top3_tuple)

print('========== CONSULTA: top 10 mais comuns ==========')
for index in range(len(rank_10)):
    print(f'{tuple(rank_10.keys())[index]}: {tuple(rank_10.values())[index]}')

print('========== Qtd. de números divisíveis por 3 dos 10 últimos jogos ==========')
print(ten_last_divisible3_amount)
