

from banco_de_dados.banco import dtb


class PrimeNumbers:

    @staticmethod
    def prime_numbers_counter(game_var):
        prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23]
        prime_numbers_box = []

        for number_ in game_var:
            if number_ in prime_numbers:
                prime_numbers_box.append(number_)

        return len(prime_numbers_box)

    # a_a
    def count_each_game_prime_numbers_amount(self):
        box = []
        for game in self.database: box.append(self.prime_numbers_counter(game))
        self.rank = box
        return self.rank

    def get_absolute_frequency(self):
        pass
        # self.absolute_freq = len(self.database)
        # return self.absolute_freq

    # a_c
    def create_prime_numbers_report(self):
        primes_amount = [*range(10)]  # Qualquer jogo pode ter (0 a 9) números primos possíveis
        all_data = []

        for index, prime in enumerate(primes_amount):
            repetition = primes_amount[index]
            repetition_freq = f'{self.rank.count(prime)} jogos'
            repetition_percentage = float(f'{(self.rank.count(prime) * 100) / self.absolute_freq:.2f}')
            repetition_percentage_str = f"{float(f'{(self.rank.count(prime) * 100) / self.absolute_freq:.2f}')}%"

            all_data.append((repetition, repetition_freq, repetition_percentage, repetition_percentage_str))

        self.prime_numbers_amount_report = sorted(all_data, key=lambda this_index: this_index[2], reverse=True)
        return self.prime_numbers_amount_report

    # a_d
    def get_most_common_amount(self):
        box = []
        for tuple_index in self.prime_numbers_amount_report:
            if tuple_index[2] > 10: box.append(tuple_index[0])
        self.prime_numbers_amount_allowed = box
        return self.prime_numbers_amount_allowed

    # PARTE 2 # a_e
    def get_each_game_prime_number_frequency(self):
        prime_numbers_ = [2, 3, 5, 7, 11, 13, 17, 19, 23]
        for game in self.database:
            for number in game:
                if number in prime_numbers_:
                    if number == 2: self.prime_numbers_dict[2]['qt'] += 1
                    if number == 3: self.prime_numbers_dict[3]['qt'] += 1
                    if number == 5: self.prime_numbers_dict[5]['qt'] += 1
                    if number == 7: self.prime_numbers_dict[7]['qt'] += 1
                    if number == 11: self.prime_numbers_dict[11]['qt'] += 1
                    if number == 13: self.prime_numbers_dict[13]['qt'] += 1
                    if number == 17: self.prime_numbers_dict[17]['qt'] += 1
                    if number == 19: self.prime_numbers_dict[19]['qt'] += 1
                    if number == 23: self.prime_numbers_dict[23]['qt'] += 1

    def create_prime_number_report(self):
        research = []
        for key in self.prime_numbers_dict:
            research.append(
                (
                    key,
                    self.prime_numbers_dict[key]['qt'],
                    float(f"{(self.prime_numbers_dict[key]['qt'] * 100) / self.absolute_freq:.2f}")
                )
            )

        self.prime_numbers_report = sorted(research, key=lambda index_n: index_n[2], reverse=True)
        return self.prime_numbers_report

    def get_most_common_primes(self):
        box = []
        for tuple_index in self.prime_numbers_report:
            if tuple_index[2] > 60: box.append(tuple_index[0])
        self.most_common_primes = box
        return self.most_common_primes

    def print_vars(self):
        print(f"{self.rank = }")
        print(f"{self.absolute_freq = }")
        print(f"{self.prime_numbers_amount_report = }")
        print(f"{self.prime_numbers_amount_allowed = }")
        print(f"{self.prime_numbers_dict = }")
        print(f"{self.prime_numbers_report = }")
        print(f"{self.most_common_primes = }")

    def __init__(self, db):
        """
        ==================================================== # a_a ====================================================
        . Cada jogo da Lotofácil têm uma quantidade de números primos. Temos um exemplo de coletagem abaixo
        . Podemos ter entre 0 a 9 primos em cada jogo, e ao final teremos as taxas mais frequentes

        self.rank = [6, 6, 4, 6, 5, 6, 3, 4, 6, 6, 5, 5, 8, 6, 3, 7, 7, 6, 7, 5, 5, 5, 5, 8, 6, 7, 3, 6, 4, 7, 5, ...]

        ==================================================== # a_b ====================================================
        . O tamanho da frequência é igual ao do banco, pois números primos não se repetem num mesmo jogo

        self.absolute_freq = 2629

        ==================================================== # a_c ====================================================
        . Pela frequência absoluta, podemos calcular quantas vezes cada quantidade de primos veio
        . Isso é feito criando uma tupla com 4 dados
        . COMPOSIÇÃO: (qtd. de repetições de primos, freq., porcentagem da freq., porcentagem da freq. em string)

        self.prime_numbers_report = [
            (0, '0 jogos', 0.0, '0.0%'), (1, '2 jogos', 0.08, '0.08%'), (2, '11 jogos', 0.42, '0.42%'),
            (3, '123 jogos', 4.68, '4.68%'), (4, '446 jogos', 16.96, '16.96%'), (5, '804 jogos', 30.58, '30.58%'),
            (6, '775 jogos', 29.48, '29.48%'), (7, '377 jogos', 14.34, '14.34%'), (8, '85 jogos', 3.23, '3.23%'),
            (9, '6 jogos', 0.23, '0.23%')
        ]

        ==================================================== # a_d ====================================================
        self.prime_numbers_amount_allowed = [5, 6, 4, 7]

        PARTE 2: DESCONTINUADA

        ==================================================== # a_e ====================================================
        self.prime_numbers_dict = {
            2: {'qt': 1565}, 3: {'qt': 1592}, 5: {'qt': 1601}, 7: {'qt': 1540}, 11: {'qt': 1628}, 13: {'qt': 1607},
            17: {'qt': 1563}, 19: {'qt': 1570}, 23: {'qt': 1554}
        }

        ==================================================== # a_f ====================================================
        self.prime_numbers_report = [
            (11, 1628, 61.92), (13, 1607, 61.13), (5, 1601, 60.9), (3, 1592, 60.56), (19, 1570, 59.72),
            (2, 1565, 59.53), (17, 1563, 59.45), (23, 1554, 59.11), (7, 1540, 58.58)
        ]
        """

        self.database = db
        self.rank = self.count_each_game_prime_numbers_amount()                # a_a
        # self.absolute_freq = self.get_absolute_frequency()                   # a_b
        self.absolute_freq = len(self.database)                                # a_b
        self.prime_numbers_amount_report = self.create_prime_numbers_report()  # a_c
        self.prime_numbers_amount_allowed = self.get_most_common_amount()      # a_d

        # PARTE 2 (descontinuada no algoritmo principal)
        self.prime_numbers_dict = {
            2: {'qt': 0}, 3: {'qt': 0}, 5: {'qt': 0}, 7: {'qt': 0}, 11: {'qt': 0}, 13: {'qt': 0}, 17: {'qt': 0},
            19: {'qt': 0}, 23: {'qt': 0}
        }
        self.get_each_game_prime_number_frequency()                    # a_e
        self.prime_numbers_report = self.create_prime_number_report()  # a_f

        # DESCARTADO (motivo: não parece ser relevante)
        self.most_common_primes = self.get_most_common_primes()

        "ÚTIL APENAS DURANTE A CONSTRUÇÃO"
        # self.print_vars()


prime_numbers_amount_allowed = PrimeNumbers(db=dtb).prime_numbers_amount_allowed
most_common_primes = PrimeNumbers(db=dtb).most_common_primes
# print(prime_numbers_amount_allowed)
