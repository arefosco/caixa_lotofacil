

from banco_de_dados.banco import dtb
from collections import Counter


def divisible_by_3(game_var):

    divisibles = [3, 6, 9, 12, 15, 18, 21, 24]
    found = []
    counter = 0
    for number in game_var:
        if not number % 3:
            counter += 1

    [found.append(number) for number in divisibles if number in game_var]

    return {'amount': counter, 'which_ones': found}


print(divisible_by_3([3, 6, 9, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 25]))

rank_1st = []
rank_2nd = []
for game in dtb:
    rank_1st.append(divisible_by_3(game)['amount'])
    rank_2nd.append(divisible_by_3(game)['which_ones'])

divisibles_ = [3, 6, 9, 12, 15, 18, 21, 24]
indexes = list(range(len(divisibles_)))

rank_frequency = list(Counter(rank_1st).items())
absolute_freq = sum([tuple_[1] for tuple_ in rank_frequency])
rank_frequency_ordered = sorted(rank_frequency, key=lambda the_index: the_index[1], reverse=True)
rank_frequency_ordered_array = [list(tuple_) for tuple_ in rank_frequency_ordered]

# ANTES: Converte [5, 841] em [5, 841, 32.79] (em cada índice, que é uma tupla, adicionar novo dado: porcentagem)
for index, data in enumerate(rank_frequency_ordered_array):
    rank_frequency_ordered_array[index].append(
        float(f"{(rank_frequency_ordered_array[index][1] * 100) / absolute_freq:.2f}")
    )

# As quantidades de divisíveis por 3 que atingirem + de 10%, são inseridos aqui
main_divisibles_amount = []
[main_divisibles_amount.append(tuple_i[0]) if tuple_i[2] > 10 else None for tuple_i in rank_frequency_ordered_array]


if __name__ == '__main__':
    print(rank_1st)
    print(rank_2nd)

    print(f"{rank_frequency = }")
    print(f"{absolute_freq = }")
    print(f"{rank_frequency_ordered = }")
    print(f"{rank_frequency_ordered_array = }")
    print(f"{main_divisibles_amount = }")
