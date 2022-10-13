

"""
# a_c
    box = [{2, 3, 4, 5, 7, 8, 9, 11, 12, 15, 17, 19, 20, 24, 25}]
    result = [11, 10, 7, 11, 11, 8, 11, 11, 9, 7]

    -> O loop só para quando o parâmetro em "count" for satisfeito
    -> Portanto, "while result.count(11) < 5", significa que em "result" há 5 jogos com interseção 11 ao jogo em "box"
    -> Os jogos não são vistos, pois apenas len() é coletada, ao invés do conjunto que mostra os números
"""

from banco_de_dados.banco import ten_last


def create_game(length):
    from random import choice
    game_ = set({})
    # Lotofácil possui 25 números
    card = [*range(1, 26)]

    while len(game_) < length:
        game_.add(choice(card))

    return game_


# a_a: Recebe o jogo a ser comparado com os 10 últimos que sairam da loteria (importado acima)
box = []

# a_b: Recebe o resultado da similaridade do jogo em "a_a" com os dez últimos (apenas o número)
result = []

# a_c: Ver docstring com essa hashtag
while result.count(11) < 5:
    "10 JOGOS ALEATÓRIOS"
    # for n in range(10):
    #     box.append(create_game(length=15))

    # for index, game in enumerate(ten_last):
    #     result.append(len(set(game).intersection(set(box[index]))))

    "UM JOGO ALEATÓRIO"
    box.append(create_game(length=15))

    for index, game in enumerate(ten_last):
        result.append(len(set(game).intersection(set(box[0]))))

    # a_d: Enquanto não achar um jogo que satisfaça a condição, recria o jogo e limpa as interseções anteriores
    if result.count(11) != 5:
        box.clear()
        result.clear()
    # else:
        # for index in box:
        #     print(index)
        # print(result)
