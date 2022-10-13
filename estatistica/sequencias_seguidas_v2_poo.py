

from banco_de_dados.banco import dtb


class OddEvenSequences:

    @staticmethod
    def avoid_large_odd_even_sequence(game_var):
        box = []
        odd, even = 'p', 'i'
        [box.append(odd) if not number % 2 else box.append(even) for number in game_var]

        # A partir de cada jogo verificao, é criado uma variável string somente com letras 'p' e 'i' (par e ímpar)
        box = "".join(box)

        return box

    # a_a
    def get_each_game_odd_even_sequence(self):
        box = []
        for tuple_i in self.database: box.append(self.avoid_large_odd_even_sequence(tuple_i))
        self.rank = box
        return self.rank

    # a_b
    def increment_each_game_odd_even_sequence_found(self):
        for code in self.rank:
            if self.chances[0] in code: self.counters['odd_3']['qt'] += 1
            if self.chances[1] in code: self.counters['odd_4']['qt'] += 1
            if self.chances[2] in code: self.counters['odd_5']['qt'] += 1
            if self.chances[3] in code: self.counters['odd_6']['qt'] += 1
            if self.chances[4] in code: self.counters['odd_7']['qt'] += 1
            if self.chances[5] in code: self.counters['odd_8']['qt'] += 1
            if self.chances[6] in code: self.counters['odd_9']['qt'] += 1
            if self.chances[7] in code: self.counters['odd_10']['qt'] += 1
            if self.chances[8] in code: self.counters['odd_11']['qt'] += 1
            if self.chances[9] in code: self.counters['odd_12']['qt'] += 1

        for code in self.rank:
            if self.chances[10] in code: self.counters['even_3']['qt'] += 1
            if self.chances[11] in code: self.counters['even_4']['qt'] += 1
            if self.chances[12] in code: self.counters['even_5']['qt'] += 1
            if self.chances[13] in code: self.counters['even_6']['qt'] += 1
            if self.chances[14] in code: self.counters['even_7']['qt'] += 1
            if self.chances[15] in code: self.counters['even_8']['qt'] += 1
            if self.chances[16] in code: self.counters['even_9']['qt'] += 1
            if self.chances[17] in code: self.counters['even_10']['qt'] += 1
            if self.chances[18] in code: self.counters['even_11']['qt'] += 1
            if self.chances[19] in code: self.counters['even_12']['qt'] += 1
            if self.chances[20] in code: self.counters['even_13']['qt'] += 1

    # a_c
    def get_absolute_frequency(self):
        box = sum([self.counters[key]['qt'] for key in self.counters])
        self.absolute_freq = box
        return self.absolute_freq

    # a_d
    def make_tuple_database(self):
        # box = [(int, str, int, float, str), ...] -> (3, 'ímpares', 1009, 38.87, '38.87%')
        box = [
            (
                self.counters[key]['id'],
                self.counters[key]['type'],
                self.counters[key]['qt'],
                float(f"{(self.counters[key]['qt'] * 100) / self.absolute_freq:.2f}"),
                f"{float((self.counters[key]['qt'] * 100) / self.absolute_freq):.2f}%",
            ) for key in self.counters
        ]

        self.rank_tuple = box
        return self.rank_tuple

    # a_e
    def sort_tuple_database(self):
        box = sorted(self.rank_tuple, key=lambda index_n: index_n[3], reverse=True)
        self.sorted_rank_tuple = box
        return self.sorted_rank_tuple

    # a_f
    def filter_common_sequences(self, manner, percentage):
        above, below = [], []
        for tuple_i in self.sorted_rank_tuple:
            if tuple_i[3] > percentage: above.append(tuple_i)
            else: below.append(tuple_i)

        if manner == 'above':
            self.sequences_above_10_percent = above
            return self.sequences_above_10_percent
        elif manner == 'below':
            self.sequences_below_10_percent = below
            return self.sequences_below_10_percent

    # a_g
    def convert_sequences_into_code(self, manner):
        best, worst = [], []
        # [1] = classe / [0] = quantidade de repetições
        for tuple_i in self.sequences_above_10_percent:
            if tuple_i[1] == 'ímpares': best.append('i' * tuple_i[0])
            elif tuple_i[1] == 'pares': best.append('p' * tuple_i[0])

        for tuple_i in self.sequences_below_10_percent:
            if tuple_i[1] == 'ímpares': worst.append('i' * tuple_i[0])
            elif tuple_i[1] == 'pares': worst.append('p' * tuple_i[0])

        if manner == 'best':
            self.best_sequences = best
            return self.best_sequences
        elif manner == 'worst':
            self.worst_sequences = worst
            return self.worst_sequences

    def print_vars(self):
        print(f"{self.rank = }")
        print(f"{self.counters = }")
        print(f"{self.absolute_freq = }")
        print(f"{self.rank_tuple = }")
        print(f"{self.sorted_rank_tuple = }")
        print(f"{self.sequences_above_10_percent = }")
        print(f"{self.sequences_below_10_percent = }")
        print(f"{self.best_sequences = }")
        print(f"{self.worst_sequences = }")

    def __init__(self, db):
        """
        ==================================================== # a_a ====================================================
        . Cada jogo da Lotofácil têm sua sequência de pares e ímpares seguidos convertidas em código

        self.rank = [
            'piipipiippppipi', 'ipipiiipiipipip', 'ippipipipppipip', 'ippipppipipiipi', 'ipppiipiipipipi', ...
        ]

        ==================================================== # a_b ====================================================
        . Cada chave ['qt'] recebe incrementos
        . Exemplo: "odd_3" são 3 ímpares, isso quer dizer que é achado dentro do código do jogo: "iii"
        . Ao achar, "odd_3['qt']" é incrementado

        self.counters = {
            'odd_3': {'qt': 913, 'id': 3, 'type': 'pares'}, 'odd_4': {'qt': 240, 'id': 4, 'type': 'pares'},
            'odd_5': {'qt': 43, 'id': 5, 'type': 'pares'}, 'odd_6': {'qt': 9, 'id': 6, 'type': 'pares'},
            'odd_7': {'qt': 1, 'id': 7, 'type': 'pares'}, 'odd_8': {'qt': 0, 'id': 8, 'type': 'pares'},
            'odd_9': {'qt': 0, 'id': 9, 'type': 'pares'}, 'odd_10': {'qt': 0, 'id': 10, 'type': 'pares'},
            'odd_11': {'qt': 0, 'id': 11, 'type': 'pares'}, 'odd_12': {'qt': 0, 'id': 12, 'type': 'pares'},
            'even_3': {'qt': 1009, 'id': 3, 'type': 'ímpares'}, 'even_4': {'qt': 294, 'id': 4, 'type': 'ímpares'},
            'even_5': {'qt': 71, 'id': 5, 'type': 'ímpares'}, 'even_6': {'qt': 12, 'id': 6, 'type': 'ímpares'},
            'even_7': {'qt': 3, 'id': 7, 'type': 'ímpares'}, 'even_8': {'qt': 1, 'id': 8, 'type': 'ímpares'},
            'even_9': {'qt': 0, 'id': 9, 'type': 'ímpares'}, 'even_10': {'qt': 0, 'id': 10, 'type': 'ímpares'},
            'even_11': {'qt': 0, 'id': 11, 'type': 'ímpares'}, 'even_12': {'qt': 0, 'id': 12, 'type': 'ímpares'},
            'even_13': {'qt': 0, 'id': 13, 'type': 'ímpares'}
        }

    ====================================================== # a_c ======================================================
    . Valor necessário para calcular as porcentagens nos índices (3, 4) da tupla "self.rank_ordered"
    . O valor não é o tamanho do banco, pois as sequências de 2 pares e ímpares não são contadas (comuns demais)

    self.absolute_freq = 2596

    ====================================================== # a_d ======================================================
    . É criada uma cópia de "self.counters" em forma de tupla, só que com complementos
    . Como "self.counters" já têm as frequências em ['qt'], podemos por ela, calcular a porcentagem de cada frequência
    . O cálculo é inserido na var abaixo

    self.rank_tuple = [
        (3, 'pares', 913, 35.17, '35.17%'), (4, 'pares', 240, 9.24, '9.24%'), (5, 'pares', 43, 1.66, '1.66%'),
        (6, 'pares', 9, 0.35, '0.35%'), (7, 'pares', 1, 0.04, '0.04%'), (8, 'pares', 0, 0.0, '0.00%'),
        (9, 'pares', 0, 0.0, '0.00%'), (10, 'pares', 0, 0.0, '0.00%'), (11, 'pares', 0, 0.0, '0.00%'),
        (12, 'pares', 0, 0.0, '0.00%'), (3, 'ímpares', 1009, 38.87, '38.87%'),
        (4, 'ímpares', 294, 11.33, '11.33%'), (5, 'ímpares', 71, 2.73, '2.73%'),
        (6, 'ímpares', 12, 0.46, '0.46%'), (7, 'ímpares', 3, 0.12, '0.12%'),
        (8, 'ímpares', 1, 0.04, '0.04%'), (9, 'ímpares', 0, 0.0, '0.00%'), (10, 'ímpares', 0, 0.0, '0.00%'),
        (11, 'ímpares', 0, 0.0, '0.00%'), (12, 'ímpares', 0, 0.0, '0.00%'), (13, 'ímpares', 0, 0.0, '0.00%')
    ]

    ====================================================== # a_e ======================================================
    . Cada índice do array é organizado pelo valor de porcentagem (índice aninhado 3)

    self.sorted_rank_tuple = [
        (3, 'ímpares', 1009, 38.87, '38.87%'), (3, 'pares', 913, 35.17, '35.17%'),
        (4, 'ímpares', 294, 11.33, '11.33%'), (4, 'pares', 240, 9.24, '9.24%'),
        (5, 'ímpares', 71, 2.73, '2.73%'), (5, 'pares', 43, 1.66, '1.66%'),
        (6, 'ímpares', 12, 0.46, '0.46%'), (6, 'pares', 9, 0.35, '0.35%'), (7, 'ímpares', 3, 0.12, '0.12%'),
        (7, 'pares', 1, 0.04, '0.04%'), (8, 'ímpares', 1, 0.04, '0.04%'), (8, 'pares', 0, 0.0, '0.00%'),
        (9, 'pares', 0, 0.0, '0.00%'), (10, 'pares', 0, 0.0, '0.00%'), (11, 'pares', 0, 0.0, '0.00%'),
        (12, 'pares', 0, 0.0, '0.00%'), (9, 'ímpares', 0, 0.0, '0.00%'), (10, 'ímpares', 0, 0.0, '0.00%'),
        (11, 'ímpares', 0, 0.0, '0.00%'), (12, 'ímpares', 0, 0.0, '0.00%'), (13, 'ímpares', 0, 0.0, '0.00%')
    ]

    ====================================================== # a_f ======================================================
    . Com base no índice aninhado 3, filtramos os índices com valor maior que 10
    . Com base no índice aninhado 3, filtramos os índices com valor menor que 10

    self.sequences_above_10_percent = [
        (3, 'ímpares', 1009, 38.87, '38.87%'), (3, 'pares', 913, 35.17, '35.17%'),
        (4, 'ímpares', 294, 11.33, '11.33%')
    ]

    self.sequences_below_10_percent = [
        (4, 'pares', 240, 9.24, '9.24%'), (5, 'ímpares', 71, 2.73, '2.73%'), (5, 'pares', 43, 1.66, '1.66%'),
        (6, 'ímpares', 12, 0.46, '0.46%'), (6, 'pares', 9, 0.35, '0.35%'), (7, 'ímpares', 3, 0.12, '0.12%'),
        (7, 'pares', 1, 0.04, '0.04%'), (8, 'ímpares', 1, 0.04, '0.04%'), (8, 'pares', 0, 0.0, '0.00%'),
        (9, 'pares', 0, 0.0, '0.00%'), (10, 'pares', 0, 0.0, '0.00%'), (11, 'pares', 0, 0.0, '0.00%'),
        (12, 'pares', 0, 0.0, '0.00%'), (9, 'ímpares', 0, 0.0, '0.00%'), (10, 'ímpares', 0, 0.0, '0.00%'),
        (11, 'ímpares', 0, 0.0, '0.00%'), (12, 'ímpares', 0, 0.0, '0.00%'), (13, 'ímpares', 0, 0.0, '0.00%')
    ]

    ====================================================== # a_g ======================================================
    . O que foi feito acima é convertido para formato de código
    . Apenas a variável que carrega as piores sequências (self.worst_sequences) serão levadas ao algoritmo principal

    self.best_sequences = ['iii', 'ppp', 'iiii']

    self.worst_sequences = [
        'pppp', 'iiiii', 'ppppp', 'iiiiii', 'pppppp', 'iiiiiii', 'ppppppp', 'iiiiiiii', 'pppppppp', 'ppppppppp',
        'pppppppppp', 'ppppppppppp', 'pppppppppppp', 'iiiiiiiii', 'iiiiiiiiii', 'iiiiiiiiiii', 'iiiiiiiiiiii',
        'iiiiiiiiiiiii'
    ]
    """

        self.database = db
        self.chances = [
            'ppp', 'pppp', 'ppppp', 'pppppp', 'ppppppp', 'pppppppp', 'ppppppppp', 'pppppppppp', 'ppppppppppp',
            'pppppppppppp', 'iii', 'iiii', 'iiiii', 'iiiiii', 'iiiiiii', 'iiiiiiii', 'iiiiiiiii', 'iiiiiiiiii',
            'iiiiiiiiiii', 'iiiiiiiiiiii', 'iiiiiiiiiiiii'
        ]
        self.counters = {
            'odd_3': {'qt': 0, 'id': 3, 'type': 'pares'}, 'odd_4': {'qt': 0, 'id': 4, 'type': 'pares'},
            'odd_5': {'qt': 0, 'id': 5, 'type': 'pares'}, 'odd_6': {'qt': 0, 'id': 6, 'type': 'pares'},
            'odd_7': {'qt': 0, 'id': 7, 'type': 'pares'}, 'odd_8': {'qt': 0, 'id': 8, 'type': 'pares'},
            'odd_9': {'qt': 0, 'id': 9, 'type': 'pares'}, 'odd_10': {'qt': 0, 'id': 10, 'type': 'pares'},
            'odd_11': {'qt': 0, 'id': 11, 'type': 'pares'}, 'odd_12': {'qt': 0, 'id': 12, 'type': 'pares'},
            'even_3': {'qt': 0, 'id': 3, 'type': 'ímpares'}, 'even_4': {'qt': 0, 'id': 4, 'type': 'ímpares'},
            'even_5': {'qt': 0, 'id': 5, 'type': 'ímpares'}, 'even_6': {'qt': 0, 'id': 6, 'type': 'ímpares'},
            'even_7': {'qt': 0, 'id': 7, 'type': 'ímpares'}, 'even_8': {'qt': 0, 'id': 8, 'type': 'ímpares'},
            'even_9': {'qt': 0, 'id': 9, 'type': 'ímpares'}, 'even_10': {'qt': 0, 'id': 10, 'type': 'ímpares'},
            'even_11': {'qt': 0, 'id': 11, 'type': 'ímpares'}, 'even_12': {'qt': 0, 'id': 12, 'type': 'ímpares'},
            'even_13': {'qt': 0, 'id': 13, 'type': 'ímpares'}
        }
        self.rank = self.get_each_game_odd_even_sequence()                                             # a_a
        self.increment_each_game_odd_even_sequence_found()                                             # a_b
        self.absolute_freq = self.get_absolute_frequency()                                             # a_c
        self.rank_tuple = self.make_tuple_database()                                                   # a_d
        self.sorted_rank_tuple = self.sort_tuple_database()                                            # a_e
        self.sequences_above_10_percent = self.filter_common_sequences(manner='above', percentage=10)  # a_f
        self.sequences_below_10_percent = self.filter_common_sequences(manner='below', percentage=10)  # a_f
        self.best_sequences = self.convert_sequences_into_code(manner='best')                          # a_g
        self.worst_sequences = self.convert_sequences_into_code(manner='worst')                        # a_g

        "ÚTIL APENAS DURANTE A CONSTRUÇÃO"
        # self.print_vars()


worst_sequences = OddEvenSequences(db=dtb).worst_sequences
