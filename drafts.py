

from banco_de_dados.banco import dtb
from collections import Counter

# upper = []
# lower = []
# for index in dtb[0]:
#     if index in range(1, 16):
#         upper.append(index)
#     else:
#         lower.append(index)
# print(lower, sum(lower) / len(lower))
# print(upper, sum(upper) / len(upper))


class GameMeanNumbers:

    def __init__(self, db):
        self.database = db
        self.mean_results = []

        for index in range(len(self.database)):
            self.mean_results.append(self.mean_first_15_all(target_game=self.database[index]))

        self.rank = self.mean_first_15_all_count()
        self.rank_array = self.turn_tuple_into_array()
        self.include_percentage()
        self.arrange_data()
        self.good_mean_sequences = self.get_data_above_percentage_half_one()
        self.print_vars()

    @staticmethod
    def mean_first_15_all(target_game):
        upper = []
        for number in target_game:
            if number in range(1, 16):
                upper.append(number)
        return f'{sum(upper) / len(upper):.1f}'

    def mean_first_15_all_count(self):
        box = list(Counter(self.mean_results).items())
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
        [box.append(index[0]) if index[2] >= 1 else None for index in self.rank_array]
        self.good_mean_sequences = box
        return self.good_mean_sequences

    def print_vars(self):
        # pass
        print(f'{self.mean_results = }')
        print(f'{self.rank = }')
        print(f'{self.rank_array = }')
        print(f'Quantas médias boas foram encontradas? {len(self.good_mean_sequences)}')
        print(f'{self.good_mean_sequences = }')


good_mean_sequences = GameMeanNumbers(db=dtb).good_mean_sequences
