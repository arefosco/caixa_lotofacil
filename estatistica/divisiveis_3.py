

from banco_de_dados.banco import dtb
from collections import Counter


class GameMiddleNumbers:

    def __init__(self, db):
        self.database = db
        self.divisible_by_3_all = self.divisible_3()
        self.rank = self.divisible_3_group_count()
        self.rank_array = self.turn_tuple_into_array()
        self.include_percentage()
        self.arrange_data()
        self.good_divisible_by_3_sequences = self.get_data_above_percentage_half_one()
        # self.print_vars()

    def divisible_3(self):
        box = []

        # É preciso 2 loops for, pois cada índice de "self.database" é uma tupla
        # Os divisíveis por 3 são guardados, enquanto os não, são transformados em ponto
        for index in range(len(self.database)):
            for number in self.database[index]:
                if not number % 3:
                    box.append(number)
                if number % 3:
                    box.append('.')
                # Detectar o último índice do array p/ criar um separador entre o fim de cada tupla
                if number == self.database[index][-1]:
                    box.append('/')

        # Tudo é salvo numa string
        # Os não divisíveis são eliminados, ficando apenas os divisíveis e os "/"
        # Pelo "/" separamos cada combinação e temos o resultado dos múltiplos de 3 de cada jogo
        box_str = "".join([str(index) for index in box])
        box_str_filtered = box_str.replace('.', '')
        box_array = box_str_filtered.split('/')

        return box_array

    def divisible_3_group_count(self):
        box = list(Counter(self.divisible_by_3_all).items())
        self.rank = box
        return self.rank

    def turn_tuple_into_array(self):
        box = []
        [box.append(list(index)) for index in self.rank]
        self.rank_array = box
        return self.rank_array

    def include_percentage(self):
        for index in self.rank_array:
            calculus = float(f'{(index[1] * 100) / len(self.database):.2f}')
            index.append(calculus)

    def arrange_data(self):
        self.rank_array = sorted(self.rank_array, key=lambda index: index[2], reverse=True)

    def get_data_above_percentage_half_one(self):
        box = []
        [box.append(index[0]) if index[2] >= 0.5 else None for index in self.rank_array]
        self.good_divisible_by_3_sequences = box
        return self.good_divisible_by_3_sequences

    def print_vars(self):
        print(f'{self.divisible_by_3_all = }')
        print(f'{self.rank = }')
        print(f'{self.rank_array = }')
        print(f'{self.good_divisible_by_3_sequences = }')


most_common_divisible_3_sequences = GameMiddleNumbers(db=dtb).good_divisible_by_3_sequences

var = [3, 6, 9, 12, 15, 18, 24]
# print(var)
var2 = "".join([str(number) for number in var])
# print(var2)
