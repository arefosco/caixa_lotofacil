

from banco_de_dados.banco import dtb
from executavel.exe import CardLoopLess

# Para usar a função "sequence_horizontal" sem recriá-la aqui, vamos instanciar um objeto de classe "CardLoopLess"
obj = CardLoopLess(db=dtb, last_game=dtb[-1])

# Onde os resultados serão inseridos
rank = []

for game in dtb:
    # Como a função da classe precisa de "self.game", é preciso dizer que cada jogo do banco é "self.game"
    obj.game = game
    # Após cada análise, se insere em "rank" o resultado se o jogo possui ou não uma linha em branco
    rank.append(f"{obj.sequence_horizontal()['blank_free']}")

if __name__ == '__main__':
    print('\n=============================================== RELATÓRIO ===============================================')
    absolute_frequence = len(dtb)
    relative_frequence_true = rank.count("True")
    relative_frequence_false = rank.count("False")
    percentage_for_true = f'{(relative_frequence_true * 100) / absolute_frequence:.2f}'
    percentage_for_false = f'{(relative_frequence_false * 100) / absolute_frequence:.2f}'
    print(f'Quantos jogos sem linha vazia? {relative_frequence_true} jogos [{percentage_for_true}%]')
    print(f'Quantos jogos com linha vazia? {relative_frequence_false} jogos [{percentage_for_false}%]')
