

from banco_de_dados.banco import dtb


class GameType:

    @staticmethod
    def get_game_type(game_tuple):
        # Contador da parte 1, contador da parte2, parte 1 do volante, parte 2 do volante
        upper, lower, upper_area, lower_area = 0, 0, tuple(range(1, 16)), tuple(range(16, 26))

        for number in game_tuple:
            if number in upper_area:
                upper += 1
            elif number in lower_area:
                lower += 1

        game_class = f"{upper}/{lower}"

        return game_class

    # a_a
    def get_each_game_type(self):
        box = []
        for tuple_i in self.database: box.append(f"{self.get_game_type(game_tuple=tuple_i)}")
        self.rank = box
        return self.rank

    # a_b
    def count_each_game_type_found(self):
        box = (
            self.rank.count('5/10'), self.rank.count('6/9'), self.rank.count('7/8'), self.rank.count('8/7'),
            self.rank.count('9/6'), self.rank.count('10/5'), self.rank.count('11/4'), self.rank.count('12/3'),
            self.rank.count('13/2'), self.rank.count('14/1'), self.rank.count('15/0')
        )
        self.relative_freqs = box
        return self.relative_freqs

    # a_c
    def make_tuple_of_each_game_type(self):
        box = []
        for index, freq in enumerate(self.relative_freqs):
            box.append(
                (
                    self.types[index],
                    f'{freq} jogos',
                    float(f'{(freq * 100) / self.absolute_freq:.2f}'),
                    f"{float(f'{(freq * 100) / self.absolute_freq:.2f}')}%"
                )
            )
        self.game_type_tuple = box
        return self.game_type_tuple

    # a_d
    def sort_game_types_tuple(self):
        # Organizar dados de cada tupla de tipo de jogo pelo índice 2, referente ao valor de porcentagem
        box = sorted(self.game_type_tuple, key=lambda index_n: index_n[2], reverse=True)
        self.game_types_rank = box
        return self.game_types_rank

    # a_e
    def build_main_game_types_array(self):
        # Anexar a string do tipo de jogo (índice 0 na tupla de tipos de jogos)
        box = []
        [box.append(tuple_index[0]) for tuple_index in self.game_types_rank[0:3]]
        self.game_types = box
        return self.game_types

    def print_vars(self):
        print(f"{self.absolute_freq = }")
        print(f"{self.rank = }")
        print(f"{self.relative_freqs = }")
        print(f"{self.game_type_tuple = }")
        print(f"{self.game_types_rank = }")
        print(f"{self.game_types = }")

    def __init__(self, db):
        """
        ==================================================== # a_a ====================================================
        . Cada jogo da Lotofácil têm seu tipo de jogo capturado
        . Exemplo: "9/6" significa: do 1 ao 15, temos 9 números, e do 16 ao 25, temos 6 números

        self.rank = ['9/6', '10/5', '10/5', '8/7', '9/6', '9/6', '8/7', '8/7', '8/7', '11/4', '8/7', '11/4', ...]

        ==================================================== # a_b ====================================================
        . Contagem de cada tipo
        . Exemplo: 867 aqui é a quantidade de vezes que o tipo de jogo '9/6' foi achado até o momento

        self.relative_freqs = (1, 35, 231, 616, 867, 615, 223, 37, 3, 0, 0)

        ==================================================== # a_c ====================================================
        . Com base nas quantidades de cada tipo adquirida acima, há dados suficientes para criar uma tupla de dados
        . A tupla é: (tipo do jogo, frequência, percentagem, percentagem string)

        self.game_type_tuple = [
            ('5/10', '1 jogos', 0.04, '0.04%'), ('6/9', '35 jogos', 1.33, '1.33%'), ('7/8', '231 jogos', 8.79, '8.79%'),
            ('8/7', '616 jogos', 23.44, '23.44%'), ('9/6', '867 jogos', 32.99, '32.99%'),
            ('10/5', '615 jogos', 23.4, '23.4%'), ('11/4', '223 jogos', 8.49, '8.49%'),
            ('12/3', '37 jogos', 1.41, '1.41%'), ('13/2', '3 jogos', 0.11, '0.11%'),
            ('14/1', '0 jogos', 0.0, '0.0%'), ('15/0', '0 jogos', 0.0, '0.0%')
        ]

        ==================================================== # a_d ====================================================
        . Os dados acima são capturados, mas não estão ordenados. A ordenação acontece pelo índice aninhado 2

        self.game_types_rank = [
            ('9/6', '867 jogos', 32.99, '32.99%'), ('8/7', '616 jogos', 23.44, '23.44%'),
            ('10/5', '615 jogos', 23.4, '23.4%'), ('7/8', '231 jogos', 8.79, '8.79%'),
            ('11/4', '223 jogos', 8.49, '8.49%'), ('12/3', '37 jogos', 1.41, '1.41%'),
            ('6/9', '35 jogos', 1.33, '1.33%'), ('13/2', '3 jogos', 0.11, '0.11%'),
            ('5/10', '1 jogos', 0.04, '0.04%'), ('14/1', '0 jogos', 0.0, '0.0%'),
            ('15/0', '0 jogos', 0.0, '0.0%')
        ]

        ==================================================== # a_e ====================================================
        . Após organizados, pegamos o índice aninhado 1 de cada índice
        . Não foi usado critérios de filtragem por valor de porcentagem
        . Razão? Esses tipos de jogos são a esmagadora maioria, então apenas eles serão selecionados

        self.game_types = ['9/6', '8/7', '10/5']
        """

        self.database = db
        self.absolute_freq = len(self.database)
        self.types = ('5/10', '6/9', '7/8', '8/7', '9/6', '10/5', '11/4', '12/3', '13/2', '14/1', '15/0')
        self.rank = self.get_each_game_type()                       # a_a
        self.relative_freqs = self.count_each_game_type_found()     # a_b
        self.game_type_tuple = self.make_tuple_of_each_game_type()  # a_c
        self.game_types_rank = self.sort_game_types_tuple()         # a_d
        self.game_types = self.build_main_game_types_array()        # a_e

        "ÚTIL APENAS DURANTE A CONSTRUÇÃO"
        # self.print_vars()


game_types = GameType(db=dtb).game_types
