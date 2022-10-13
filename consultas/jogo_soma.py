

from banco_de_dados.banco import dtb
from collections import Counter


def game_sum(game_var):
    return sum(game_var)


rank = []

# Inserção da soma de cada jogo em "rank"
for tuple_ in dtb:
    rank.append(game_sum(tuple_))

min_sum = sum(tuple(range(1, 16)))
max_sum = sum(tuple(range(11, 26)))

single_calculus = list(sorted(set(rank), reverse=True))


if __name__ == '__main__':
    print('Pontuação máxima do jogo')
    print(f"{max_sum = }")
    print(f"{min_sum = }")
    print(f"{single_calculus = }")
    print(Counter(rank))
