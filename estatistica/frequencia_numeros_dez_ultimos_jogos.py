

from banco_de_dados.banco import dtb


class LastNumbers:
    def __init__(self, db):
        self.database = db
        self.ten_last = self.ten_last_game_numbers()
        self.countage = self.count_each_number_frequency()
        self.numbers_group = self.split_by_frequency_rank()
        self.bigger_group = self.filter_biggest_array()
        self.reference_percentage = self.setup_percentage_variable()
        # self.print_vars()

    def ten_last_game_numbers(self):
        db_ten_last_games = [
            *self.database[-1], *self.database[-2], *self.database[-3], *self.database[-4], *self.database[-5],
            *self.database[-6], *self.database[-7], *self.database[-8], *self.database[-9], *self.database[-10]
        ]
        self.ten_last = db_ten_last_games
        return self.ten_last

    def count_each_number_frequency(self):
        countage_report = {}
        for index in range(25):
            index = index + 1
            countage_report[index] = self.ten_last.count(index)
        self.countage = countage_report
        # Dicionário de dicionários {número: frequência de repetições}
        return self.countage

    def split_by_frequency_rank(self):
        until_3 = []
        until_5 = []
        until_7 = []
        above_7 = []

        # É criada uma tupla das chaves [dict_[0]] e valores [dict_[1]]
        for dict_ in self.countage.items():
            if dict_[1] <= 3: until_3.append(dict_[0])
            if 3 < dict_[1] <= 5: until_5.append(dict_[0])
            if 5 < dict_[1] <= 7: until_7.append(dict_[0])
            if 7 < dict_[1] < 10: above_7.append(dict_[0])

        main_box = [until_3, until_5, until_7, above_7]
        self.numbers_group = main_box
        return self.numbers_group

    def filter_biggest_array(self):
        """
        self.numbers_group = [
            [1, 3],
            [5, 14, 15, 17, 18, 19, 21, 23, 25],
            [2, 6, 7, 9, 12, 13, 20, 24],
            [4, 8, 10, 11, 16, 22]
        ]

        bigger_group = [2, 9, 8, 6]                             (qtd. de índices de cada array acima)
        main_index = 9                                          (índice de maior valor)
        target_index = 1                                        (índice do índice de maior valor)
        self.bigger_group = [5, 14, 15, 17, 18, 19, 21, 23, 25] (maior array dentro de "bigger_group")
        """

        bigger_group = [len(array) for array in self.numbers_group]
        main_index = max(bigger_group)
        target_index = bigger_group.index(main_index)
        self.bigger_group = self.numbers_group[target_index]
        return self.bigger_group

    def setup_percentage_variable(self):
        percentages = {
            '40%': int(str((40 * len(self.bigger_group)) / 100)[0]),
            '70%': int(str((70 * len(self.bigger_group)) / 100)[0])
        }

        self.reference_percentage = percentages
        return self.reference_percentage

    def print_vars(self):
        print(f'{self.ten_last = }')
        print(f'{self.countage = }')
        print(f'{self.numbers_group = }')
        print(f'{self.bigger_group = }')
        print(f'{self.reference_percentage = }')


ten_last_games_most_frequent_numbers = LastNumbers(db=dtb).reference_percentage
