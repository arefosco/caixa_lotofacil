

from banco_de_dados.banco import dtb
from executavel.exe import Card

# Para usar a função "game_type" sem recriá-la aqui, vamos instanciar um objeto de classe "Card"
obj_ = Card()

# Onde os resultados serão inseridos
rank = []

for game in dtb:
    # Como a função da classe precisa de "self.game", é preciso dizer que cada jogo do banco é "self.game"
    obj_.game = game
    # Após cada análise, se insere em "rank" o resultado se o jogo é dividido de forma correta no volante
    rank.append(f"{obj_.game_type()['type']}")

absolute_frequence = len(dtb)
types = ['5/10', '6/9', '7/8', '8/7', '9/6', '10/5', '11/4', '12/3', '13/2', '14/1', '15/0']

relative_freqs = (
    rank.count('5/10'), rank.count('6/9'), rank.count('7/8'), rank.count('8/7'), rank.count('9/6'),
    rank.count('10/5'), rank.count('11/4'), rank.count('12/3'), rank.count('13/2'), rank.count('14/1'),
    rank.count('15/0')
)

# (tipo do jogo, frequência, porcentagem da frequência, porcentagem em str) EX: ['8/7', '100 jogos', 15.00, 15.00%]
all_data = []
for index, freq in enumerate(relative_freqs):
    all_data.append(
        (types[index],
         f'{freq} jogos',
         float(f'{(freq * 100) / absolute_frequence:.2f}'),
         f"{float(f'{(freq * 100) / absolute_frequence:.2f}')}%")
    )

# Dados organizados pelo valor de porcentagem para serem mostrados abaixo (índice 2 = valor de porcentagem)
rank_organized = sorted(all_data, key=lambda all_data_index: all_data_index[2], reverse=True)

# Separar os 3 tipos de jogos mais frequentes
most_common_game_types = []
[most_common_game_types.append(tuple_index[0]) for tuple_index in rank_organized[0:3]]

if __name__ == '__main__':
    print('=============================================== RELATÓRIO ===============================================')
    print('Rank em porcentagem da qtd. de tipos de jogos mais recorrentes')
    for report in rank_organized:
        print(report)
    print('Os 3 tipos de jogos mais frequentes (outros são desprezados por porcentagem baixa)')
    print(most_common_game_types)
