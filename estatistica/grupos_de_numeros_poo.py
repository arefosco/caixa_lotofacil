

from banco_de_dados.banco import dtb
from collections import Counter


class NumbersGroupsOfThree:
    """
    ====================================================== # a_a ======================================================
    . Cada jogo da Lotofácil têm várias sequências de 3 num mesmo jogo. Aqui temos um exemplo de resultado
    . Cada número aqui significa que o jogo teve essa quantidade de 3 números seguidos
    . Exemplo: Um jogo com números [1, 2, 3, 4, 5] contêm [1, 2, 3] [2, 3, 4] [3, 4, 5] (3 sequências seguidas)

    self.rank = [2, 3, 5, 3, 2, 3, 2, 5, 4, 6, 7, 4, 8, 4, 1, 3, 6, 4, 5, 6, 3, 7, 6, 3, 6, 6, 5, 8, 3, 6, 5, 3, 2, ...]

    ====================================================== # a_b ======================================================
    . Do exemplo acima, é inserido na var abaixo o valor de frequência de cada sequência
    . COMPOSIÇÃO: (Quantidade de sequências de 3, frequência da quantidade)

    box = [
        (2, 211), (3, 435), (5, 600), (4, 628), (6, 413), (7, 177), (8, 73), (1, 59), (10, 4), (9, 19), (0, 8),
        (12, 1), (11, 1)
    ]

    . Depois as tuplas são são convertidas para listas, pois é desejado inserir a frequência de cada sequência

    box_array = [
        [2, 211], [3, 435], [5, 600], [4, 628], [6, 413], [7, 177], [8, 73], [1, 59], [10, 4], [9, 19], [0, 8],
        [12, 1], [11, 1]
    ]

    . Convertendo cada índice p/ array, os percentuais são inseridos em cada índice aninhado 2

    box_array = [
        [2, 211, 8.03], [3, 435, 16.55], [5, 600, 22.82], [4, 628, 23.89], [6, 413, 15.71], [7, 177, 6.73],
        [8, 73, 2.78], [1, 59, 2.24], [10, 4, 0.15], [9, 19, 0.72], [0, 8, 0.3], [12, 1, 0.04], [11, 1, 0.04]
    ]

    . E por último, os dados são organizados pelo índice aninhado 2

    box_array_sorted = [
        [4, 628, 23.89], [5, 600, 22.82], [3, 435, 16.55], [6, 413, 15.71], [2, 211, 8.03], [7, 177, 6.73],
        [8, 73, 2.78], [1, 59, 2.24], [9, 19, 0.72], [0, 8, 0.3], [10, 4, 0.15], [12, 1, 0.04], [11, 1, 0.04]
    ]

    ====================================================== # a_c ======================================================
    . Os arrays aninhados acima são analisados, e os que tiverem índice aninhado 2 acima de 10, são enviados a var
      abaixo pelo seu índice aninhado 0. O resultado é o que se vê abaixo

    self.most_common_sequences_of_3 = [4, 5, 3, 6]
    """

    @staticmethod
    def three_in_a_row_counter(game_var):
        i, i2, i3 = 1, 2, 3
        rows = []
        # É preciso 22 repetições de 3 para alcançar o volante completo (23, 24, 25)
        for n in range(23):
            rows.append([i, i2, i3])
            i += 1
            i2 += 1
            i3 += 1
        # rows = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]...até [23, 24, 25]]

        game_cells = [
            game_var[0:3], game_var[1:4], game_var[2:5], game_var[3:6], game_var[4:7], game_var[5:8], game_var[6:9],
            game_var[7:10], game_var[8:11], game_var[9:12], game_var[10:13], game_var[11:14], game_var[12:15]
        ]

        # [SUPOSIÇÃO] game = tuple(range(1, 16). O que se quer saber?
        # [OBJETIVO] game[0:3] in índice de "rows" ... game[1:4] in índice de "rows" ... etc
        # [RESULTADO] A cada sequência de 3 achada, "three_in_a_row_sequence" incrementa
        three_in_a_row_sequence = 0
        for cell in game_cells:
            if cell in rows:
                three_in_a_row_sequence += 1

        return three_in_a_row_sequence

    # a_a
    def get_sequences_of_3_amount(self):
        box = []
        for game in dtb: box.append(self.three_in_a_row_counter(list(game)))
        self.rank = box
        return self.rank

    # a_b
    def get_sequences_of_3_frequency(self):
        # Lista com tuplas
        box = list(Counter(self.rank).items())

        # Listas com listas (para adicionar um novo dado em cada índice aninhado)
        box_array = [list(tuple_) for tuple_ in box]

        # Adicionar o cálculo de porcentagem em cada índice aninhado
        [box_array[index].append(float(f"{(tuple_[1] * 100) / self.absolute_frequency:.2f}"))
         for index, tuple_ in enumerate(box_array)]

        # Ordenar pela porcentagem inserida
        box_array_sorted = sorted(box_array, key=lambda index: index[2], reverse=True)

        # Resultado final do processo
        self.sequences_of_3 = box_array_sorted
        return self.sequences_of_3

    # a_c
    def get_most_common_sequences_of_3(self):
        box = []
        [box.append(tuple_[0]) for tuple_ in self.sequences_of_3 if tuple_[2] > 10]
        self.most_common_sequences_of_3_amount = box
        return self.most_common_sequences_of_3_amount

    def print_vars(self):
        print(f"{self.rank = }")
        print(f"{self.sequences_of_3 = }")
        print(f"{self.most_common_sequences_of_3_amount = }")

    def __init__(self, db):
        self.database = db
        self.absolute_frequency = len(db)
        self.rank = self.get_sequences_of_3_amount()                                    # a_a
        self.sequences_of_3 = self.get_sequences_of_3_frequency()                       # a_b
        self.most_common_sequences_of_3_amount = self.get_most_common_sequences_of_3()  # a_c

        "ÚTIL APENAS DURANTE A CONSTRUÇÃO"
        # self.print_vars()


most_common_sequences_of_3_amount = NumbersGroupsOfThree(db=dtb).most_common_sequences_of_3_amount
