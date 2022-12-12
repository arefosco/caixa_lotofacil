

from banco_de_dados.banco import dtb
from executavel.exe import CardLoopLess

# Não repetir código (ignorar dados acima da palavra "RELATÓRIO" em destaque)
obj = CardLoopLess(db=dtb, last_game=dtb[-1])

# Onde os resultados serão inseridos
rank = []

# Cada jogo do banco têm sua sequência de linhas verificada
for game in dtb:
    obj.game = game
    rank.append(f"{obj.sequence_horizontal()['blank_free']}")

if __name__ == '__main__':
    print('\n=============================================== RELATÓRIO ===============================================')

    absolute_frequence = len(dtb)

    # Respectivamente: Jogos sem lacuna horizontal, com lacuna horizontal
    relative_frequence_true = rank.count("True")
    relative_frequence_false = rank.count("False")

    percentage_for_true = f'{(relative_frequence_true * 100) / absolute_frequence:.2f}'
    percentage_for_false = f'{(relative_frequence_false * 100) / absolute_frequence:.2f}'

    print(f'Quantos jogos sem linha vazia? {relative_frequence_true} jogos [{percentage_for_true}%]')
    print(f'Quantos jogos com linha vazia? {relative_frequence_false} jogos [{percentage_for_false}%]')
