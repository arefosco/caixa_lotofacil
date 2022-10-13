

from banco_de_dados.banco import dtb


class Sequences:

    @staticmethod
    def avoid_long_sequences(game_var, first_index=0, second_index=1):
        # Recebe os cálculos no loop, recebe string dos cálculos
        integer_list, answer = [], []

        while second_index < len(game_var):
            # O cálculo precisa ser 0. Vamos pegar o jogo [1, 2, 3, 5, 7, 8, 10, 11, 14, 16, 17, 19, 21, 24, 25]
            # A lógica é: (2 - 1) (3 - 2) (5 - 3) (7 - 5) e assim por diante até acabar os índices do array
            # Se os números são seguidos, o valor será 1, mas na anexação é subtraído por 1, ou seja, será 0
            # No array que anexa, que é "integer_list", só pode haver 0 até 5 vezes (significa 5 números seguidos)
            integer_list.append((game_var[second_index] - game_var[first_index]) - 1)
            first_index += 1
            second_index += 1

        # Aqui, a cada 0 achado em "integer_list", "answer" recebe uma string "y", não podendo passar de 5
        [answer.append('y') if integer == 0 else answer.append('n') for integer in integer_list]
        # Depois os índices são mesclados em uma string p/ uso nas condições abaixo
        answer_code = "".join(answer)

        return answer_code

    # a_a
    def get_each_game_string_code(self):
        box = []
        for game in self.database: box.append(self.avoid_long_sequences(game))
        self.rank = box
        return self.rank

    # a_b
    def count_each_game_string_code(self):
        for code in self.rank:
            if self.rows[0] in code: self.sequences_in_a_row_report[4]['qt'] += 1
            if self.rows[1] in code: self.sequences_in_a_row_report[5]['qt'] += 1
            if self.rows[2] in code: self.sequences_in_a_row_report[6]['qt'] += 1
            if self.rows[3] in code: self.sequences_in_a_row_report[7]['qt'] += 1
            if self.rows[4] in code: self.sequences_in_a_row_report[8]['qt'] += 1
            if self.rows[5] in code: self.sequences_in_a_row_report[9]['qt'] += 1
            if self.rows[6] in code: self.sequences_in_a_row_report[10]['qt'] += 1
            if self.rows[7] in code: self.sequences_in_a_row_report[11]['qt'] += 1

    # a_c
    def get_each_numbers_in_a_row_countage(self):
        box = []
        for key in self.sequences_in_a_row_report: box.append(self.sequences_in_a_row_report[key]['qt'])
        self.frequences = box
        return self.frequences

    # a_c
    def get_absolute_frequency(self):
        for key in self.sequences_in_a_row_report:
            self.frequences.append(self.sequences_in_a_row_report[key]['qt'])
        self.absolute_freq = sum(self.frequences)

    # a_d
    def make_sequences_tuple_database(self):
        box = []
        for index, freq in enumerate(self.rows):
            # EX: (4, '724 jogos', 55.82, '55.82%')
            target_sequence_amount = self.sequences_keys[index]
            target_sequence_amount_frequency = f'{self.frequences[index]} jogos'
            target_sequence_amount_frequency_math = float(f'{(self.frequences[index] * 100) / self.absolute_freq:.2f}')
            target_sequence_amount_percentage = f"{float(f'{(self.frequences[index] * 100) / self.absolute_freq:.2f}')}%"

            box.append(
                (target_sequence_amount,
                 target_sequence_amount_frequency,
                 target_sequence_amount_frequency_math,
                 target_sequence_amount_percentage
                 )
            )

        box_sorted = sorted(box, key=lambda all_data_index: all_data_index[2], reverse=True)
        self.sequences_tuple = box_sorted
        return self.sequences_tuple

    # a_e
    def set_most_common_sequences(self):
        box = []
        for tuple_index in self.sequences_tuple:
            if tuple_index[2] > 10: box.append(tuple_index[0])
        self.most_common = box
        return self.most_common

    # a_f
    def convert_most_common_sequences(self):
        box = []
        static_function_gap_decrement_necessary = 1
        for number in self.most_common:
            box.append('y' * (number - static_function_gap_decrement_necessary))

        self.most_common_codes = box
        return self.most_common_codes

    # a_g
    def collect_sequences(self, badge):
        if badge == 'good':
            proper_ones = list(set(self.rows).intersection(set(self.most_common_codes)))
            self.proper_ones = proper_ones
            return self.proper_ones
        elif badge == 'bad':
            impropers_ = list(set(self.rows).difference(set(self.most_common_codes)))
            self.impropers = impropers_
            return self.impropers

    def print_vars(self):
        print(f"{self.rank = }")
        print(f"{self.sequences_in_a_row_report = }")
        print(f"{self.absolute_freq = }")
        print(f"{self.sequences_tuple = }")
        print(f"{self.most_common = }")
        print(f"{self.most_common_codes = }")
        print(f"{self.proper_ones = }")
        print(f"{self.impropers = }")

    def __init__(self, db):
        """
        ==================================================== # a_a ====================================================
        . Cada jogo da Lotofácil têm suas sequências de números seguidos coletada
        . Normalmente, é muito comum jogos terem 2 a 3 números seguidos, então analizaremos as quantias acima disso
        . Exemplo: 'ynynyynynnnnyy', o 'nnnn' significa 4 números não são seguidos
        . Exemplo: 'nnyyyyyynnynny', o 'yyyyyy' significa 6 números seguidos

        self.rank = [
            'ynynyynynnnnyy', 'nyyynnyynynyny', 'nnyyyyyynnynny', 'ynynnnynyyynyy', 'ynnynyynynynyy', ...
        ]

        ==================================================== # a_b ====================================================
        . Os dados da var acima são base para contar a frequência dos dados abaixo, usando "self.rows" como referência
        . self.rows = ("yyy", "yyyy", "yyyyy", "yyyyyy", "yyyyyyy", "yyyyyyyy", "yyyyyyyyy", "yyyyyyyyyy")
        . Exemplo:
              for code in self.rank:
                  if self.rows[0] in code: self.sequences_in_a_row_report[4]['qt'] += 1
                  if self.rows[1] in code: self.sequences_in_a_row_report[5]['qt'] += 1
        TRADUÇÃO
        . Se 'yyy' in 'ynynyynynnnnyy': incrementar a quantidade de jogos com 4 números seguidos
        . Se 'yyyy' in 'ynynyynynnnnyy': incrementar a quantidade de jogos com 5 números seguidos
        . E assim suscesivamente, ou seja, todos os jogos são verificados se têm dentre 4 a 11 números seguidos
        . O resultado é a alteração da var existente abaixo

        self.sequences_in_a_row_report = {
            4: {'qt': 2298}, 5: {'qt': 1470}, 6: {'qt': 747}, 7: {'qt': 338}, 8: {'qt': 142},
            9: {'qt': 62}, 10: {'qt': 33}, 11: {'qt': 9}
        }

        ==================================================== # a_c ====================================================
        . Da var acima, pegamos todas as chaves e somamos
        . A valor está acima do tamanho do banco, pois alguns jogos têm mais de 1 sequência de números seguidos

        self.absolute_freq = 5099

        ==================================================== # a_d ====================================================
        . Com a frequência absoluta, há dados suficientes para criar uma tupla de dados de cada quantidade
        . COMPOSIÇÃO: (qtd. de sequências, frequência, porcentagem da freq,, porcentagem da freq. em string)
        . Os dados ainda são organizados pelo índice aninhado 2, mas não muda a ordem
        . MOTIVO? A tendência natural de jogos terem sempre maior probabilidade de virem com menos sequências seguidas
        . PADRÃO: Quanto menos sequências seguidas, maior a probabilidade, então sequências de 2 e 3 são muito comuns
        . PADRÃO: Aqui analisamos a partir de 3 até 11, e o padrão se repete, de acordo com a var abaixo

        self.sequences_tuple = [
            (4, '2298 jogos', 45.07, '45.07%'), (5, '1470 jogos', 28.83, '28.83%'),
            (6, '747 jogos', 14.65, '14.65%'), (7, '338 jogos', 6.63, '6.63%'),
            (8, '142 jogos', 2.78, '2.78%'), (9, '62 jogos', 1.22, '1.22%'),
            (10, '33 jogos', 0.65, '0.65%'), (11, '9 jogos', 0.18, '0.18%')
        ]

        ==================================================== # a_e ====================================================
        . Dos dados acima, são pegos o índice aninhado 0 dos que têm índice aninhado 2 acima de 10
        . Abaixo, temos as sequências de números seguidos mais comuns (além de 2 e 3)

        self.most_common = [4, 5, 6]

        ==================================================== # a_f ====================================================
        . Da var acima, seus valores são convertidos em código, mas temos uma peculiaridade
        . Percebe-se que a quantidade é um dado menor para todas os códigos, ou seja, [4, 5, 6] seria [3, 4, 5]
        . MOTIVO? A função principal possui uma limitação que força retirar 1 caracter, o que corrige o problema

        self.most_common_codes = ['yyy', 'yyyy', 'yyyyy']

        ==================================================== # a_g ====================================================
        . A partir da var acima, esta é comparada com a var com todas as sequência: "self.row"
        . Usando interseção de conjunto, temos o resultado, e usamos a segunda var no algoritmo

        self.proper_ones = ['yyy', 'yyyy', 'yyyyy']
        self.impropers = ['yyyyyyy', 'yyyyyyyyyy', 'yyyyyyyy', 'yyyyyyyyy', 'yyyyyy']
        """

        self.database = db
        self.rows = ("yyy", "yyyy", "yyyyy", "yyyyyy", "yyyyyyy", "yyyyyyyy", "yyyyyyyyy", "yyyyyyyyyy")
        self.sequences_in_a_row_report = {
            4: {'qt': 0}, 5: {'qt': 0}, 6: {'qt': 0}, 7: {'qt': 0}, 8: {'qt': 0}, 9: {'qt': 0}, 10: {'qt': 0},
            11: {'qt': 0}
        }

        self.rank = self.get_each_game_string_code()                        # a_a
        self.count_each_game_string_code()                                  # a_b
        self.frequences = self.get_each_numbers_in_a_row_countage()         # a_c
        self.absolute_freq = sum(self.frequences)                           # a_d
        self.sequences_keys = tuple(self.sequences_in_a_row_report.keys())  # a_d
        self.sequences_tuple = self.make_sequences_tuple_database()         # a_d (principal)
        self.most_common = self.set_most_common_sequences()                 # a_e
        self.most_common_codes = self.convert_most_common_sequences()       # a_f
        self.proper_ones = self.collect_sequences(badge='good')             # a_g
        self.impropers = self.collect_sequences(badge='bad')                # a_g (principal) (p/ algoritmo)

        "ÚTIL APENAS DURANTE A CONSTRUÇÃO"
        # self.print_vars()


impropers = Sequences(db=dtb).impropers
