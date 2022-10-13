

from banco_de_dados.banco import dtb


class Numbers:

    # a_a
    def count_each_starting_number(self):
        # Contar quantos jogos começam: (1 a 4) e (5 p/ cima)
        for game in dtb:
            if game[0] >= 5: self.starts_with[5]['qt'] += 1
            elif game[0] == 4: self.starts_with[4]['qt'] += 1
            elif game[0] == 3: self.starts_with[3]['qt'] += 1
            elif game[0] == 2: self.starts_with[2]['qt'] += 1
            elif game[0] == 1: self.starts_with[1]['qt'] += 1

    # a_b
    def count_each_ending_number(self):
        # Contar quantos jogos terminam: (15, 25)
        for game in dtb:
            if game[-1] == 15: self.finishes_with[15]['qt'] += 1
            if game[-1] == 16: self.finishes_with[16]['qt'] += 1
            if game[-1] == 17: self.finishes_with[17]['qt'] += 1
            if game[-1] == 18: self.finishes_with[18]['qt'] += 1
            if game[-1] == 19: self.finishes_with[19]['qt'] += 1
            if game[-1] == 20: self.finishes_with[20]['qt'] += 1
            if game[-1] == 21: self.finishes_with[21]['qt'] += 1
            if game[-1] == 22: self.finishes_with[22]['qt'] += 1
            if game[-1] == 23: self.finishes_with[23]['qt'] += 1
            if game[-1] == 24: self.finishes_with[24]['qt'] += 1
            if game[-1] == 25: self.finishes_with[25]['qt'] += 1

    # a_c
    def get_absolute_frequency(self, for_):
        pass
        # if for_ == 'start':
        #     self.absolute_freqs['start'] = sum([self.starts_with[key]['qt'] for key in self.starts_with])
        # elif for_ == 'end':
        #     self.absolute_freqs['end'] = sum([self.finishes_with[key]['qt'] for key in self.finishes_with])

    # a_d
    def create_numbers_tuple_report(self, location):
        # (número inicial, frequência dele, porcentagem da frequência) -> (1, 1568, 59.64)
        if location == 'start':
            box = [
                (
                    key,
                    self.starts_with[key]['qt'],
                    # float(f"{(self.starts_with[key]['qt'] * 100) / self.absolute_freqs['start']:.2f}")
                    float(f"{(self.starts_with[key]['qt'] * 100) / self.absolute_frequency:.2f}")
                )
                for key in self.starts_with
            ]

            box_sorted = sorted(box, key=lambda index: index[2], reverse=True)
            self.sorted_rank_starts_with = box_sorted
            return self.sorted_rank_starts_with

        elif location == 'end':
            box = [
                (key, self.finishes_with[key]['qt'],
                 # float(f"{(self.finishes_with[key]['qt'] * 100) / self.absolute_freqs['end']:.2f}"))
                 float(f"{(self.finishes_with[key]['qt'] * 100) / self.absolute_frequency:.2f}"))
                for key in self.finishes_with
            ]

            box_sorted = sorted(box, key=lambda index: index[2], reverse=True)
            self.sorted_rank_finishes_with = box_sorted
            return self.sorted_rank_finishes_with

    # a_f
    def get_most_frequent_numbers(self, place):
        if place == 'start':
            start = []
            [start.append(tuple_[0]) if tuple_[2] > 10 else None for tuple_ in self.sorted_rank_starts_with]
            self.allowed_at_start = start
            return self.allowed_at_start
        else:
            end = []
            [end.append(tuple_[0]) if tuple_[2] > 10 else None for tuple_ in self.sorted_rank_finishes_with]
            self.allowed_at_end = end
            return self.allowed_at_end

    def print_vars(self):
        print(f"{self.starts_with = }")
        print(f"{self.finishes_with = }")
        # print(f"{self.absolute_freqs = }")
        print(f"{self.absolute_frequency = }")
        # print(f"{self.rank_starts_with = }")
        # print(f"{self.rank_finishes_with = }")
        print(f"{self.sorted_rank_starts_with = }")
        print(f"{self.sorted_rank_finishes_with = }")
        print(f"{self.allowed_at_start = }")
        print(f"{self.allowed_at_end = }")

    def __init__(self, db):
        """
        ==================================================== # a_a ====================================================
        . Inicialmente, estas vars possuem todas as chaves vazias, mas elas são incrementadas
        . Temos a frequência dos números iniciais

        self.starts_with = {
            1: {'qt': 1568}, 2: {'qt': 652}, 3: {'qt': 281}, 4: {'qt': 83}, 5: {'qt': 45}
        }

        ==================================================== # a_b ====================================================
        . Inicialmente, estas vars possuem todas as chaves vazias, mas elas são incrementadas
        . Temos a frequência dos números finais

        self.finishes_with = {
            15: {'qt': 0}, 16: {'qt': 0}, 17: {'qt': 0}, 18: {'qt': 1}, 19: {'qt': 4}, 20: {'qt': 8},
            21: {'qt': 34}, 22: {'qt': 78}, 23: {'qt': 251}, 24: {'qt': 630}, 25: {'qt': 1623}
        }

        ==================================================== # a_c ====================================================
        . Precisamos desse valor para pegar valores de porcentagem
        . O tamanho sempre dá o tamanho do banco, pois um número nunca se repete no mesmo jogo
        . Por isso, a função "get_absolute_frequency" foi trocada por "self.absolute_frequency"

        ANTES
        self.absolute_freqs = {'start': 2629, 'end': 2629}

        DEPOIS
        self.absolute_frequency = 2629

        ==================================================== # a_d ====================================================
        . Dos primeiros números e últimos números, já temos a frequência com que eles acontecem
        . Deles, criamos uma tupla com a cópia dos dados + o cálculo de porcentagem (adicionado)
        . Portanto, temos abaixo: (número inicial, frequência, porcentagem da frequência)

        INICIAIS
        self.rank_starts_with = [
            (1, 1568, 59.64), (2, 652, 24.8), (3, 281, 10.69), (4, 83, 3.16), (5, 45, 1.71)
        ]

        FINAIS
        self.rank_finishes_with = [
            (15, 0, 0.0), (16, 0, 0.0), (17, 0, 0.0), (18, 1, 0.04), (19, 4, 0.15), (20, 8, 0.3),
            (21, 34, 1.29), (22, 78, 2.97), (23, 251, 9.55), (24, 630, 23.96), (25, 1623, 61.73)
        ]

        ==================================================== # a_d ====================================================
        . Temos os dados, mas é preciso ordená-los por valor de porcentagem (índice aninhado 2)

        self.sorted_rank_starts_with = [
            (1, 1568, 59.64), (2, 652, 24.8), (3, 281, 10.69), (4, 83, 3.16), (5, 45, 1.71)
        ]

        self.sorted_rank_finishes_with = [
            (25, 1623, 61.73), (24, 630, 23.96), (23, 251, 9.55), (22, 78, 2.97), (21, 34, 1.29),
            (20, 8, 0.3), (19, 4, 0.15), (18, 1, 0.04), (15, 0, 0.0), (16, 0, 0.0), (17, 0, 0.0)
        ]

        ==================================================== # a_e ====================================================
        . Dos dados organizados, tanto dos números iniciais quanto finais serão filtrados
        . O filtro é pelo índice aninhado 0 de cada uma das vars acima com porcentagem acima de 10%
        . A segunda opção foi descartada (passei a achar irrelevante)

        self.allowed_at_start = [1, 2, 3]
        self.allowed_at_end = [25, 24]
        """

        self.database = db

        self.starts_with = {
            1: {'qt': 0}, 2: {'qt': 0}, 3: {'qt': 0}, 4: {'qt': 0}, 5: {'qt': 0}
        }

        self.finishes_with = {
            15: {'qt': 0}, 16: {'qt': 0}, 17: {'qt': 0}, 18: {'qt': 0}, 19: {'qt': 0}, 20: {'qt': 0}, 21: {'qt': 0},
            22: {'qt': 0}, 23: {'qt': 0}, 24: {'qt': 0}, 25: {'qt': 0}
        }

        # self.absolute_freqs = {'start': 0, 'end': 0}

        self.count_each_starting_number()                                                  # a_a
        self.count_each_ending_number()                                                    # a_b
        self.absolute_frequency = len(self.database)                                       # a_c
        self.sorted_rank_starts_with = self.create_numbers_tuple_report(location='start')  # a_d
        self.sorted_rank_finishes_with = self.create_numbers_tuple_report(location='end')  # a_d
        self.allowed_at_start = self.get_most_frequent_numbers(place='start')              # a_e
        self.allowed_at_end = self.get_most_frequent_numbers(place='end')                  # a_e

        # self.get_absolute_frequency(for_='start')           # a_c -> self.absolute_freqs['start']
        # self.get_absolute_frequency(for_='end')             # a_c -> self.absolute_freqs['end']

        "ÚTIL APENAS DURANTE A CONSTRUÇÃO"
        # self.print_vars()


allowed_at_start = Numbers(db=dtb).allowed_at_start
