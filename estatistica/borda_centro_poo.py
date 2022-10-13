

from banco_de_dados.banco import dtb
from collections import Counter


class BorderOrCenter:
    """
    # Cada borda de cada jogo
        box = [
            [2, 3, 5, 6, 10, 11, 16, 20, 23, 24, 25], [1, 4, 5, 6, 11, 15, 16, 20, 23, 24],
            [1, 4, 6, 10, 11, 16, 20, 23, 24], ...
        ]

    # Cada quantidade de números de borda achados, frequência da quantidade
        box_tuple = [
            [(11, 443), (10, 842), (9, 768), (8, 331), (7, 93), (12, 134), (13, 14), (6, 3), (14, 1)]
        ]

    # Tuplas de "box_tuple" convertidas em array, para adicionar dados extras
        box_array = [
            [11, 443], [10, 842], [9, 768], [8, 331], [7, 93], [12, 134], [13, 14], [6, 3], [14, 1]
        ]

    # Porcentagem adicionada ao índice aninhado 2 de cada índice
        box_array = [
            [11, 443, 16.85], [10, 842, 32.03], [9, 768, 29.21], [8, 331, 12.59], [7, 93, 3.54], [12, 134, 5.1],
            [13, 14, 0.53], [6, 3, 0.11], [14, 1, 0.04]
        ]

    # Organizar pela porcentagem (índice aninhado 2)
        box_array_sorted = [
            [10, 842, 32.03], [9, 768, 29.21], [11, 443, 16.85], [8, 331, 12.59], [12, 134, 5.1], [7, 93, 3.54],
            [13, 14, 0.53], [6, 3, 0.11], [14, 1, 0.04]
        ]

    # Com base em "box_array_sorted" os dados acima 10% são incluídos aos mais frequentes, e abaixo, aos menos
        box_most_frequent_edges = [10, 9, 11, 8]
        box_less_frequent_edges = [12, 7, 13, 6, 14]
    """

    @staticmethod
    def get_border_or_center_size(game_var, site):

        card_edges = []
        card_center = []

        # Todos os números de borda do volante
        for n in list(game_var):
            if n == 1 or n == 2 or n == 3 or n == 4 or n == 5 or \
                    n == 10 or n == 15 or n == 20 or n == 25 or \
                    n == 24 or n == 23 or n == 22 or n == 21 or \
                    n == 16 or n == 11 or n == 6:
                card_edges.append(n)

        # Todos os números de centro do volante
        for n in list(game_var):
            if n == 7 or n == 8 or n == 9 or n == 12 or n == 13 or n == 14 or n == 17 or n == 18 or n == 19:
                card_center.append(n)

        if site == 'edges':
            return card_edges
        elif site == 'center':
            return card_center

    def get_each_game_placement(self, place):
        if place == 'edge':
            box = []
            for tuple_ in dtb: box.append(self.get_border_or_center_size(game_var=tuple_, site='edges'))
            # print(box)

            box_tuple = list(Counter([len(tuple_) for tuple_ in box]).items())
            # print(box_tuple)

            box_array = [list(tuple_) for tuple_ in box_tuple]
            # print(box_array)

            for index, data in enumerate(box_array):
                percentage = float(f"{(box_array[index][1] * 100) / len(dtb):.2f}")
                box_array[index].append(percentage)
            # print(box_array)

            box_array_sorted = sorted(box_array, key=lambda this_index: this_index[2], reverse=True)
            # print(box_array_sorted)

            box_most_frequent_edges = []
            box_less_frequent_edges = []

            [box_most_frequent_edges.append(tuple_i[0]) if tuple_i[2] > 10 else box_less_frequent_edges.append(tuple_i[0])
             for tuple_i in box_array_sorted]
            # print(box_most_frequent_edges)
            # print(box_less_frequent_edges)

            self.most_common_edges_amount = box_most_frequent_edges
            self.less_common_edges_amount = box_less_frequent_edges
            return {
                'common': self.most_common_edges_amount,
                'uncommon': self.less_common_edges_amount
            }

        elif place == 'center':
            box = []
            for tuple_ in dtb: box.append(self.get_border_or_center_size(game_var=tuple_, site='center'))
            # print(box)

            box_tuple = list(Counter([len(tuple_) for tuple_ in box]).items())
            # print(box_tuple)

            box_array = [list(tuple_) for tuple_ in box_tuple]
            # print(box_array)

            for index, data in enumerate(box_array):
                percentage = float(f"{(box_array[index][1] * 100) / len(dtb):.2f}")
                box_array[index].append(percentage)
            # print(box_array)

            box_array_sorted = sorted(box_array, key=lambda this_index: this_index[2], reverse=True)
            # print(box_array_sorted)

            box_most_frequent_centers = []
            box_less_frequent_centers = []

            [box_most_frequent_centers.append(tuple_i[0]) if tuple_i[2] > 10 else box_less_frequent_centers.append(
                tuple_i[0])
             for tuple_i in box_array_sorted]
            # print(box_most_frequent_edges)
            # print(box_less_frequent_edges)

            self.most_common_centers_amount = box_most_frequent_centers
            self.less_common_centers_amount = box_less_frequent_centers
            return {
                'common': self.most_common_centers_amount,
                'uncommon': self.less_common_centers_amount
            }

    def print_vars(self):
        print(f"{self.most_common_edges_amount}")
        print(f"{self.less_common_edges_amount}")
        print(f"{self.most_common_centers_amount}")
        print(f"{self.less_common_centers_amount}")

    def __init__(self, db):
        self.database = db
        self.edges = []
        self.centers = []

        self.most_common_edges_amount = self.get_each_game_placement(place='edge')['common']
        self.less_common_edges_amount = self.get_each_game_placement(place='edge')['uncommon']
        self.most_common_centers_amount = self.get_each_game_placement(place='center')['common']
        self.less_common_centers_amount = self.get_each_game_placement(place='center')['uncommon']

        "ÚTIL APENAS DURANTE A CONSTRUÇÃO"
        # self.print_vars()


most_frequent_edges = BorderOrCenter(db=dtb).most_common_edges_amount
most_frequent_centers = BorderOrCenter(db=dtb).most_common_centers_amount
