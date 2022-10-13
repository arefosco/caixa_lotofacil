

from banco_de_dados.banco import dtb
from executavel.exe import Card

# Para usar a função "avoid_long_sequences" sem recriá-la aqui, vamos instanciar um objeto de classe "Card"
obj = Card()

# Onde os resultados serão inseridos
rank = []

for game in dtb:
    # Como a função da classe precisa de "self.game", é preciso dizer que cada jogo do banco é "self.game"
    obj.game = game
    # Após cada análise, se insere em "rank" o resultado se o jogo possui muitos números seguidos
    rank.append(f"{obj.avoid_long_sequences()['code_str']}")

if __name__ == '__main__':
    print('=============================================== RELATÓRIO ===============================================')
    four, five, six, seven, eight, nine = 0, 0, 0, 0, 0, 0
    row_4, row_5, row_6, row_7, row_8, row_9 = "yyyyy", "yyyyyy", "yyyyyyy", "yyyyyyyy", "yyyyyyyyy", "yyyyyyyyyy"
    for code in rank:
        if row_4 in code: four += 1
        if row_5 in code: five += 1
        if row_6 in code: six += 1
        if row_7 in code: seven += 1
        if row_8 in code: eight += 1
        if row_9 in code: nine += 1
    absolute_frequence = four + five + six + seven + eight + nine
    percentage_for_four = f'{four} jogos [{(four * 100) / absolute_frequence:.2f}%]'
    percentage_for_five = f'{five} jogos [{(five * 100) / absolute_frequence:.2f}%]'
    percentage_for_six = f'{six} jogos [{(six * 100) / absolute_frequence:.2f}%]'
    percentage_for_seven = f'{seven} jogos [{(seven * 100) / absolute_frequence:.2f}%]'
    percentage_for_eight = f'{eight} jogos [{(eight * 100) / absolute_frequence:.2f}%]'
    percentage_for_nine = f'{nine} jogos [{(nine * 100) / absolute_frequence:.2f}%]'
    print(f'Quantas vezes um jogo teve sequência de 4 números seguidos? {percentage_for_four}')
    print(f'Quantas vezes um jogo teve sequência de 5 números seguidos? {percentage_for_five}')
    print(f'Quantas vezes um jogo teve sequência de 6 números seguidos? {percentage_for_six}')
    print(f'Quantas vezes um jogo teve sequência de 7 números seguidos? {percentage_for_seven}')
    print(f'Quantas vezes um jogo teve sequência de 8 números seguidos? {percentage_for_eight}')
    print(f'Quantas vezes um jogo teve sequência de 9 números seguidos? {percentage_for_nine}')
