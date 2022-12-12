

from banco_de_dados.banco import dtb, ten_last  # a_a
from executavel.exe import CardLoopLess

""" IMPORTANTE
  . Como não há variáveis a serem exportadas daqui, a classe 'Card' pode ser usada aqui
  . A classe é chamada para usar uma função dela que realizará uma consulta aqui
  . Se houvesse um dado a ser exportado para o algoritmo principal, a classe não poderia ser importada para cá
  . Ao invés disso, se cria uma cópia da função da classe para cá
  . Caso contrário, ao tentar importar a variável, haveria 'ImportError'
  . Motivo? A classe está sendo importada aqui, e uma variável seria mandada para onde a classe está 
  . Neste documento, a classe está sendo importada, e a variável está sendo mandada para onde a classe está
  . Tecnicamente, junto com a variável, as importações vão também, e é ai que acontece o erro 
  . Não se importa a classe pro mesmo local onde ela foi criada. Sendo assim, o erro é gerado
"""

# Para usar a função "row_repetition" sem recriá-la aqui, vamos instanciar um objeto de classe "Card"
obj = CardLoopLess(db=dtb, last_game=dtb[-1])

# Onde os resultados serão inseridos
rank = []

# Cada jogo do banco
for game in dtb:
    # Como a função da classe precisa de "self.game", é preciso dizer que cada jogo do banco é "self.game"
    obj.game = game
    # Após cada análise, se insere em "rank" o resultado se o jogo possui linhas repetidas
    rank.append(f"{obj.row_repetition()['empty']}")

# a_b
ten_last_rows_report = [
    rank[-1], rank[-2], rank[-3], rank[-4], rank[-5], rank[-6], rank[-7], rank[-8], rank[-9], rank[-10]
]

if __name__ == '__main__':
    print('=============================================== RELATÓRIO ===============================================')
    absolute_frequence = len(dtb)
    relative_frequence_true = rank.count("True")
    relative_frequence_false = rank.count("False")
    percentage_for_true = f'{(relative_frequence_true * 100) / absolute_frequence:.2f}%'
    percentage_for_false = f'{(relative_frequence_false * 100) / absolute_frequence:.2f}%'
    print(f'Quantos jogos têm linhas todas diferentes? {relative_frequence_true} jogos [{percentage_for_true}]')
    print(f'Quantos jogos têm alguma linha igual?      {relative_frequence_false} jogos [{percentage_for_false}]')

    # a_c: Se o jogo não possuir linhas iguais (True), mostrar que o jogo foi aprovado, caso contrário, mostrar vazio
    print('\nRelatório dos 10 últimos jogos (linhas diferentes)')
    for index, game in enumerate(ten_last):
        print(*[f'[aprovado] {game}' if ten_last_rows_report[index] else '           '])
