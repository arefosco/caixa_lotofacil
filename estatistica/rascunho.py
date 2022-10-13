

from banco_de_dados.banco import dtb
from collections import Counter


class Detour:
    @staticmethod
    def get_mean(the_game):
        box = []
        for tuple_ in the_game:
            all_number = [number for number in tuple_]
            mean = float(f"{sum(all_number) / len(all_number):.2f}")
            box.append(mean)
        return box

    def get_detour(self):
        box = []
        temporary_box = []
        for index, tuple_ in enumerate(self.database):
            for number in tuple_:
                if number < self.mean[index]:
                    temporary_box.append(float(f"{self.mean[index] - number:.2f}"))
                elif number > self.mean[index]:
                    temporary_box.append(float(f"{number - self.mean[index]:.2f}"))
                if len(temporary_box) == 15:
                    box.append([*temporary_box])
                    temporary_box.clear()
        return box

    def get_variance(self):
        box = []
        for index in range(len(self.database)):
            sum_of_each_number_potency_by_2 = sum([(index_nested ** 2) for index_nested in self.database[index]])
            variance = float(f"{sum_of_each_number_potency_by_2 / len(self.database[index]):.2f}")
            box.append(variance)
        return box

    def get_square_root(self):
        box = []
        for variance in self.variance:
            square_root_calculus = float(f"{variance ** (1/2):.2f}")
            box.append(square_root_calculus)
        return box

    def print_vars(self):
        # print(f"{self.mean}")
        # print(f"{self.detour}")
        # print(f"{self.variance}")
        # print(f"{self.standard_detour = }")
        print(f"{self.rank_draft = }")
        print(f"{self.rank = }")
        print([len(self.rank_ordered)], f"{self.rank_ordered = }")
        print(self.reference)

    def __init__(self, db):
        self.database = db
        self.mean = self.get_mean(the_game=self.database)
        self.detour = self.get_detour()
        self.variance = self.get_variance()
        self.standard_detour = self.get_square_root()

        self.rank_draft = Counter(self.standard_detour)
        self.rank = list(Counter([tuple_ for tuple_ in self.standard_detour]).items())
        self.rank_ordered_bad = [tuple_[0] for tuple_ in self.rank if tuple_[1] < 10]
        # IGUAIS
        self.rank_ordered = [tuple_[0] for tuple_ in self.rank if tuple_[1] > 10]
        self.rank_ordered_set = set(self.rank_ordered)
        # RANGE
        self.reference = {
            'least': min(self.rank_ordered),
            'most': max(self.rank_ordered)
        }

        self.print_vars()


if __name__ == '__main__':
    obj = Detour(db=dtb)
