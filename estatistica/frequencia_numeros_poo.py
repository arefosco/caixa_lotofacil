

from banco_de_dados.banco import dtb
from collections import Counter


class AllNumbers:

    def make_initial_dict(self):
        # a_a: Dados criados e a serem inseridos em "numbers_dict"
        number = 0
        amount = []
        [amount.append(number) for n in range(25)]

        # Criação de um dicionário sem digitar dados manualmente (usando os dados acima) (que serão alterados abaixo)
        numbers_dict_ = {}
        for index in range(len(self.numbers)):
            numbers_dict_[self.numbers[index]] = {'qt': amount[index]}
        self.numbers_dict = numbers_dict_
        return self.numbers_dict

    def count_each_number_frequency(self):
        for index, tuple_ in enumerate(dtb):
            for number in tuple_:
                if number == 1: self.numbers_dict[number]['qt'] += 1
                elif number == 2: self.numbers_dict[number]['qt'] += 1
                elif number == 3: self.numbers_dict[number]['qt'] += 1
                elif number == 4: self.numbers_dict[number]['qt'] += 1
                elif number == 5: self.numbers_dict[number]['qt'] += 1
                elif number == 6: self.numbers_dict[number]['qt'] += 1
                elif number == 7: self.numbers_dict[number]['qt'] += 1
                elif number == 8: self.numbers_dict[number]['qt'] += 1
                elif number == 9: self.numbers_dict[number]['qt'] += 1
                elif number == 10: self.numbers_dict[number]['qt'] += 1
                elif number == 11: self.numbers_dict[number]['qt'] += 1
                elif number == 12: self.numbers_dict[number]['qt'] += 1
                elif number == 13: self.numbers_dict[number]['qt'] += 1
                elif number == 14: self.numbers_dict[number]['qt'] += 1
                elif number == 15: self.numbers_dict[number]['qt'] += 1
                elif number == 16: self.numbers_dict[number]['qt'] += 1
                elif number == 17: self.numbers_dict[number]['qt'] += 1
                elif number == 18: self.numbers_dict[number]['qt'] += 1
                elif number == 19: self.numbers_dict[number]['qt'] += 1
                elif number == 20: self.numbers_dict[number]['qt'] += 1
                elif number == 21: self.numbers_dict[number]['qt'] += 1
                elif number == 22: self.numbers_dict[number]['qt'] += 1
                elif number == 23: self.numbers_dict[number]['qt'] += 1
                elif number == 24: self.numbers_dict[number]['qt'] += 1
                elif number == 25: self.numbers_dict[number]['qt'] += 1

    def convert_number_frequencies_dict_into_arrays(self):
        # [(int, {'qt': int})] organizado por ordem crescente
        box = list(Counter(self.numbers_dict).items())
        # [(int, {'qt': int})] organizado pelo valor da chave ['qt']
        box_sorted = sorted(box, key=lambda the_index: the_index[1]['qt'], reverse=True)
        # [[int, {'qt': int}]] organizado por ['qt']
        box_sorted_each_index_is_array = [list(tuple_) for tuple_ in box_sorted]

        self.sorted_numbers_array = box_sorted_each_index_is_array
        return self.sorted_numbers_array

    def add_frequency_percentage_into_each_array(self):
        for index, data in enumerate(self.sorted_numbers_array):
            # [index] = índice principal    [1] = índice aninhado do índice principal    ['qt'] = valor da chave
            percentage_of_this_index = float(f"{(self.sorted_numbers_array[index][1]['qt'] * 100) / len(dtb):.2f}")
            self.sorted_numbers_array[index].append(percentage_of_this_index)

    def get_most_frequent_numbers(self):
        box = []
        # Os números mais reincidentes são adicionados à "box" (acima de 60%) [2] = porcentagem / [0] = número
        [box.append(tuple_i[0]) if tuple_i[2] > 60 else None for tuple_i in self.sorted_numbers_array]
        self.most_frequent_numbers = box
        return self.most_frequent_numbers

    def get_less_frequent_numbers(self):
        less_frequent = set(self.numbers).difference(set(self.most_frequent_numbers))
        self.less_frequent_numbers = less_frequent
        return tuple(self.less_frequent_numbers)

    def get_percentage(self, percentage):
        percentage_ = None
        the_calculus = (percentage * self.most_frequent_numbers_length) / 100
        # Porque conversão para string? O valor pode vir quebrado, e é preciso um valor inteiro
        # Portanto, após a conversão, o número quebrado é detectado na condição, quando ele têm len() maior que 1
        # Depois se coleta o índice 0, que representa a parcela inteira do número
        result = str(the_calculus)
        if len(result) > 1: percentage_ = int(result[0])

        return percentage_

    def print_vars(self):
        print(f"{self.numbers_dict = }")
        print(f"{self.sorted_numbers_array = }")
        print(f"{self.most_frequent_numbers = }")
        print(f"{self.most_frequent_numbers_length = }")
        print(f"{self.less_frequent_numbers = }")
        print(f"{self.percentages = }")

    def __init__(self, db):
        """
        ==================================================== # a_a ====================================================
        . Como a Lotofácil possui uma quantidade razoável de números, não é desejado fazer um dicionário manual
        . Os 2 arrays são os dados do dicionário {chave: valor}
        . Pelos procedimentos desta função, os dados mesclados se tornam a dicionário abaixo

        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
        amount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        numbers_dict = {
            1: {'qt': 0}, 2: {'qt': 0}, 3: {'qt': 0}, 4: {'qt': 0}, 5: {'qt': 0}, 6: {'qt': 0}, 7: {'qt': 0},
            8: {'qt': 0}, 9: {'qt': 0}, 10: {'qt': 0}, 11: {'qt': 0}, 12: {'qt': 0}, 13: {'qt': 0}, 14: {'qt': 0},
            15: {'qt': 0}, 16: {'qt': 0}, 17: {'qt': 0}, 18: {'qt': 0}, 19: {'qt': 0}, 20: {'qt': 0}, 21: {'qt': 0},
            22: {'qt': 0}, 23: {'qt': 0}, 24: {'qt': 0}, 25: {'qt': 0}
        }

        ==================================================== # a_b ====================================================
        . Por esta função, a var acima recebe em cada uma de suas chaves, a frequência de cada número

        self.numbers_dict = {
            1: {'qt': 1568}, 2: {'qt': 1565}, 3: {'qt': 1592}, 4: {'qt': 1579}, 5: {'qt': 1601},
            6: {'qt': 1531}, 7: {'qt': 1540}, 8: {'qt': 1507}, 9: {'qt': 1571}, 10: {'qt': 1634},
            11: {'qt': 1628}, 12: {'qt': 1574}, 13: {'qt': 1607}, 14: {'qt': 1605}, 15: {'qt': 1558},
            16: {'qt': 1520}, 17: {'qt': 1563}, 18: {'qt': 1572}, 19: {'qt': 1570}, 20: {'qt': 1637},
            21: {'qt': 1560}, 22: {'qt': 1571}, 23: {'qt': 1554}, 24: {'qt': 1605}, 25: {'qt': 1623}
        }

        ==================================================== # a_c ====================================================
        . Uma cópia do dicionário acima é feita para a var abaixo, em formato de array, pois receberá dados

        self.sorted_numbers_tuple = [
            [20, {'qt': 1637}], [10, {'qt': 1634}], [11, {'qt': 1628}], [25, {'qt': 1623}], [13, {'qt': 1607}],
            [14, {'qt': 1605}], [24, {'qt': 1605}], [5, {'qt': 1601}], [3, {'qt': 1592}], [4, {'qt': 1579}],
            [12, {'qt': 1574}], [18, {'qt': 1572}], [9, {'qt': 1571}], [22, {'qt': 1571}], [19, {'qt': 1570}],
            [1, {'qt': 1568}], [2, {'qt': 1565}], [17, {'qt': 1563}], [21, {'qt': 1560}], [15, {'qt': 1558}],
            [23, {'qt': 1554}], [7, {'qt': 1540}], [6, {'qt': 1531}], [16, {'qt': 1520}], [8, {'qt': 1507}]
        ]

        ==================================================== # a_d ====================================================
        . Por esta função, temos a adição do cálculos da porcentagem no índice aninhado 2
        . Além disso, os arrays aninhados são organizados pelo índice aninhado 2
        . O que temos abaixo, são arrays ordenados do mais frequente ao menos

        self.sorted_numbers_array = [
            [20, {'qt': 1637}, 62.27], [10, {'qt': 1634}, 62.15], [11, {'qt': 1628}, 61.92], [25, {'qt': 1623}, 61.73],
            [13, {'qt': 1607}, 61.13], [14, {'qt': 1605}, 61.05], [24, {'qt': 1605}, 61.05], [5, {'qt': 1601}, 60.9],
            [3, {'qt': 1592}, 60.56], [4, {'qt': 1579}, 60.06], [12, {'qt': 1574}, 59.87], [18, {'qt': 1572}, 59.79],
            [9, {'qt': 1571}, 59.76], [22, {'qt': 1571}, 59.76], [19, {'qt': 1570}, 59.72], [1, {'qt': 1568}, 59.64],
            [2, {'qt': 1565}, 59.53], [17, {'qt': 1563}, 59.45], [21, {'qt': 1560}, 59.34], [15, {'qt': 1558}, 59.26],
            [23, {'qt': 1554}, 59.11], [7, {'qt': 1540}, 58.58], [6, {'qt': 1531}, 58.24], [16, {'qt': 1520}, 57.82],
            [8, {'qt': 1507}, 57.32]
        ]

        ==================================================== # a_e ====================================================
        . Do array acima, cada índice é analisado em seu índice aninhado 2, aqueles com valor maior que 60 têm seu
          índice 0 é copiado para a var abaixo

        self.most_frequent_numbers = [20, 10, 11, 25, 13, 14, 24, 5, 3, 4]

        ==================================================== # a_f ====================================================
        . Da quantidade de índices da var acima, que são os números mais reincidentes, um jogo do algoritmo deve ter
          pelo menos 40% e no máximo 70& deles (praticamente impossível vir quase todos ou todos)

        self.percentages = {'40%': 4, '70%': 7}
        """

        self.database = db
        self.numbers = list(range(1, 26))
        self.numbers_dict = self.make_initial_dict()                                    # a_a
        self.count_each_number_frequency()                                              # a_b
        self.sorted_numbers_array = self.convert_number_frequencies_dict_into_arrays()  # a_c
        self.add_frequency_percentage_into_each_array()                                 # a_d
        self.most_frequent_numbers = self.get_most_frequent_numbers()                   # a_e
        self.most_frequent_numbers_length = len(self.most_frequent_numbers)             # a_e
        self.less_frequent_numbers = self.get_less_frequent_numbers()                   # a_e

        # a_f
        self.percentages = {
            '40%': self.get_percentage(percentage=40),
            '70%': self.get_percentage(percentage=70)
        }

        "ÚTIL APENAS DURANTE A CONSTRUÇÃO"
        # self.print_vars()


most_frequent_numbers = AllNumbers(db=dtb).most_frequent_numbers
percentages = AllNumbers(db=dtb).percentages
