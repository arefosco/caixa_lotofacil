

from banco_de_dados.banco import dtb
from collections import Counter


class GameHorizontalThreadGroup:

    def __init__(self, db):
        self.database = db
        self.horizontal_codes = self.horizontal_code_all()
        self.countage = self.horizontal_code_count()
        self.countage_array = self.turn_tuple_into_array()
        self.include_percentage()
        self.arrange_data()
        self.good_horizontal_blocks = self.get_data_above_percentage_one()
        # self.print_vars()

    @staticmethod
    def horizontal_code(game_tuple):
        rows = {'1st': 0, '2nd': 0, '3rd': 0, '4th': 0, '5th': 0}

        for number in game_tuple:
            if number in range(1, 6): rows['1st'] += 1
            elif number in range(6, 11): rows['2nd'] += 1
            elif number in range(11, 16): rows['3rd'] += 1
            elif number in range(16, 21): rows['4th'] += 1
            elif number in range(21, 26): rows['5th'] += 1

        game_code_tuple = tuple(rows.values())
        # print(game_code_tuple)
        game_code_str = "".join([str(int_index) for int_index in game_code_tuple])
        return game_code_str

    @staticmethod
    def horizontal_code_v2(game_tuple, reference):
        rows = {'1st': 0, '2nd': 0, '3rd': 0, '4th': 0, '5th': 0}

        for number in game_tuple:
            if number in range(1, 6): rows['1st'] += 1
            elif number in range(6, 11): rows['2nd'] += 1
            elif number in range(11, 16): rows['3rd'] += 1
            elif number in range(16, 21): rows['4th'] += 1
            elif number in range(21, 26): rows['5th'] += 1

        game_code_tuple = tuple(rows.values())
        # print(game_code_tuple)
        game_code_str = "".join([str(int_index) for int_index in game_code_tuple])

        if game_code_str in reference:
            return {'is_proper': True, 'report': f'{game_code_str} [{reference.index(game_code_str)}]'}
        return {'is_proper': False, 'report': f'{game_code_str} [{reference.index(game_code_str)}]'}

    def horizontal_code_all(self):
        box = []
        for tuple_i in self.database:
            box.append(f"{self.horizontal_code(game_tuple=tuple_i)}")
        self.horizontal_codes = box
        return self.horizontal_codes

    def horizontal_code_count(self):
        box = list(Counter(self.horizontal_codes).items())
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
        self.good_horizontal_blocks = box
        return self.good_horizontal_blocks

    def print_vars(self):
        print(f'{self.horizontal_codes = }')
        print(f'{self.countage = }')
        print(f'{self.countage_array = }')
        print(f'O dado abaixo possui: {len(self.good_horizontal_blocks)} índices')
        print(f'{self.good_horizontal_blocks =}')


common_horizontal_thread_groups = GameHorizontalThreadGroup(db=dtb).good_horizontal_blocks

if __name__ == '__main__':
    zero, one, two, three, four, five = 0, 0, 0, 0, 0, 0
    for index in common_horizontal_thread_groups:
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

    print(len(common_horizontal_thread_groups), 'grupos possuem frequência acima/igual 1%, e estão listados abaixo')
    print(common_horizontal_thread_groups)

    print(f"""
        JOGOS COMUNS QUE COMEÇAM COM LINHA 1 ZERADA        || {zero}
        JOGOS COMUNS QUE COMEÇAM COM LINHA 1 COM 1 NÚMERO  || {one}
        JOGOS COMUNS QUE COMEÇAM COM LINHA 1 COM 2 NÚMEROS || {two}
        JOGOS COMUNS QUE COMEÇAM COM LINHA 1 COM 3 NÚMEROS || {three}
        JOGOS COMUNS QUE COMEÇAM COM LINHA 1 COM 4 NÚMEROS || {four}
        JOGOS COMUNS QUE COMEÇAM COM LINHA 1 COM 5 NÚMEROS || {five}""")

    # (3, 4, 1, 5, 2)
    # sample_game = (1, 3, 5, 7, 8, 9, 10, 14, 16, 17, 18, 19, 20, 22, 23)
    # sample_game2 = (7, 8, 10, 11, 12, 14, 15, 16, 17, 18, 20, 21, 22, 23, 25)
    # result = var.horizontal_code(game_tuple=sample_game)
    # result2 = var.horizontal_code(game_tuple=sample_game2)
    # print(result)
    # print(result2)

    _33333 = (1, 2, 3, 6, 9, 10, 12, 13, 14, 17, 18, 19, 21, 24, 25)
    _23334 = (1, 5, 7, 8, 10, 11, 14, 15, 18, 19, 20, 21, 23, 24, 25)
    simulation = GameHorizontalThreadGroup(db=dtb).horizontal_code_v2(
        game_tuple=_33333,
        reference=common_horizontal_thread_groups
    )
    simulation2 = GameHorizontalThreadGroup(db=dtb).horizontal_code_v2(
        game_tuple=_23334,
        reference=common_horizontal_thread_groups
    )
    print(simulation['is_proper'])
    print(simulation['report'])
    print(simulation2['is_proper'])
    print(simulation2['report'])
