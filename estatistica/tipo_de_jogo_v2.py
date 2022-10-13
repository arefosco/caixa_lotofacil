

from banco_de_dados.banco import dtb


def game_type(game_var):
    # Contador da parte 1, contador da parte2, parte 1 do volante, parte 2 do volante
    upper, lower, upper_area, lower_area = 0, 0, tuple(range(1, 16)), tuple(range(16, 26))

    for number in game_var:
        if number in upper_area: upper += 1
        elif number in lower_area: lower += 1

    game_class = f"{upper}/{lower}"

    return game_class


# Onde os resultados serão inseridos
rank = []

# "rank" receberá o tipo de jogo de cada jogo do banco
for game in dtb: rank.append(f"{game_type(game)}")

# Var usada para calcular porcentagem
absolute_frequence = len(dtb)

# Cada tipo de jogo possível usado em "relative_freqs"
types = ['5/10', '6/9', '7/8', '8/7', '9/6', '10/5', '11/4', '12/3', '13/2', '14/1', '15/0']

relative_freqs = (
    rank.count('5/10'), rank.count('6/9'), rank.count('7/8'), rank.count('8/7'), rank.count('9/6'),
    rank.count('10/5'), rank.count('11/4'), rank.count('12/3'), rank.count('13/2'), rank.count('14/1'),
    rank.count('15/0')
)

# (tipo do jogo, frequência, porcentagem, porcentagem em str) EX: ['8/7', '100 jogos', 15.00, 15.00%]
all_data = []
for index, freq in enumerate(relative_freqs):
    all_data.append(
        (types[index],
         f'{freq} jogos',
         float(f'{(freq * 100) / absolute_frequence:.2f}'),
         f"{float(f'{(freq * 100) / absolute_frequence:.2f}')}%")
    )

# Dados organizados pelo valor de porcentagem (índice 2)
rank_organized = sorted(all_data, key=lambda all_data_index: all_data_index[2], reverse=True)

"VAR para uso em [ game_type ]"
# Separar os 3 tipos de jogos mais frequentes
game_types = []
[game_types.append(tuple_index[0]) for tuple_index in rank_organized[0:3]]

if __name__ == '__main__':
    print('=============================================== RELATÓRIO ===============================================')
    print('Rank em porcentagem da qtd. de tipos de jogos mais recorrentes')
    for report in rank_organized:
        print(report)
    print('Os 3 tipos de jogos mais frequentes (outros são desprezados por porcentagem muito baixa)')
    print(game_types)
