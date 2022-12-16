

def sequence_horizontal(game) -> dict:
    row_1, row_2, row_3, row_4, row_5 = 0, 0, 0, 0, 0

    row_1_numbers = [*range(1, 6)]
    row_2_numbers = [*range(6, 11)]
    row_3_numbers = [*range(11, 16)]
    row_4_numbers = [*range(16, 21)]
    row_5_numbers = [*range(21, 26)]

    # Análise [1]
    for number in game:
        if number in row_1_numbers: row_1 += 1
        elif number in row_2_numbers: row_2 += 1
        elif number in row_3_numbers: row_3 += 1
        elif number in row_4_numbers: row_4 += 1
        elif number in row_5_numbers: row_5 += 1

    game_horizontal = [row_1, row_2, row_3, row_4, row_5]

    if 0 not in game_horizontal:
        return {'ok': True, 'report': game_horizontal, 'report_str': "".join([str(integer) for integer in game_horizontal])}
    return {'ok': False, 'report': game_horizontal, 'report_str': "".join([str(integer) for integer in game_horizontal])}


game_ = (1, 2, 3, 6, 7, 8, 11, 12, 13, 16, 17, 18, 21, 22, 23)
sample = sequence_horizontal(game_)
print(sample['report'])
print(sample['report_str'], type(sample['report_str']))
