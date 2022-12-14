

from banco_de_dados.banco import dtb
from collections import Counter


class NumbersHistory:

    def __init__(self, db):
        self.database = db
        self.all_ranks = self.most_common_numbers()
        self.all_ranks_report = self.most_common_numbers_countage()
        self.include_percentage()
        self.arrange_data()
        self.main_numbers_by_position = self.get_data_above_percentage_ten()
        # self.print_vars()

    def most_common_numbers(self):
        # Ex: _1 guardará todos os índices "0" de cada tupla índice de "self.database"..._2 guardará índices "1"...etc
        _1, _2, _3, _4, _5 = [], [], [], [], []
        _6, _7, _8, _9, _10 = [], [], [], [], []
        _11, _12, _13, _14, _15 = [], [], [], [], []

        # Armazenamento, os dados são convertidos p/ string, pois "Counter" só conta dados strings
        for tuple_ in self.database:
            _1.append(str(tuple_[0])), _2.append(str(tuple_[1])), _3.append(str(tuple_[2]))
            _4.append(str(tuple_[3])), _5.append(str(tuple_[4])), _6.append(str(tuple_[5]))
            _7.append(str(tuple_[6])), _8.append(str(tuple_[7])), _9.append(str(tuple_[8]))
            _10.append(str(tuple_[9])), _11.append(str(tuple_[10])), _12.append(str(tuple_[11]))
            _13.append(str(tuple_[12])), _14.append(str(tuple_[13])), _15.append(str(tuple_[14]))

        # Transferência dos dados p/ um dicionário
        self.all_ranks = {
            '1': _1, '2': _2, '3': _3, '4': _4, '5': _5,
            '6': _6, '7': _7, '8': _8, '9': _9, '10': _10,
            '11': _11, '12': _12, '13': _13, '14': _14, '15': _15,
        }
        return self.all_ranks

    def most_common_numbers_countage(self):
        """
        Antes:
            '1st', [('1', 1597), ('2', 671), ('3', 286), ('4', 86), ('5', 37), ('6', 7), ('7', 1)]
        Depois:
            '1st', [['1', 1597], ['2', 671], ['3', 286], ['4', 86], ['5', 37], ['6', 7], ['7', 1]]
        Razão:
            Counter não gera um dado iterável, mas gera uma contagem que pode ser convertida para iterável
            Por isso as chaves abaixo estão em lista
            A conversão p/ lista internamente, se dá pelo fato de ser desejado incluir porcentagens como índice 2
        """

        # Ler documentação da função
        self.all_ranks_report = {
            '1st': [list(index) for index in Counter(self.all_ranks['1']).items()],
            '2nd': [list(index) for index in Counter(self.all_ranks['2']).items()],
            '3rd': [list(index) for index in Counter(self.all_ranks['3']).items()],
            '4th': [list(index) for index in Counter(self.all_ranks['4']).items()],
            '5th': [list(index) for index in Counter(self.all_ranks['5']).items()],
            '6th': [list(index) for index in Counter(self.all_ranks['6']).items()],
            '7th': [list(index) for index in Counter(self.all_ranks['7']).items()],
            '8th': [list(index) for index in Counter(self.all_ranks['8']).items()],
            '9th': [list(index) for index in Counter(self.all_ranks['9']).items()],
            '10th': [list(index) for index in Counter(self.all_ranks['10']).items()],
            '11th': [list(index) for index in Counter(self.all_ranks['11']).items()],
            '12th': [list(index) for index in Counter(self.all_ranks['12']).items()],
            '13th': [list(index) for index in Counter(self.all_ranks['13']).items()],
            '14th': [list(index) for index in Counter(self.all_ranks['14']).items()],
            '15th': [list(index) for index in Counter(self.all_ranks['15']).items()]
        }

        return self.all_ranks_report

    def include_percentage(self):
        """
        No loop 1: todas as chaves são pêgas...['1st']...['2nd']...onde cada chave é "key"
        No loop 2: cada chave possui seu tamanho separado, por isso "range" se faz necessário
        No loop 2: ex -> for index in range(self.ranks_report['1st']), representado logo abaixo
        No loop 2: [['1', 1597], ['2', 671], ['3', 286], ['4', 86], ['5', 37], ['6', 7], ['7', 1]]
        "frequency" usa [key] + [index], onde [key] = ['1st'] e [index] = ['1st'][0]
        "frequency" passa por todos os índices em ['1st']...['1st'][0][1]...['1st'][1][1]...['1st'][2][1]
        "frequency" está pegando cada frequência (índice 1) de cada lista aninhada dentro da lista do exemplo acima
        Com base no valor de "frequency", podemos calcular a porcentagem via "calculus"
        Ao final, cada índice da chave ['1st'] recebe o cálculo
        [
            ['1', 1597, 59.48], ['2', 671, 24.99], ['3', 286, 10.65], ['4', 86, 3.2], ['5', 37, 1.38], ['6', 7, 0.26],
            ['7', 1, 0.04]
        ]
        Só foi usado a chave ['1st'] como exemplo, mas o mesmo procedimento se aplica até a chave ['15th']
        """

        # Ler documentação da função
        for key in self.all_ranks_report.keys():
            for index in range(len(self.all_ranks_report[key])):
                frequency = self.all_ranks_report[key][index][1]
                total_games = len(self.database)
                calculus = float(f'{(frequency * 100) / total_games:.2f}')
                self.all_ranks_report[key][index].append(calculus)

    def arrange_data(self):
        # Pelo índice 2, adicionado pela função anterior, cada chave organiza seus dados pelo maior índice 2
        for key in self.all_ranks_report.keys():
            self.all_ranks_report[key] = sorted(self.all_ranks_report[key], key=lambda index: index[2], reverse=True)

    def get_data_above_percentage_ten(self):
        """
        De todas as chaves (loop 1) e suas listas com listas aninhadas (array), filtramos aquelas com índice aninhado 2
        maiores ou iguais a 10, e o índice 0 é pêgo com base nesse índice 2

        Exemplo simulando a chave ['1st'] :
        [
            ['1', 1597, 59.48], ['2', 671, 24.99], ['3', 286, 10.65], ['4', 86, 3.2], ['5', 37, 1.38], ['6', 7, 0.26],
            ['7', 1, 0.04]
        ]

        Então, dessa chave ['1st'], os seus índices 0 aninhados capturados seriam: '1', '2', '3'
        '4', '5', '6' e '7' ficariam fora, pois seus índices aninhados 2 não alcançam 10+
        """

        _1, _2, _3, _4, _5 = [], [], [], [], []
        _6, _7, _8, _9, _10 = [], [], [], [], []
        _11, _12, _13, _14, _15 = [], [], [], [], []

        # Ler documentação da função
        for key in self.all_ranks_report.keys():
            for array in self.all_ranks_report[key]:
                if array[2] >= 10 and key == '1st': _1.append(int(array[0]))
                if array[2] >= 10 and key == '2nd': _2.append(int(array[0]))
                if array[2] >= 10 and key == '3rd': _3.append(int(array[0]))
                if array[2] >= 10 and key == '4th': _4.append(int(array[0]))
                if array[2] >= 10 and key == '5th': _5.append(int(array[0]))
                if array[2] >= 10 and key == '6th': _6.append(int(array[0]))
                if array[2] >= 10 and key == '7th': _7.append(int(array[0]))
                if array[2] >= 10 and key == '8th': _8.append(int(array[0]))
                if array[2] >= 10 and key == '9th': _9.append(int(array[0]))
                if array[2] >= 10 and key == '10th': _10.append(int(array[0]))
                if array[2] >= 10 and key == '11th': _11.append(int(array[0]))
                if array[2] >= 10 and key == '12th': _12.append(int(array[0]))
                if array[2] >= 10 and key == '13th': _13.append(int(array[0]))
                if array[2] >= 10 and key == '14th': _14.append(int(array[0]))
                if array[2] >= 10 and key == '15th': _15.append(int(array[0]))

        self.main_numbers_by_position = {
            '1st': sorted(_1), '2nd': sorted(_2), '3rd': sorted(_3), '4th': sorted(_4), '5th': sorted(_5),
            '6th': sorted(_6), '7th': sorted(_7), '8th': sorted(_8), '9th': sorted(_9), '10th': sorted(_10),
            '11th': sorted(_11), '12th': sorted(_12), '13th': sorted(_13), '14th': sorted(_14), '15th': sorted(_15)
        }

        return self.main_numbers_by_position

    def print_vars(self):
        # print(f'{self.all_ranks = }')
        for report in self.all_ranks_report.items():
            print(report)
        print(f'{self.main_numbers_by_position = }')


