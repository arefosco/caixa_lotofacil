

from banco_de_dados.banco import dtb
from collections import Counter


class GameVerticalThreadGroup:
    def __init__(self, db):
        self.database = db
        self.vertical_codes = self.vertical_code_all()
        self.countage = self.vertical_code_count()
        self.countage_array = self.turn_tuple_into_array()
        self.include_percentage()
        self.arrange_data()
        self.good_vertical_blocks = self.get_data_above_percentage_one()
        # self.print_vars()

    @staticmethod
    def vertical_code(game_tuple):
        columns = {
            '1st': {'sequence': [1, 6, 11, 16, 21], 'countage': 0},
            '2nd': {'sequence': [2, 7, 12, 17, 22], 'countage': 0},
            '3rd': {'sequence': [3, 8, 13, 18, 23], 'countage': 0},
            '4th': {'sequence': [4, 9, 14, 19, 24], 'countage': 0},
            '5th': {'sequence': [5, 10, 15, 20, 25], 'countage': 0}
        }

        for number in game_tuple:
            if number in columns['1st']['sequence']:
                columns['1st']['countage'] += 1
            elif number in columns['2nd']['sequence']:
                columns['2nd']['countage'] += 1
            elif number in columns['3rd']['sequence']:
                columns['3rd']['countage'] += 1
            elif number in columns['4th']['sequence']:
                columns['4th']['countage'] += 1
            elif number in columns['5th']['sequence']:
                columns['5th']['countage'] += 1

        game_code_tuple = (
            columns['1st']['countage'], columns['2nd']['countage'], columns['3rd']['countage'],
            columns['4th']['countage'], columns['5th']['countage']
        )

        # print(game_code_tuple)
        game_code_str = "".join([str(int_index) for int_index in game_code_tuple])
        return game_code_str

    def vertical_code_all(self):
        box = []
        for tuple_i in self.database:
            box.append(f"{self.vertical_code(game_tuple=tuple_i)}")
        self.vertical_codes = box
        return self.vertical_codes

    def vertical_code_count(self):
        box = list(Counter(self.vertical_codes).items())
        self.countage = box
        return self.countage

    def turn_tuple_into_array(self):
        box = []
        [box.append(list(index)) for index in self.countage]
        self.countage_array = box
        return self.countage_array

    def include_percentage(self):
        for index in self.countage_array:
            calculus = float(f'{(index[1] * 100) / len(self.database):.2f}')
            index.append(calculus)

    def arrange_data(self):
        self.countage_array = sorted(self.countage_array, key=lambda index: index[2], reverse=True)

    def get_data_above_percentage_one(self):
        box = []
        [box.append(index[0]) if index[2] >= 1 else None for index in self.countage_array]
        self.good_vertical_blocks = box
        return self.good_vertical_blocks

    def print_vars(self):
        print(f'{self.vertical_codes = }')
        print(f'{self.countage = }')
        print(f'{self.countage_array = }')
        print(f'O dado abaixo possui: {len(self.good_vertical_blocks)} índices')
        print(f'{self.good_vertical_blocks = }')


common_vertical_thread_groups = GameVerticalThreadGroup(db=dtb).good_vertical_blocks


if __name__ == '__main__':
    zero, one, two, three, four, five = 0, 0, 0, 0, 0, 0
    for index in common_vertical_thread_groups:
        if index[0] == '0':
            zero += 1
        elif index[0] == '1':
            one += 1
        elif index[0] == '2':
            two += 1
        elif index[0] == '3':
            three += 1
        elif index[0] == '4':
            four += 1
        elif index[0] == '5':
            five += 1

    print(len(common_vertical_thread_groups), 'grupos possuem frequência acima/igual a 1%, e estão listados abaixo')
    print(common_vertical_thread_groups)

    print(f"""
    JOGOS COMUNS QUE COMEÇAM COM COLUNA 1 ZERADA        || {zero}
    JOGOS COMUNS QUE COMEÇAM COM COLUNA 1 COM 1 NÚMERO  || {one}
    JOGOS COMUNS QUE COMEÇAM COM COLUNA 1 COM 2 NÚMEROS || {two}
    JOGOS COMUNS QUE COMEÇAM COM COLUNA 1 COM 3 NÚMEROS || {three}
    JOGOS COMUNS QUE COMEÇAM COM COLUNA 1 COM 4 NÚMEROS || {four}
    JOGOS COMUNS QUE COMEÇAM COM COLUNA 1 COM 5 NÚMEROS || {five}""")

    simulation = GameVerticalThreadGroup(db=dtb)
    # _33342 = (1, 2, 3, 6, 9, 10, 12, 13, 14, 17, 18, 19, 21, 24, 25)
    # sample_1 = GameVerticalThreadGroup(db=dtb).vertical_code(game_tuple=_33342)
    # print(sample_1)
