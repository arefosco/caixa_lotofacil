

from banco_de_dados.banco import dtb
from collections import Counter


def get_border_or_center_size(game_var, site):

    card_edges = []
    card_center = []

    # Todos os números de borda do volante
    for n in list(game_var):
        if n == 1 or n == 2 or n == 3 or n == 4 or n == 5 or \
           n == 10 or n == 15 or n == 20 or n == 25 or \
           n == 24 or n == 23 or n == 22 or n == 21 or \
           n == 16 or n == 11 or n == 6:
            card_edges.append(n)

    # Todos os números de centro do volante
    for n in list(game_var):
        if n == 7 or n == 8 or n == 9 or n == 12 or n == 13 or n == 14 or n == 17 or n == 18 or n == 19:
            card_center.append(n)

    if site == 'edges': return card_edges
    elif site == 'center': return card_center


# ======================================================= CANTOS =======================================================
rank_edges = []

for tuple_ in dtb: rank_edges.append(get_border_or_center_size(game_var=tuple_, site='edges'))

rank_edges_converted = list(Counter([len(array) for array in rank_edges]).items())

rank_edges_converted_array = [list(tuple_) for tuple_ in rank_edges_converted]

for index, data in enumerate(rank_edges_converted_array):
    rank_edges_converted_array[index].append(
        float(f"{(rank_edges_converted_array[index][1] * 100) / len(dtb):.2f}")
    )

rank_edges_converted_array_sorted = sorted(rank_edges_converted_array, key=lambda this_index: this_index[2], reverse=True)

most_frequent_edges = []
less_frequent_edges = []
[most_frequent_edges.append(tuple_i[0]) if tuple_i[2] > 10 else less_frequent_edges.append(tuple_i[0])
 for tuple_i in rank_edges_converted_array_sorted]

# ======================================================= CENTRO =======================================================
rank_centers = []
for tuple_ in dtb: rank_centers.append(get_border_or_center_size(game_var=tuple_, site='center'))

rank_centers_converted = list(Counter([len(array) for array in rank_centers]).items())

rank_centers_converted_array = [list(tuple_) for tuple_ in rank_centers_converted]

for index, data in enumerate(rank_centers_converted_array):
    rank_centers_converted_array[index].append(
        float(f"{(rank_centers_converted_array[index][1] * 100) / len(dtb):.2f}")
    )

rank_centers_converted_array_sorted = sorted(rank_centers_converted_array, key=lambda this_index: this_index[2], reverse=True)

most_frequent_centers = []
less_frequent_centers = []
[most_frequent_centers.append(tuple_i[0]) if tuple_i[2] > 10 else less_frequent_centers.append(tuple_i[0])
 for tuple_i in rank_centers_converted_array_sorted]

if __name__ == '__main__':
    # ==================================================== CANTOS ====================================================
    print(f"{rank_edges_converted = }")
    print(f"{rank_edges_converted_array = }")
    print(f"{rank_edges_converted_array = }")
    print(f"{rank_edges_converted_array_sorted = }")
    print(f"{most_frequent_edges = }")
    print(f"{less_frequent_edges = }")

    # ==================================================== CENTROS ====================================================
    print(f"{rank_centers_converted = }")
    print(f"{rank_centers_converted_array = }")
    print(f"{rank_centers_converted_array = }")
    print(f"{rank_centers_converted_array_sorted = }")
    print(f"{most_frequent_centers = }")
    print(f"{less_frequent_centers = }")
