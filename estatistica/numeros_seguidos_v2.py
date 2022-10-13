

from banco_de_dados.banco import dtb


def avoid_long_sequences(game_var, first_index=0, second_index=1):
    # Recebe os cálculos no loop, recebe string dos cálculos
    integer_list, answer = [], []

    """ LIMITAÇÃO DA FUNÇÃO
      . Após o uso desta função abaixo, dados dela serão tratados em "proper_sequence_codes"
      . Em "proper_sequence_codes", teremos as qtds. de sequências seguidas + recorrentes (inteiros)
      . O problema dessa função é que os cálculos dela desprezam 1 número achado. Vejamos o exemplo abaixo
      . Esse jogo [1, 2, 3, 4, 5, 6, 7, 9, 12, 13, 14, 17, 18, 20, 23], gera isso: 'yyyyyynnyynynn'
      . Aqui temos 7 números seguidos (mais comuns são 4, 5, 6), mas o código gerado possui "6 y seguidos"
      . Deveria ser "7 y seguidos", então por conta dessa limitação, a correção é feita fora da função
      . sequences_in_row = [4, 5, 6]    gera    proper_sequence_codes = ['yyyy', 'yyyyy', 'yyyyyy']
      . Por conta da limitação da função, é preciso uma adaptação em "proper_sequence_codes"
      . Na construção de "proper_sequence_codes", 1 caractere é reduzido, ficando da seguinte forma
      . sequences_in_row = [4, 5, 6]    gera    proper_sequence_codes = ['yyy', 'yyyy', 'yyyyy']
      . Temos [3, 4, 5], que são, na verdade, [4, 5, 6], por conta da limitação da função
      . Dentre as possibilidades [ 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ], os + comuns são [4, 5, 6]
      . [2, 3, 7, 8, 9, 10, 11, 12, 13, 14, 15] têm porcentagens desprezíveis
      . Cada número do array acima é convertido em 'y' na qtd. de cada número - 1
      . Por isso, os permitidos são ['yyy', 'yyyy', 'yyyyy'] = [4, 5, 6]
    """
    while second_index < len(game_var):
        # O cálculo precisa ser 0. Vamos pegar o jogo [1, 2, 3, 5, 7, 8, 10, 11, 14, 16, 17, 19, 21, 24, 25]
        # A lógica é: (2 - 1) (3 - 2) (5 - 3) (7 - 5) e assim por diante até acabar os índices do array
        # Se os números são seguidos, o valor será 1, mas na anexação é subtraído por 1, ou seja, será 0
        # No array que anexa, que é "integer_list", só pode haver 0 até 5 vezes (significa 5 números seguidos)
        integer_list.append((game_var[second_index] - game_var[first_index]) - 1)
        first_index += 1
        second_index += 1

    # Aqui, a cada 0 achado em "integer_list", "answer" recebe uma string "y", não podendo passar de 5
    [answer.append('y') if integer == 0 else answer.append('n') for integer in integer_list]
    # Depois os índices são mesclados em uma string p/ uso nas condições abaixo
    answer_code = "".join(answer)

    return answer_code


# Onde os resultados serão inseridos
rank = []

# Cada jogo no banco é analizado e seu código string e passado para "rank" para saber a contagem e porcentagem
for game in dtb: rank.append(avoid_long_sequences(game))

# Contadores incrementáveis
four, five, six, seven, eight, nine, ten, eleven = 0, 0, 0, 0, 0, 0, 0, 0

# Dos dados avaliados, serão alvo os de: 4 a 11 números seguidos (1 a menos por conta da limitação da função)
rows = ("yyy", "yyyy", "yyyyy", "yyyyyy", "yyyyyyy", "yyyyyyyy", "yyyyyyyyy", "yyyyyyyyyy")

# (índice 0 da tupla) que representa cada número de repetição contado (4 a 11 repetições)
in_a_row = [*range(4, 12)]

# Registro da contagem nas vars alvo contadoras (com base numa amplitude desejada) (descartas: 2, 3, 12, 13, 14, 15)
for code in rank:
    if rows[0] in code: four += 1
    if rows[1] in code: five += 1
    if rows[2] in code: six += 1
    if rows[3] in code: seven += 1
    if rows[4] in code: eight += 1
    if rows[5] in code: nine += 1
    if rows[6] in code: ten += 1
    if rows[7] in code: eleven += 1

# Contagem das frequências (usado nos índices 1, 2 e 3 da tupla)
freqs = (four, five, six, seven, eight, nine, ten, eleven)
print(f"{freqs = }")

# Dado principal para calcular porcentagem (usado nos índices 2 e 3 da tupla)
absolute_freq = four + five + six + seven + eight + nine + ten + eleven
print(f"{absolute_freq = }")

all_data = []
for index, freq in enumerate(rows):
    # EX: (4, '724 jogos', 55.82, '55.82%')
    all_data.append(
        (in_a_row[index],
         f'{freqs[index]} jogos',
         float(f'{(freqs[index] * 100) / absolute_freq:.2f}'),
         f"{float(f'{(freqs[index] * 100) / absolute_freq:.2f}')}%")
    )

# Dados organizados pelo valor de porcentagem para serem mostrados abaixo (índice 2 = valor de porcentagem)
rank_organized = sorted(all_data, key=lambda all_data_index: all_data_index[2], reverse=True)

# Separar os 3 tipos de jogos mais frequentes
sequences_in_row = []
[sequences_in_row.append(tuple_index[0]) for tuple_index in rank_organized if tuple_index[2] > 10]

# - 1 é preciso, pois há uma limitação na função (que eu não sei corrigir). A correção é feita nas vars abaixo
proper_sequences_codes = []
[proper_sequences_codes.append('y' * (number - 1)) for number in sequences_in_row]

allowed = list(set(rows).intersection(set(proper_sequences_codes)))

"VAR usada em [ avoid_long_sequences ]"
impropers = list(set(rows).difference(set(proper_sequences_codes)))

if __name__ == '__main__':
    print('\nOrdem crescente de frequência de números seguidos')
    for tuple_ in rank_organized:
        print(tuple_)
    print('\n3 frequências de números seguidos mais comuns')
    print(sequences_in_row)
    print('\n3 frequências de números seguidos mais comuns (em código)')
    print(proper_sequences_codes)
    print('\nOutras frequências de números seguidos menos comuns (em código) (usados no algoritmo)')
    print(impropers)

    print('\n================= DADOS RELEVANTES PARA VISUALIZAR O PROBLEMA COM A FUNÇÃO NESTE ARQUIVO =================')
    print(f'{in_a_row = }')
    print(f'{sequences_in_row = }')
    print(f'{proper_sequences_codes = }')
    print(f'{allowed = }')
    print(f'{impropers = } [ PRINCIPAL ]')

    # Testes para ver se as sequências mostram o padrão esperado (se 4 é 'yyy') (se 5 é 'yyyy') ...
    print('\n===== TESTES =====')
    print('4 seguidos', avoid_long_sequences([1, 2, 3, 4, 6, 7, 9, 10, 12, 13, 15, 16, 18, 19, 21]))
    print('5 seguidos', avoid_long_sequences([1, 2, 3, 4, 5, 7, 9, 10, 12, 13, 15, 16, 18, 19, 21]))
    print('6 seguidos', avoid_long_sequences([1, 2, 3, 4, 5, 6, 9, 10, 12, 13, 15, 16, 18, 19, 21]))
    print('7 seguidos', avoid_long_sequences([1, 2, 3, 4, 5, 6, 7, 10, 12, 13, 15, 16, 18, 19, 21]))