proper_numbers_by_position = NumbersHistory(db=dtb).main_numbers_by_position
# print(proper_numbers_by_position)


class NumbersPatterns:
    def __init__(self, db):
        self.database = db
        self.countage = []

        for index in range(len(self.database)):
            self.countage.append(
                self.mistakes_counter(
                    target_game=self.database[index],
                    reference=proper_numbers_by_position)
            )

        self.mistakes_ranked()
        self.countage = self.turn_tuple_into_array()
        self.include_percentage()
        self.arrange_data()
        self.tolerable_mistakes_amount = self.get_data_above_percentage_ten()

        # self.print_vars()

    @staticmethod
    def mistakes_counter(target_game, reference):
        result = []

        positions = [
            '1st', '2nd', '3rd', '4th', '5th',
            '6th', '7th', '8th', '9th', '10th',
            '11th', '12th', '13th', '14th', '15th'
        ]

        for index in range(len(target_game)):
            if target_game[index] in reference[positions[index]]: result.append(True)
            else: result.append(False)

        mistakes = result.count(False)

        return mistakes

    def mistakes_ranked(self):
        self.countage = list(Counter(self.countage).items())
        return self.countage

    def turn_tuple_into_array(self):
        box = []
        [box.append(list(index)) for index in self.countage]
        return box

    def include_percentage(self):
        for index in self.countage:
            calculus = float(f'{(index[1] * 100) / len(self.database):.2f}')
            index.append(calculus)

    def arrange_data(self):
        self.countage = sorted(self.countage, key=lambda index: index[2], reverse=True)

    def get_data_above_percentage_ten(self):
        box = []
        [box.append(index[0]) if index[2] >= 10 else None for index in self.countage]
        return box

    def print_vars(self):
        print(f'{self.countage = }')
        print(f'{self.tolerable_mistakes_amount = }')


tolerable_mistakes = NumbersPatterns(db=dtb).tolerable_mistakes_amount
# print(tolerable_mistakes)
