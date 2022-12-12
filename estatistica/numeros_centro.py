

from banco_de_dados.banco import dtb
from collections import Counter


class GameMiddleNumbers:

    def __init__(self, db):
        self.database = db
        self.middle_numbers_all = self.middle_number()
        self.rank = self.middle_number_count()
        self.rank_array = self.turn_tuple_into_array()
        self.include_percentage()
        self.arrange_data()
        self.good_middle_numbers = self.get_data_above_percentage_ten()
        # self.print_vars()

    def middle_number(self):
        box = []
        for index in self.database:
            box.append(index[7])
        self.middle_numbers_all = box
        return self.middle_numbers_all

    def middle_number_count(self):
        box = list(Counter(self.middle_numbers_all).items())
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

    def get_data_above_percentage_ten(self):
        box = []
        [box.append(index[0]) if index[2] >= 10 else None for index in self.rank_array]
        self.good_middle_numbers = box
        return self.good_middle_numbers

    def print_vars(self):
        print(f'{self.middle_numbers_all = }')
        print(f'{self.rank = }')
        print(f'{self.rank_array = }')
        print(f'{self.good_middle_numbers = }')


good_middle_numbers = GameMiddleNumbers(db=dtb).good_middle_numbers
