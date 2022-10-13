

def row_repetition(self):
    row_1, row_2, row_3, row_4, row_5 = [], [], [], [], []
    row_1_bin, row_2_bin, row_3_bin, row_4_bin, row_5_bin = [], [], [], [], []
    group_1 = (None, *range(1, 6))
    group_2 = (None, *range(6, 11))
    group_3 = (None, *range(11, 16))
    group_4 = (None, *range(16, 21))
    group_5 = (None, *range(21, 26))

    for number in self.game:
        if number in [*range(1, 6)]:
            index = group_1.index(number)
            row_1.append(group_1[index])
        if number in [*range(6, 11)]:
            index = group_2.index(number)
            row_2.append(group_2[index])
        if number in [*range(11, 16)]:
            index = group_3.index(number)
            row_3.append(group_3[index])
        if number in [*range(16, 21)]:
            index = group_4.index(number)
            row_4.append(group_4[index])
        if number in [*range(21, 26)]:
            index = group_5.index(number)
            row_5.append(group_5[index])

    for number in group_1:
        if number in row_1: row_1_bin.append(1)
        if number not in row_1 and number is not None: row_1_bin.append(0)

    for number in group_2:
        if number in row_2: row_2_bin.append(1)
        if number not in row_2 and number is not None: row_2_bin.append(0)

    for number in group_3:
        if number in row_3: row_3_bin.append(1)
        if number not in row_3 and number is not None: row_3_bin.append(0)

    for number in group_4:
        if number in row_4: row_4_bin.append(1)
        if number not in row_4 and number is not None: row_4_bin.append(0)

    for number in group_5:
        if number in row_5: row_5_bin.append(1)
        if number not in row_5 and number is not None: row_5_bin.append(0)

    result = [row_1_bin, row_2_bin, row_3_bin, row_4_bin, row_5_bin]
    result_tuple = [tuple(each_list) for each_list in result]
    result = set(result_tuple)

    """
    PADRÃO QUE GERA False
    result = [
        [1, 1, 1, 1, 0] horizontal igual
        [1, 1, 1, 1, 0] horizontal igual
        [1, 0, 1, 0, 1]
        [0, 1, 1, 0, 1]
        [0, 0, 1, 0, 0]
    ]
    -> Após conversão p/ conjunto, se "len" cair p/ < 5, retorna "False"
    """

    # Linhas com padrões de posição todos != [True], se não, [False]
    if len(result) == 5:
        return True
    return False


def column_repetition(self):
    column_1, column_2, column_3, column_4, column_5 = [], [], [], [], []
    column_1_bin, column_2_bin, column_3_bin, column_4_bin, column_5_bin = [], [], [], [], []
    group_1 = (None, 1, 6, 11, 16, 21)
    group_2 = (None, 2, 7, 12, 17, 22)
    group_3 = (None, 3, 8, 13, 18, 23)
    group_4 = (None, 4, 9, 14, 19, 24)
    group_5 = (None, 5, 10, 15, 20, 25)

    for number in self.game:
        if number in group_1:
            index = group_1.index(number)
            column_1.append(group_1[index])
        if number in group_2:
            index = group_2.index(number)
            column_2.append(group_2[index])
        if number in group_3:
            index = group_3.index(number)
            column_3.append(group_3[index])
        if number in group_4:
            index = group_4.index(number)
            column_4.append(group_4[index])
        if number in group_5:
            index = group_5.index(number)
            column_5.append(group_5[index])

    for number in group_1:
        if number in column_1: column_1_bin.append(1)
        if number not in column_1 and number is not None: column_1_bin.append(0)

    for number in group_2:
        if number in column_2: column_2_bin.append(1)
        if number not in column_2 and number is not None: column_2_bin.append(0)

    for number in group_3:
        if number in column_3: column_3_bin.append(1)
        if number not in column_3 and number is not None: column_3_bin.append(0)

    for number in group_4:
        if number in column_4: column_4_bin.append(1)
        if number not in column_4 and number is not None: column_4_bin.append(0)

    for number in group_5:
        if number in column_5: column_5_bin.append(1)
        if number not in column_5 and number is not None: column_5_bin.append(0)

    result = [column_1_bin, column_2_bin, column_3_bin, column_4_bin, column_5_bin]

    for data in result:
        print(data)

    result_tuple = [tuple(each_list) for each_list in result]
    result = set(result_tuple)

    # Colunas com padrões de posição todos != [True], se não, [False]
    if len(result) == 5:
        return True
    return False
