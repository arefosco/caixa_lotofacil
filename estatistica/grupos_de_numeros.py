

from banco_de_dados.banco import dtb
from collections import Counter


def three_in_a_row_counter(game_var):
    i, i2, i3 = 1, 2, 3
    rows = []
    for n in range(23):
        rows.append([i, i2, i3])
        i += 1
        i2 += 1
        i3 += 1
    # print(rows)

    game_cells = [
        game_var[0:3], game_var[1:4], game_var[2:5], game_var[3:6], game_var[4:7], game_var[5:8], game_var[6:9],
        game_var[7:10], game_var[8:11], game_var[9:12], game_var[10:13], game_var[11:14], game_var[12:15]
    ]
    # print(game_cells)

    three_in_a_row_sequence = 0
    for cell in game_cells:
        if cell in rows:
            three_in_a_row_sequence += 1

    return three_in_a_row_sequence


rank = []
for game in dtb: rank.append(three_in_a_row_counter(list(game)))

rank_organized = list(Counter(rank).items())
rank_organized_array = [list(tuple_) for tuple_ in rank_organized]
absolute_frequency = len(dtb)  # sum([tuple_[1] for tuple_ in rank_organized])

[rank_organized_array[index].append(float(f"{(tuple_[1] * 100) / absolute_frequency:.2f}"))
 for index, tuple_ in enumerate(rank_organized_array)]

rank_organized_array_final = sorted(rank_organized_array, key=lambda index: index[2], reverse=True)

"Var para uso em [ three_in_a_row_counter ]"
three_in_a_row_common = []
[three_in_a_row_common.append(tuple_[0]) for tuple_ in rank_organized_array_final if tuple_[2] > 10]

if __name__ == '__main__':
    # Exemplo de 1 sequência e 2
    print(three_in_a_row_counter([1, 2, 3, 5, 7, 8, 10, 11, 13, 15, 16, 18, 20, 22, 23]))
    print(three_in_a_row_counter([1, 2, 3, 5, 7, 8, 10, 11, 12, 15, 16, 18, 20, 22, 23]))
    print(f"{rank = }")
    print(f"{rank_organized = }")
    print(f"{rank_organized_array = }")
    print(f"{absolute_frequency = }")
    print(f"{rank_organized_array = }")
    print(f"{rank_organized_array_final = }")
    print(f"{three_in_a_row_common = }")
