

"""
# o_a:
    O método é estático, pois "target_game" é preciso para criar separado: [self.game, self.last_game]
    Caso contrário, precisaria criar um método separado para os 2

# p_a:
    É muito comum os dados do último jogo serem diferentes do próximo (mas não é impossível virem iguais)
    "self.comparisons" guardará todas as comparações que forem consideradas cabíveis entre o jogo cridao e o último
"""

# from estatistica.primeiros_numeros import allowed_at_start
from estatistica.primeiros_numeros_poo import allowed_at_start

# from estatistica.sequencias_seguidas_v2 import worst_sequences
from estatistica.sequencias_seguidas_v2_poo import worst_sequences

# from estatistica.numeros_seguidos_v2 import impropers
from estatistica.numeros_seguidos_v2_poo import impropers  # h_a

# from estatistica.tipo_de_jogo_v2 import game_types
from estatistica.tipo_de_jogo_v2_poo import game_types  # i_a

# from estatistica.contar_numeros_primos_v2 import primes
from estatistica.contar_numeros_primos_v2_poo import (prime_numbers_amount_allowed, most_common_primes)  # j_a

# from estatistica.frequencia_numeros import (most_frequent, percentages)
from estatistica.frequencia_numeros_poo import (most_frequent_numbers, percentages)

# from estatistica.grupos_de_numeros import three_in_a_row_common
from estatistica.grupos_de_numeros_poo import most_common_sequences_of_3_amount

# from estatistica.borda_centro import (most_frequent_edges, most_frequent_centers)
from estatistica.borda_centro_poo import (most_frequent_edges, most_frequent_centers)

from estatistica.grupos_horizontais_poo import common_horizontal_thread_groups

from estatistica.grupos_verticais_poo import common_vertical_thread_groups

from estatistica.numeros_centro import good_middle_numbers

from banco_de_dados.banco import dtb, ten_last
from funcoes.banco_de_dados import ink


class CardLoopLess:

    attempts = 0
    storage = []

    # a_a
    def create_game(self, length: int):
        from random import choice

        self.game = set({})

        # Lotofácil possui 25 números
        card = [*range(1, 26)]

        while len(self.game) < length:
            self.game.add(choice(card))

        return list(self.game)

    # b_a
    def sequence_horizontal(self) -> dict:
        """
        Mais informações || consultas/espaco_horizontal_branco.py
        Teste            || testes.py/test_sequence_horizontal
        """

        row_1, row_2, row_3, row_4, row_5 = 0, 0, 0, 0, 0

        # Cada linha do volante em ordem crescente
        row_1_numbers = [*range(1, 6)]
        row_2_numbers = [*range(6, 11)]
        row_3_numbers = [*range(11, 16)]
        row_4_numbers = [*range(16, 21)]
        row_5_numbers = [*range(21, 26)]

        # Estou ciente de que as ações deveriam estar nas linhas abaixo, mas é desejado economizar linhas
        for number in self.game:
            if number in row_1_numbers: row_1 += 1
            elif number in row_2_numbers: row_2 += 1
            elif number in row_3_numbers: row_3 += 1
            elif number in row_4_numbers: row_4 += 1
            elif number in row_5_numbers: row_5 += 1

        game_horizontal = [row_1, row_2, row_3, row_4, row_5]

        if 0 not in game_horizontal:
            return {'ok': True, 'report': game_horizontal}
        return {'ok': False, 'report': game_horizontal}

    # c_a
    def sequence_vertical(self) -> dict:
        """
        Mais informações || consultas/espaco_vertical_branco.py
        Teste            || testes.py/test_sequence_vertical
        """

        column_1, column_2, column_3, column_4, column_5 = 0, 0, 0, 0, 0

        column_1_numbers = [1, 6, 11, 16, 21]
        column_2_numbers = [2, 7, 12, 17, 22]
        column_3_numbers = [3, 8, 13, 18, 23]
        column_4_numbers = [4, 9, 14, 19, 24]
        column_5_numbers = [5, 10, 15, 20, 25]

        # Estou ciente de que as ações deveriam estar nas linhas abaixo, mas é desejado economizar linhas
        for number in self.game:
            if number in column_1_numbers: column_1 += 1
            elif number in column_2_numbers: column_2 += 1
            elif number in column_3_numbers: column_3 += 1
            elif number in column_4_numbers: column_4 += 1
            elif number in column_5_numbers: column_5 += 1

        game_vertical = [column_1, column_2, column_3, column_4, column_5]

        if 0 not in game_vertical:
            return {'ok': True, 'report': game_vertical}
        return {'ok': False, 'report': game_vertical}

    # d_a
    def proper_gap(self, reference) -> dict:
        """
        Mais informações || estatistica/primeiros_numeros_poo.py (executar)
        Teste            || testes.py/test_proper_gap
        """

        # Não pode anexar "False", "overflow_gap_3" e "overflow_gap_4"
        result = []
        # Não é importante, mas é útil para ver as subtrações feitas no tratamento 2
        calculus = []

        "TRATAMENTO 1 (trocado pelo parâmetro 'reference')"
        # # Primeiro número do volante é pelo menos 5, indica uma lacuna grande e incomum (descartável)
        # if self.game[0] >= 5: result.append(False)
        # # Jogo iniciando com 4 ou menos é aprovável (pois a lacuna é de 3)
        # if self.game[0] <= 4: result.append(True)
        # # Se o último número do volante for entre 16 a 21, há várias lacunas maiores do que 3 (descartável)
        # if self.game[-1] in range(16, 22): result.append(False)

        "TRATAMENTO 2 (evitar lacunas maiores que 5)"
        index_first = 0
        index_second = 1

        # Índices do jogos são subtraídos entre si (posterior - anterior) e o resultado não deve exceder 5
        while index_second < len(self.game):
            calculus.append(self.game[index_second] - self.game[index_first])
            # Se a subtração for maior que 5: jogo reprovado (lacuna muito grande)
            if self.game[index_second] - self.game[index_first] > 5:
                result.append(False)

            index_first += 1
            index_second += 1

        "TERCEIRO TRATAMENTO (evitar + do que uma lacuna grande de cada tipo)"
        # calculus_str = [math_ for math_ in calculus]
        gap_of_3_amount = calculus.count(4)
        gap_of_4_amount = calculus.count(5)

        # O jogo pode ter: 1 lacuna de 3, nenhuma de 4, caso contrário, "result" recebe dados que reprovam o jogo
        if gap_of_3_amount > 1:
            result.append('overflow_gap_3')
        if gap_of_4_amount != 0:
            result.append('overflow_gap_4')

        "TRATAMENTO 4 (dados do jogo devem estar em 'references')"

        "REMOVIDOS (últimas condições de cada condição abaixo)"
        # Motivo? Mudança de ideia na questão de achar relevante
        # or self.game[-1] not in references[1]
        # and self.game[-1] in references[1]

        # O jogo reprovado têm: algum "False" em "result" ou (+ de 1 lacuna de 3) ou (+ de 1 lacuna de 4)
        if False in result \
           or 'overflow_gap_3' in result \
           or 'overflow_gap_4' in result \
           or self.game[0] not in reference:
            return {'ok': False, 'report': calculus, 'data': result}

        # Jogo aceitável: (máx de 1 lacuna de 3 ou nenhuma)
        if False not in result \
           and 'overflow_gap_3' not in result \
           and 'overflow_gap_4' not in result \
           and self.game[0] in reference:
            return {'ok': True, 'report': calculus, 'data': result}

    # e_a
    def avoid_large_odd_even_sequence(self, reference) -> dict:
        """
        Mais informações || estatistica/sequencias_seguidas_v2_poo.py (executar)
        Teste            || testes/test_avoid_large_odd_even_sequence
        """

        box = []

        # Um jogo analizado "self.game" têm seus números pares convertidos em 'p' e ímpares em 'i'
        odd, even = 'p', 'i'

        "Substituído por [ reference ]"
        # odd_flood_4, odd_flood_5, odd_flood_6, odd_flood_7 = 'pppp', 'ppppp', 'pppppp', 'ppppppp'
        # even_flood_4, even_flood_5, even_flood_6, even_flood_7 = 'iiii', 'iiiii', 'iiiiii', 'iiiiiii'

        [box.append(odd) if not number % 2 else box.append(even) for number in self.game]

        # A partir do jogo, é criada uma variável string somente com letras 'p' e 'i'
        game_string = "".join(box)

        must_have_false_only = []

        "Código antigo"
        # Qual a razão disso? evitar muitos "if" e "not" seguidos numa linha (sintaxe fica bagunçada)
        # conditions = {
        #     1: proper_data.append(True) if odd_flood_4 not in box else proper_data.append(False),
        #     2: proper_data.append(True) if odd_flood_5 not in box else proper_data.append(False),
        #     3: proper_data.append(True) if odd_flood_6 not in box else proper_data.append(False),
        #     4: proper_data.append(True) if odd_flood_7 not in box else proper_data.append(False),
        #     5: proper_data.append(True) if even_flood_4 not in box else proper_data.append(False),
        #     6: proper_data.append(True) if even_flood_5 not in box else proper_data.append(False),
        #     7: proper_data.append(True) if even_flood_6 not in box else proper_data.append(False),
        #     8: proper_data.append(True) if even_flood_7 not in box else proper_data.append(False),
        # }

        "Código antigo"
        # Não havendo quaisquer sequências de 4, 5, 6, 7 pares ou ímpares seguidos, o jogo é aprovado
        # if False not in proper_data:
        #     return {'is_proper': True, 'game_string': box, 'result': proper_data}
        # Caso contrário, é reprovado
        # return {'is_proper': False, 'game_string': box, 'result': proper_data}

        for code in reference: must_have_false_only.append(code in game_string)

        if True in must_have_false_only:
            return {'ok': False, 'report': game_string, 'proof': must_have_false_only}
        return {'ok': True, 'report': game_string, 'proof': must_have_false_only}

    # f_a
    def row_repetition(self) -> dict:
        """
        Mais informações: consultas/linhas_repetidas.py (executar)
        """

        # 2 arrays, [15 índices 1] e [10 índices 0] (Volante têm 25 números, 15 são escolhidos e 10 ficam de fora)
        array_of_ones = []
        arrays_of_zeros = []

        # Para não digitar 0 e 1 manualmente, eles são inseridos via "list comprehension"
        [array_of_ones.append(1) for n in range(15)]
        [arrays_of_zeros.append(0) for n in range(10)]

        # ones_to_receive_1 = 15 números que terão 1    ones_to_receive_zero = 10 números que terão 0
        all_numbers = set(range(1, 26))
        ones_to_receive_1 = set(self.game)
        ones_to_receive_zero = all_numbers.difference(ones_to_receive_1)

        "O que está sendo feito?"
        # Se "self.game", possui, por exemplo: (1, 2, 3), ones_inside_game = [(1, 1), (2, 1), (3, 1)]
        # Se "self.game", não possui, por exemplo: (4, 5, 6), ones_outside_game = [(4, 0), (5, 0), (6, 0)]
        ones_inside_game = list(zip(self.game, array_of_ones))
        ones_outside_game = list(zip(ones_to_receive_zero, arrays_of_zeros))

        # Depois de organizar separadamente quem é 0 e quem é 1, todos os números podem ser juntados num mesmo array
        for outsider in ones_outside_game:
            ones_inside_game.append(outsider)

        "O que está sendo feito?"
        # O índice 0 de cada tupla é o número do volante, vamos arrumar o array na ordem crescente
        # [(4, 0), (5, 0), (6, 0), (1, 1), (2, 1), (3, 1)] se torna [(1, 1), (2, 1), (3, 1), (4, 0), (5, 0), (6, 0)]
        tuples_ordered = sorted(ones_inside_game, key=lambda index_1st: index_1st[0])

        "O que está sendo feito?"
        # Sabendo quem é zero e quem é 1 e estando organizados, é coletado o índice 1 de cada tupla (seus binários)
        # Usando os exemplos acima: [1, 2, 3, 4, 5] se torna [1, 1, 1, 0, 0]
        # binary_result = array com 25 índices 0 ou 1
        binary_result = [index[1] for index in tuples_ordered]

        # "binary_result" é quebrado em 5 grupos de 5 índices
        binary_group_1 = "".join([str(index) for index in binary_result[0:5]])
        binary_group_2 = "".join([str(index) for index in binary_result[5:10]])
        binary_group_3 = "".join([str(index) for index in binary_result[10:15]])
        binary_group_4 = "".join([str(index) for index in binary_result[15:20]])
        binary_group_5 = "".join([str(index) for index in binary_result[20:25]])

        "O que está sendo feito?"
        # Os 5 grupos são colocados num array, convertido p/ conjunto
        # Qual o motivo da conversão? Se sabe que conjunto não aceita dados repetidos
        # Havendo arrays repetidos, evidencia que algum grupo se repetiu, então a falha é detectada
        row_code = [binary_group_1, binary_group_2, binary_group_3, binary_group_4, binary_group_5]
        row_code_as_set = set(row_code)

        # O conjunto manteve seu tamanho original (não há linhas repetidas) / alguma linha se repetiu
        if len(row_code_as_set) == 5:
            return {'ok': True, 'set': row_code_as_set, 'report': len(row_code_as_set)}
        return {'ok': False, 'set': row_code_as_set, 'report': len(row_code_as_set)}

    # g_a
    def column_repetition(self) -> dict:
        """
        Mais informações: consultas/colunas_repetidas.py (executar)
        """

        # 2 arrays, [15 índices 1] e [10 índices 0] (Volante têm 25 números, 15 são escolhidos e 10 ficam de fora)
        array_of_ones = []
        arrays_of_zeros = []

        # Para não digitar 0 e 1 manualmente, eles são inseridos via "list comprehension"
        [array_of_ones.append(1) for n in range(15)]
        [arrays_of_zeros.append(0) for n in range(10)]

        # ones_to_receive_1 = 15 números que terão 1    ones_to_receive_zero = 10 números que terão 0
        all_numbers = set(range(1, 26))
        ones_to_receive_1 = set(self.game)
        ones_to_receive_zero = all_numbers.difference(ones_to_receive_1)

        "O que está sendo feito?"
        # Se "self.game", possui, por exemplo: (1, 6, 11), ones_inside_game = [(1, 1), (6, 1), (11, 1)]
        # Se "self.game", não possui, por exemplo: (2, 7, 12), ones_outside_game = [(2, 0), (7, 0), (12, 0)]
        ones_inside_game = list(zip(self.game, array_of_ones))
        ones_outside_game = list(zip(ones_to_receive_zero, arrays_of_zeros))

        # Depois de organizar separadamente quem é 0 e quem é 1, todos os números podem ser juntados num mesmo array
        for tuple_element in ones_outside_game:
            ones_inside_game.append(tuple_element)

        "O que está sendo feito?"
        # O índice 0 de cada tupla é o número do volante, vamos arrumar o array na ordem crescente
        # [(2, 0), (7, 0), (12, 0), (1, 1), (6, 1), (11, 1)] se torna [(1, 1), (2, 0), (6, 1), (7, 0), (11, 1), (12, 0)]
        tuples_ordered = sorted(ones_inside_game, key=lambda index_1st: index_1st[0])

        # O nome da variável foi modificada apenas p/ caber na linha abaixo
        x = tuples_ordered

        "O que está sendo feito?"
        # A variável "x" têm 25 índices, 15 são (int, 1), 10 são (int, 0), ela será quebrada em grupos de 5
        # Colunas: [1, 6, 11, 16, 21] [2, 7, 12, 17, 22] [3, 8, 13, 18, 23] [4, 9, 14, 19, 24] [5, 10, 15, 20, 25]
        # Os valores são -1 em relação aos abaixo, pois python usa índices começando com 0
        # Temos índices aninhados, pois não é desejado o índice 0, apenas o 1 (binários)
        # Conversão para tupla mandatória, pois conjunto não aceita array como dado
        binary_group_1 = tuple([x[0][1], x[5][1], x[10][1], x[15][1], x[20][1]])
        binary_group_2 = tuple([x[1][1], x[6][1], x[11][1], x[16][1], x[21][1]])
        binary_group_3 = tuple([x[2][1], x[7][1], x[12][1], x[17][1], x[22][1]])
        binary_group_4 = tuple([x[3][1], x[8][1], x[13][1], x[18][1], x[23][1]])
        binary_group_5 = tuple([x[4][1], x[9][1], x[14][1], x[19][1], x[24][1]])

        # Para não ficar código repetido
        del tuples_ordered

        "O que está sendo feito?"
        # Os 5 grupos são colocados num array, convertido p/ conjunto
        # Qual o motivo da conversão? Se sabe que conjunto não aceita dados repetidos
        # Havendo arrays repetidos, evidencia que algum grupo se repetiu, então a falha é detectada
        row_code = [binary_group_1, binary_group_2, binary_group_3, binary_group_4, binary_group_5]
        row_code_as_set = set(row_code)

        # O conjunto manteve seu tamanho original (não há colunas repetidas) / alguma linha se repetiu
        if len(row_code_as_set) == 5:
            return {'ok': True, 'set': row_code_as_set, 'report': len(row_code_as_set)}
        return {'ok': False, 'set': row_code_as_set, 'report': len(row_code_as_set)}

    # h_a
    def avoid_long_sequences(self, reference: list, first_index=0, second_index=1) -> dict:
        """
        Mais informações || consultas/numeros_seguidos.py (executar)
        Teste            || testes.py/test_avoid_long_sequences
        """

        # Recebe os cálculos no loop [índice 2 - índice 1, índice 3 - índice 2...]
        integer_list = []

        # Após todos os cálculos acima (todos inteiros), estes são convertidos p/ strings: 'y', 'n'
        answer = []

        "Substituído pelo parâmetro [ reference ]"
        # in_row_7, in_row_8, in_row_9 = 'yyyyyy', 'yyyyyyy', 'yyyyyyyy'

        while second_index < len(self.game):
            # O cálculo precisa ser 0. Vamos pegar o jogo [1, 2, 3, 5, 7, 8, 10, 11, 14, 16, 17, 19, 21, 24, 25]
            # A lógica é: (2 - 1) (3 - 2) (5 - 3) (7 - 5) e assim por diante até acabar os índices do array
            # Se os números são seguidos, o valor será 1, mas na anexação é subtraído por 1, ou seja, será 0
            # No array que anexa, que é "integer_list", só pode haver 0 até 5 vezes (significa 5 números seguidos)
            integer_list.append((self.game[second_index] - self.game[first_index]) - 1)
            first_index += 1
            second_index += 1

        # Aqui, a cada 0 achado em "integer_list", "answer" recebe uma string "y", não podendo passar de 5
        [answer.append('y') if integer == 0 else answer.append('n') for integer in integer_list]

        # Depois os índices são mesclados em uma string p/ uso nas condições abaixo
        answer_code = "".join(answer)

        "Código antigo (substituído)"
        # Se for achado entre 6 a 8 números seguidos, o jogo é reprovado (+ números seguidos é praticamente impossível)
        # if in_row_7 in answer_code or in_row_8 in answer_code or in_row_9 in answer_code:
        #     return {'is_proper': False, 'calculus': integer_list, 'code': answer, 'code_str': answer_code}
        # Até 5 valores seguidos (aceitável)
        # return {'is_proper': True, 'calculus': integer_list, 'code': answer, 'code_str': answer_code}

        "O que está sendo feito?"
        # "answer_code" é o código string resultante de "self.game"
        # Esse código é comparado entre os códigos vindos de "reference"
        # Se ele for achado, "report" recebe "False", o que indica um problema no jogo
        report = []
        for code in reference:
            if code not in answer_code: report.append(True)
            else: report.append(False)

        # "reference" contém os padrões menos comuns (ruins)
        if False in report:
            return {'ok': False, 'calculus': integer_list, 'report': answer_code, 'proof': report}
        return {'ok': True, 'calculus': integer_list, 'report': answer_code, 'proof': report}

    # i_a
    def game_type(self, reference) -> dict:
        """
        Mais informações || consultas/tipo_de_jogo_v2_poo.py
        Teste            || testes.py/test_game_type
        """

        # Contador da parte 1, contador da parte2, parte 1 do volante, parte 2 do volante
        upper, lower, upper_area, lower_area = 0, 0, tuple(range(1, 16)), tuple(range(16, 26))

        # Iteração sob cada número do jogo, se for entre 1 até 15: [upper += 1], se for entre 16 a 25: [lower += 1]
        for number in self.game:
            if number in upper_area:
                upper += 1
            elif number in lower_area:
                lower += 1

        # String do jogo "self.game"
        game_class = f"{upper}/{lower}"

        "Substituído por [core_var]"
        # De acordo com "consultas/tipo_de_jogo.py" esses tipos são os mais recorrentes
        # right = ['8/7', '9/6', '10/5']

        # String do jogo deve estar em "reference" (tipos de jogos com frequência acima de 10%)
        if game_class in reference:
            return {'ok': True, 'report': game_class}
        return {'ok': False, 'report': game_class}

    # j_a
    def prime_numbers_counter(self, references) -> dict:
        """
        Mais informações || estatistica/contar_numeros_primos_v2_poo.py
        Teste            || testes.py/test_prime_numbers_counter
        """

        prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23]
        prime_numbers_box = []

        "Substituída por [primes]"
        # De acordo com "consultas/contar_numeros_primos.py" a qtd. de números primos mais comuns: [4, 5, 6, 7]
        # proper_amounts = range(4, 8)

        ""
        # O que for achado em "self.game" de número primo é inserido em "prime_numbers_box"
        for number in self.game:
            if number in prime_numbers:
                prime_numbers_box.append(number)

        "Removido"
        # # Dos 3 primos mais recorrentes, pelo menos 1 deles deve estar no jogo
        # one_is_true = []
        # [one_is_true.append(True) if number in references[1] else one_is_true.append(False) for number in self.game]

        "Removido"
        # if len(prime_numbers_box) in references[0] and one_is_true.count(True) >= 1:

        "Removido (junto com a continuação da condição: and has_one_most_common)"
        # must_have_true = []
        # has_one_most_common = ''
        # for number in references[1]:
        #     must_have_true.append(number in self.game)
        # if True in must_have_true: has_one_most_common = True

        ""
        # A quantidade de números primos encontrados está entre as quantidades mais recorrentes
        array_size = len(prime_numbers_box)
        if len(prime_numbers_box) in references[0]:
            return {'ok': True, 'report': f'{prime_numbers_box} [ {array_size} número(s) ]'}
        return {'ok': False, 'report': f'{prime_numbers_box} [ {array_size} número(s) ]'}

    # k_a
    def score_admin(self, single_score, score, has_comparison=False, operator='equals', repeated=0) -> [int, str]:
        """
        :param single_score:   Se apenas uma pontuação será verificada em "scores"
        :param score:          Qual o valor/chave procurado em "scores"
        :param has_comparison: Informar que "score" será comparado a "repeated"
        :param operator:       Operador de comparação
        :param repeated:       Valor a ser comparado (valor máximo de repetição)

        Mais informações || consultas/pontuacao.py
        Teste            || testes/test_score_admin
        """

        # Recebe o resultado (inteiro) da qtd. de similaridades de "self.game" com cada jogo de "self.database"
        similarities = []

        ""
        # Os jogos em "self.database" são tuplas, p/ saber a interseção é preciso conversão p/ conjunto
        # "similarity_target_game_vs_db_game" = inteiro que representa a similaridade (inserido em "similarities")
        for i in range(len(self.database)):
            game_main_as_set = set(self.game)
            game_comparared_as_set = set(self.database[i])
            similarity_target_game_vs_db_game = len(game_main_as_set.intersection(game_comparared_as_set))
            similarities.append(similarity_target_game_vs_db_game)

        # Cada qtd. é contada e se torna um índice aqui (de 6 até 15)
        precisions = [
            similarities.count(6), similarities.count(7), similarities.count(8), similarities.count(9),
            similarities.count(10), similarities.count(11), similarities.count(12), similarities.count(13),
            similarities.count(14), similarities.count(15)
        ]

        # As qtds. são separadas e organizadas neste painel
        score_panel = f"""
        Jogo analisado: {self.game}
        ========== PONTUAÇÃO GLOBAL ==========
        6  pontos || {precisions[0]} vezes
        7  pontos || {precisions[1]} vezes
        8  pontos || {precisions[2]} vezes
        9  pontos || {precisions[3]} vezes
        10 pontos || {precisions[4]} vezes
        11 pontos || {precisions[5]} vezes
        12 pontos || {precisions[6]} vezes
        13 pontos || {precisions[7]} vezes
        14 pontos || {precisions[8]} vezes
        15 pontos || {precisions[9]} vezes"""

        # Quando for desejado saber um dos pontos (entre 6 a 15) (via "score")
        if single_score:
            # Cada pontuação
            scores = {
                6: precisions[0], 7: precisions[1], 8: precisions[2], 9: precisions[3], 10: precisions[4],
                11: precisions[5], 12: precisions[6], 13: precisions[7], 14: precisions[8], 15: precisions[9],
            }

            ""
            # Supondo que se queira saber se "self.game" já fez 13 pontos, então, "score" deve ser 13
            # Seguindo a lógica, "scores" vai até a chave "13" e busca seu valor, passando a "box_with_score"
            # box_with_score[0] = inteiro de quantas vezes a similaridade 13 foi encontrada
            box_with_score = []
            [box_with_score.append(scores[key]) for key in scores if score == key]

            score_found = box_with_score[0]
            correct = {'ok': True, 'banner': score_panel, 'report': score_found}
            incorrect = {'ok': False, 'banner': score_panel, 'report': score_found}

            ""
            # Filtrar quantas vezes uma similaridade aconteceu
            # Supondo que se queira saber se a similaridade 13 se repetiu uma vez
            # Então: score=13 & repeated=1 & operator='equals'
            # (has_comparison, operator, repeated) (quer comparação, comparador, pontuação)
            if has_comparison and operator == 'equals':
                if box_with_score[0] == repeated:
                    return correct
                return incorrect
            if has_comparison and operator == 'greater':
                if box_with_score[0] >= repeated:
                    return correct
                return incorrect
            if has_comparison and operator == 'lesser':
                if box_with_score[0] <= repeated:
                    return correct
                return incorrect

            if not has_comparison:
                return box_with_score[0]

        else:
            return score_panel

    # l_a
    def numbers_frequency(self, references) -> dict:
        """
        Mais informações || estatistica/frequencia_numeros_poo.py
        Teste            || testes/test_numbers_frequency
        """

        ""
        # "references[0]" remete aos números que possuem frequência acima de 60% do total de jogos
        # O tamanho de "references[0]" muda conforme novos jogos vão sendo lançados, pois as porcentagens mudam
        # "self.game" é comparado com "references[0]"
        # Objetivo: saber quantos números de "self.game" estão entre os que vêm acima de 60%
        # Ao saber a qtd., ela é atribuida a "similarity_amount"

        similarity = set(self.game).intersection(set(references[0]))
        similarity_amount = len(similarity)

        ""
        # Apesar de haver muitos números com frequência acima de 60%, obviamente todos não virão
        # Foi especulado algo entre 40% a 70%, que é uma margem lógica aceitável
        # Com base no tamanho do array "references[0]", "references[1]" pode ter seus valores alterados
        # Exemplo: quando esta função foi feita, "len(references[0]) = 10"
        # Com base nisso [40% de 10 = 4] e [70% de 10 = 7], então "similarity_amount" deve estar entre esses valores
        # Caso não esteja, o jogo é considerado problemático
        # Conforme "len(references[0])" muda, "len(references[1])" pode mudar
        if references[1]['40%'] <= similarity_amount <= references[1]['70%']:
            return {'ok': True, 'report': similarity}
        return {'ok': False, 'report': similarity}

    # m_a
    def ten_last_comparison(self, reference) -> dict:
        """
        Mais informações || não possui
        Teste            || testes_test_ten_last_comparison
        """

        # Sequências de interseções ruins (muitos seguidas) & sua confirmação
        bad_codes = ['888', '8888', '88888', '999', '9999', '99999', '101010', '10101010', '1010101010']
        exceeding_patterns = []

        # Sequências de interseções improváveis (muito lineares/padronizadas) & sua confirmação
        bad_combinations = [
            '891011', '111098', '8910', '91011', '11109', '1098',
            '8989', '810810', '811811',
            '9898', '910910', '911911',
            '108108', '109109', '10111011',
            '118118', '119119', '11101110',
        ]
        stupid_patterns = []

        # O valor dessa var muda e invalida o jogo, caso "self.game" possua + do que 2 similaridades de 11
        too_similar = False

        # "self.game" é comparado com os 10 últimos jogos lançados, p/ saber sua similaridade em relação a eles
        # "result" = 10 índices inteiros resultantes das similaridades de "self.game" com os outros 10 jogos
        result = []
        for index, game in enumerate(reference):
            result.append(len(set(game).intersection(set(self.game))))

        # Representação em string do resultado de todas as similaridades (ex: [6, 10, 11, 8] = 610118)
        intersection_code = "".join([str(index) for index in result])

        # Se "else" for satisfeita, o jogo é considerado problemático
        for code in bad_codes:
            if code not in intersection_code:
                exceeding_patterns.append(False)
            else:
                exceeding_patterns.append(True)

        # Interseções em ordem crescente ou decrescente são algo sem lógica (muito improvável)
        for code in bad_combinations:
            if code not in intersection_code:
                stupid_patterns.append(False)
            else:
                stupid_patterns.append(True)

        # Condição satisfeita: jogo invalidado
        if result.count(11) > 2: too_similar = True

        # Todas as condições em "conditions" devem ser "True", ou seja, não deve haver "False" anexado a "box"
        box = []
        before_last_game = result[-2]
        last_game = result[-1]
        very_similar_range = range(11, 16)
        very_different_range = 7
        "INTERPRETAÇÕES"
        # 1: Similaridades de 5 a 7 ausentes (muito distantes)
        # 2: Similaridades de 13 a 15 ausentes (muito próximas)
        # 3: Similaridades de 8 a 11 presentes (muitos comuns)
        # 4: Similaridade de "self.game" em relação ao último jogo deve estar entre 8 a 10
        # 5: A similaridades dos dois últimos jogos devem ser diferentes
        # 6: As similaridades não se repetem muitas vezes seguidas (não mais do que 2)
        # 7: Não há sequências crescentes e decrescentes de interseções
        # 8: Não há mais do que duas similaridades de 11 entre "self.game" e os 10 últimos jogos
        conditions = {
            1: box.append(True) if 5 not in result and 6 not in result and 7 not in result else box.append(False),
            2: box.append(
                True) if 12 not in result and 13 not in result and 14 not in result and 15 not in result else box.append(
                False),
            3: box.append(True) if 8 in result and 9 in result and 10 in result and 11 in result else box.append(False),
            4: box.append(
                True) if last_game not in very_similar_range and last_game != very_different_range else box.append(
                False),
            5: box.append(True) if last_game != before_last_game else box.append(False),
            6: box.append(True) if True not in exceeding_patterns else box.append(False),
            7: box.append(True) if True not in stupid_patterns else box.append(False),
            8: box.append(True) if not too_similar else box.append(False)
        }

        if False not in box:
            return {'ok': True, 'report': f'{result} -> {intersection_code}'}
        return {'ok': False, 'report': f'{result} -> {intersection_code}'}

    # n_a
    def three_in_a_row_counter(self, reference) -> dict:
        """
        Mais informações || estatistica/grupos_de_numeros_poo.py (Executar)
        Teste            || testes/test_three_in_a_row_counter
        """

        # Um array com as 23 combinações de 3 números seguidos: [1, 2, 3] [2, 3, 4] até [23, 24, 25]
        rows = []
        i, i2, i3 = 1, 2, 3
        for n in range(23):
            rows.append([i, i2, i3])
            i += 1
            i2 += 1
            i3 += 1

        # Quebra do jogo em grupos de 3 números
        game_cells = [
            self.game[0:3], self.game[1:4], self.game[2:5], self.game[3:6], self.game[4:7],
            self.game[5:8], self.game[6:9], self.game[7:10], self.game[8:11], self.game[9:12],
            self.game[10:13], self.game[11:14], self.game[12:15]
        ]

        ""
        # Em todos os jogos, sempre sai alguma sequência de 3 números seguidos (ou quase todos)
        # No período deste projeto, as quantidades mais comuns são: 4, 5, 3, 6
        # Tradução? Em todos os jogos, normalmente há 3, 4, 5 ou 6 grupos de 3 números seguidos
        # [4, 5, 3, 6] são as quantidades com recorrência (acima de 10%), enquanto as outras estão abaixo disso
        # Conforme novos jogos são lançados, novos valores podem entrar (se conseguirem 10%+) ou sair deste array
        # "three_in_a_row_sequence" é o contador dessas quantidades encontradas
        # Ou seja, "three_in_a_row_sequence" deve ser um inteiro entre [4, 5, 3, 6]
        # Caso não seja, o jogo é considerado inválido (por ter grupos de 3 demais ou de menos)
        three_in_a_row_sequence = 0
        for cell in game_cells:
            if cell in rows:
                three_in_a_row_sequence += 1

        # Jogo possui grupos de 3 números seguidos apropriados / não possui
        if three_in_a_row_sequence in reference:
            return {'ok': True, 'report': three_in_a_row_sequence}
        return {'ok': False, 'report': three_in_a_row_sequence}

    # o_a
    @staticmethod
    def get_border_or_center_size(target_game, site, references):
        """
        Mais informações || estatistica/borda_centro_poo.py (Executar)
        Teste            || testes/test_get_border_or_center_size
        """

        # Anexa os números de canto e centro encontrados em "self.game", respectivamente
        card_edges = []
        card_center = []

        # Todos os números de borda do volante (quadrado)
        for n in list(target_game):
            if n == 1 or n == 2 or n == 3 or n == 4 or n == 5 or \
               n == 10 or n == 15 or n == 20 or n == 25 or \
               n == 24 or n == 23 or n == 22 or n == 21 or \
               n == 16 or n == 11 or n == 6:
                card_edges.append(n)

        # Todos os números de centro do volante (retângulo)
        for n in list(target_game):
            if n == 7 or n == 8 or n == 9 or n == 12 or n == 13 or n == 14 or n == 17 or n == 18 or n == 19:
                card_center.append(n)

        ""
        # Quando for desejado analisar os números de borda (16 números)
        # "references[0]" = qtd. de números de borda mais recorrentes (10%+)
        # "card_edges" define a qtd. de números de borda. Essa qtd. estando em "references[0]": jogo válido
        edge_amount = len(card_edges)
        if site == 'edges':
            if edge_amount in references[0]:
                return {'ok': True, 'report': edge_amount, 'array': card_edges}
            return {'ok': False, 'report': edge_amount, 'array': card_edges}

        ""
        # Quando for desejado analisar os números de centro (9 números)
        # "references[1]" = qtd. de números de centro mais recorrentes (10%+)
        # "card_center" define a qtd. de números de centro. Essa qtd. estando em "references[1]": jogo válido
        center_amount = len(card_center)
        if site == 'center':
            if center_amount in references[1]:
                return {'ok': True, 'report': card_center, 'array': card_center}
            return {'ok': False, 'report': card_center, 'array': card_center}

    # q_a
    @staticmethod
    def horizontal_code(reference, target_game):
        # Contagem de números em cada linha
        rows = {'1st': 0, '2nd': 0, '3rd': 0, '4th': 0, '5th': 0}

        # Dos 15 números de "self.game", conforme forem detectados nos ranges, as chaves de "rows" são alteradas
        for number in target_game:
            if number in range(1, 6): rows['1st'] += 1
            elif number in range(6, 11): rows['2nd'] += 1
            elif number in range(11, 16): rows['3rd'] += 1
            elif number in range(16, 21): rows['4th'] += 1
            elif number in range(21, 26): rows['5th'] += 1

        # Todos os valores das chaves em "rows" são passadas p/ uma tupla
        game_code_tuple = tuple(rows.values())

        # Os índices de cada valor são mesclados como um número string
        game_code_str = "".join([str(int_index) for int_index in game_code_tuple])

        # Jogo válido: grupo horizontal de "self.game" está entre os mais comuns / Jogo inválido
        if game_code_str in reference:
            return {
                'ok': True,
                'report': game_code_str,
                'full_report': f'{game_code_str} [{reference.index(game_code_str)}]'
            }
        return {'ok': False, 'report': game_code_str, 'full_report': f'{game_code_str} [inexistente]'}

    # r_a
    @staticmethod
    def vertical_code(reference, target_game):
        # Contagem de números em cada coluna
        columns = {
            '1st': {'sequence': [1, 6, 11, 16, 21], 'countage': 0},
            '2nd': {'sequence': [2, 7, 12, 17, 22], 'countage': 0},
            '3rd': {'sequence': [3, 8, 13, 18, 23], 'countage': 0},
            '4th': {'sequence': [4, 9, 14, 19, 24], 'countage': 0},
            '5th': {'sequence': [5, 10, 15, 20, 25], 'countage': 0}
        }

        ""
        # As chaves "sequence" são todos os 25 números possíveis, quebrados em colunas
        # Cada número de "self.game" é procurado nestes arrays (todos estarão dentre os 25)
        # O que for achado, a chave "countage" é alterada
        # Ex: Supondo que self.game tenha 4, em algum momento, no loop abaixo, ele passará por [4, 9, 14, 19, 24]
        # Antes disso acontecer: '4th': {'sequence': [4, 9, 14, 19, 24], 'countage': 0} "countage" ainda é 0
        # Após disso acontecer : '4th': {'sequence': [4, 9, 14, 19, 24], 'countage': 1} "countage" mudará p/ 1

        for number in target_game:
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

        ""
        # Todos os valores das chaves em "countage" são passadas p/ uma tupla
        # Ex: game_code_tuple = (3, 3, 3, 3, 3) [a soma dos valore sempre será 15]
        game_code_tuple = (
            columns['1st']['countage'], columns['2nd']['countage'], columns['3rd']['countage'],
            columns['4th']['countage'], columns['5th']['countage']
        )

        ""
        # Os índices de cada valor são mesclados como um número string
        # Ex: tomando o exemplo acima [3, 3, 3, 3, 3] se torna '33333'
        game_code_str = "".join([str(int_index) for int_index in game_code_tuple])

        # Se '33333' é um dos índices de "reference": Jogo válido / jogo descartado
        if game_code_str in reference:
            return {
                'ok': True,
                'report': game_code_str,
                'full_report': f'{game_code_str} [{reference.index(game_code_str)}]'
            }
        return {'ok': False, 'report': game_code_str, 'full_report': f' {game_code_str} [inexistente]'}

    def middle_number(self, reference):
        middle_number = self.game[7]
        if middle_number in reference:
            return {'ok': True, 'report': middle_number}
        return {'ok': False, 'report': middle_number}

    # Não está sendo usado
    def divisible_3(self, reference):
        box = []
        for number in self.game:
            if not number % 3:
                box.append(number)

        string_code = "".join([str(index) for index in box])
        if string_code in reference:
            return {'ok': True, 'report': f'{string_code} {box}'}
        return {'ok': False, 'report': f'{string_code} {box}'}

    # Não está sendo usado
    def mean_first_15_numbers(self, reference):
        upper = []
        for number in self.game:
            if number in range(1, 16):
                upper.append(number)
        mean_calculus = f'{sum(upper) / len(upper):.1f}'

        if mean_calculus in reference:
            return {'ok': True, 'report': mean_calculus}
        return {'ok': False, 'report': mean_calculus}

    def verify_game_integrity(self):
        self.conditions = {
            1: self.result.append(True) if self.game_horizontal_blank_free['ok'] else self.result.append(False),
            2: self.result.append(True) if self.game_vertical_blank_free['ok'] else self.result.append(False),
            3: self.result.append(True) if self.game_gap['ok'] else self.result.append(False),
            4: self.result.append(True) if self.game_odd_even_sequence['ok'] else self.result.append(False),
            5: self.result.append(True) if self.game_row_pattern['ok'] else self.result.append(False),
            6: self.result.append(True) if self.game_column_pattern['ok'] else self.result.append(False),
            7: self.result.append(True) if self.game_sequence_in_row['ok'] else self.result.append(False),
            8: self.result.append(True) if self.game_split['ok'] else self.result.append(False),
            9: self.result.append(True) if self.game_prime_numbers['ok'] else self.result.append(False),
            10: self.result.append(True) if self.game_score_15_void['ok'] else self.result.append(False),
            11: self.result.append(True) if self.game_score_14_void['ok'] else self.result.append(False),
            12: self.result.append(True) if self.game_score_13_one_or_plus['ok'] else self.result.append(False),
            13: self.result.append(True) if self.good_numbers['ok'] else self.result.append(False),
            14: self.result.append(True) if self.proper_intersections['ok'] else self.result.append(False),
            15: self.result.append(True) if self.sequence_group['ok'] else self.result.append(False),
            16: self.result.append(True) if self.game_edges['ok'] else self.result.append(False),
            17: self.result.append(True) if self.game_center['ok'] else self.result.append(False),
            18: self.result.append(True) if self.game_horizontal_code['ok'] else self.result.append(False),
            19: self.result.append(True) if self.game_vertical_code['ok'] else self.result.append(False),
            20: self.result.append(True) if self.game_middle_number['ok'] else self.result.append(False),
        }

    def compare_game_with_last_game(self):
        """
        1: Último jogo têm números de canto != das do jogo criado (podem ter qtd. ==)
        2: Último jogo têm números de centro != das do jogo criado (podem ter qtd. ==)
        3: Último jogo têm código horizontal != das do jogo criado
        3: Último jogo têm código vertical != das do jogo criado
        """

        self.conditions_game_vs_last = {
            1: self.comparisons.append(True) if self.last_game_edge['array'] != self.game_edges['array']
            else self.comparisons.append(False),
            2: self.comparisons.append(True) if self.last_game_center['array'] != self.game_center['array']
            else self.comparisons.append(False),
            3: self.comparisons.append(True) if self.last_game_horizontal_code['report'] != self.game_horizontal_code['report']
            else self.comparisons.append(False),
            4: self.comparisons.append(True) if self.last_game_vertical_code['report'] != self.game_vertical_code['report']
            else self.comparisons.append(False)
        }

    def build_game_data_report(self):
        self.report = f"""
        |1| Sem linhas em branco?                      || {self.result[0]} / {self.game_horizontal_blank_free['report']}
        |2| Sem colunas em branco?                     || {self.result[1]} / {self.game_vertical_blank_free['report']}
        |3| Lacunas apropriadas?                       || {self.result[2]} / {self.game_gap['report']}
        |4| Sequência de pares e ímpares apropriadas?  || {self.result[3]} / {self.game_odd_even_sequence['report']}
        |5| Linhas todas de padrão diferente?          || {self.result[4]} / {self.game_row_pattern['report']}
        |6| Colunas todas de padrão diferente?         || {self.result[5]} / {self.game_column_pattern['report']}
        |7| Sequências de números seguidos apropriada? || {self.result[6]} / {self.game_sequence_in_row['report']}
        |8| Tipo de [8/7, 9/6, 10/5]?                  || {self.result[7]} / {self.game_split['report']}
        |9| Quantidade de números primos apropriados?  || {self.result[8]} / {self.game_prime_numbers['report']}
        |10| Nunca fez 15 pontos?                      || {self.result[9]} / {self.game_score_15_void['report']}
        |10| Nunca fez 14 pontos?                      || {self.result[10]} / {self.game_score_14_void['report']}
        |10| Já fez 13 pontos?                         || {self.result[11]} / [ {self.game_score_13_one_or_plus['report']} jogos ]
        |11| Possui os números mais frequentes (4+)?   || {self.result[12]} / {self.good_numbers['report']}
        |12| Interseções [8, 9, 10, 11] presentes?     || {self.result[13]} / {self.proper_intersections['report']}
        |13| Possui qtd. de sequência de 3 apropriada? || {self.result[14]} / {self.sequence_group['report']}
        |14| Possui cantos com qtds. mais comuns?      || {self.result[15]} / {self.game_edges['report']}
        |14| Possui centro com qtds. mais comuns?      || {self.result[16]} / {self.game_center['report']}
        |15| Possui grupo horizontal comum?            || {self.result[17]} / {self.game_horizontal_code['full_report']}
        |16| Possui grupo vertical comum?              || {self.result[18]} / {self.game_vertical_code['full_report']}
        |17| O número do meio está entres os comuns?   || {self.result[19]} / {self.game_middle_number['report']}

        =========== JOGO CRIADO vs ÚLTIMO JOGO ===========

        ========== CONDIÇÃO 1 e 2 ==========
        |1| Bordas diferentes? [{ink('blue', str(self.comparisons[0]))}]
        {self.label}
        {ink('green', str(self.game_edges['array']))} / {ink('green', str(self.game_edges['report']))}
        {ink('yellow', str(self.last_game_edge['array']))} / {ink('yellow', str(self.last_game_edge['report']))}
         
        ========== CONDIÇÃO 3 e 4 ==========
        |1| Centros diferentes? [{ink('blue', str(self.comparisons[1]))}]
        {self.label}
        {ink('green', str(self.game_center['array']))} / {ink('green', str(self.game_center['report']))}
        {ink('yellow', str(self.last_game_center['array']))} / {ink('yellow', str(self.last_game_center['report']))}
        
        ========== CONDIÇÃO 5 ==========
        |2| Grupo horizontal diferentes? [{ink('blue', str(self.comparisons[2]))}]
        {self.label}
        {ink('green', str(self.game_horizontal_code['report']))} / {ink('yellow', str(self.last_game_horizontal_code['report']))}
        
        ========== CONDIÇÃO 6 ==========
        |2| Grupo vertical diferentes? [{ink('blue', str(self.comparisons[3]))}]
        {self.label}
        {ink('green', str(self.game_vertical_code['report']))} / {ink('yellow', str(self.last_game_vertical_code['report']))}
        """

    def store_approved_game(self):
        CardLoopLess.storage.append(self.game)

    def display_game_data_report(self):
        print(self.report)

    def display_proof(self):
        existing_conditions = len(self.result)
        satisfied_conditions = self.result.count(True)
        is_game_ok = "".join(["sim" if False not in self.result else "não"])

        report = f""" {self.indent}========== RELATÓRIO FINAL ==========
        CONDIÇÕES EXISTENTES  || {existing_conditions}
        CONDIÇÕES SATISFEITAS || {satisfied_conditions}
        JOGO APROVADO?        || {is_game_ok}
        PROVA                 || {self.result}
        TENTATIVAS            || {CardLoopLess.attempts} vezes
        JOGOS CRIADOS         || {len(CardLoopLess.storage)}"""

        print(report)
        for game in CardLoopLess.storage:
            print(self.indent, game)

    def game_disqualified(self):
        brick = '=' * 100
        report = f"""
        {brick}
        CONDIÇÕES        || {self.result}
        CONDIÇÕES FALSAS || {self.result.count(False)}
        STATUS           || Jogo reprovado"""
        print(report)

    def __init__(self, db, last_game):
        self.indent = ' ' * 7
        self.warn = f'\n{self.indent}========== AVISO ==========\n'

        self.msg = {
            'error-only-numbers': f'{self.warn}{self.indent}Por favor, informar somente números inteiros\n',
            'shut-down': f'{self.warn}{self.indent}Algoritmo interrompido\n'
        }

        self.database = db

        # a_a
        self.game = self.create_game(length=15)

        # *****************************************************************************************************
        # *****************************************************************************************************
        # *****************************************************************************************************
        # p_a: Dados do último jogo a serem comparados com "self.game"
        self.last_game = last_game
        self.label = f'{ink("green", "JOGO CRIADO")} / {ink("yellow", "ÚLTIMO JOGO")}'

        self.last_game_edge = self.get_border_or_center_size(
            target_game=self.last_game,
            site='edges',
            references=[most_frequent_edges, most_frequent_centers]
        )

        self.last_game_center = self.get_border_or_center_size(
            target_game=self.last_game,
            site='center',
            references=[most_frequent_edges, most_frequent_centers]
        )

        self.last_game_horizontal_code = self.horizontal_code(
            reference=common_horizontal_thread_groups,
            target_game=self.last_game
        )

        self.last_game_vertical_code = self.vertical_code(
            reference=common_vertical_thread_groups,
            target_game=self.last_game
        )

        # *****************************************************************************************************
        # *****************************************************************************************************
        # *****************************************************************************************************
        # Variáveis usadas em "self.conditions"

        # a_a: Criar um jogo aleatório
        self.game = self.create_game(length=15)

        # -----> consultas/espaco_horizontal_branco.py
        # b_a: Jogo não deve ter linha(s) vazia(s)
        self.game_horizontal_blank_free = self.sequence_horizontal()

        # -----> consultas/espaco_vertical_branco.py
        # c_a: Jogo não deve ter coluna(s) vazia(s)
        self.game_vertical_blank_free = self.sequence_vertical()

        # -----> estatistica / primeiros_numeros_poo.py (reference)
        # d_a: Jogo só pode ter nenhuma ou apenas 1 lacuna de 3 números seguidos
        self.game_gap = self.proper_gap(reference=allowed_at_start)

        # -----> estatistica/sequencias_seguidas_v2_poo.py (reference)
        # e_a: Jogo não deve ter sequência string de par/ímpar igual aos encontrados em "reference"
        self.game_odd_even_sequence = self.avoid_large_odd_even_sequence(reference=worst_sequences)

        # -----> consultas/linhas_repetidas.py
        # f_a: Jogo não deve ter linhas repetidas (padrão igual)
        self.game_row_pattern = self.row_repetition()

        # -----> consultas/colunas_repetidas.py
        # g_a: Jogo não deve ter colunas repetidas (padrão igual)
        self.game_column_pattern = self.column_repetition()

        # -----> consultas/numeros_seguidos.py
        # -----> estatistica/numeros_seguidos_v2_poo.py (reference)
        # h_a: Jogo não deve ter muitos números seguidos
        self.game_sequence_in_row = self.avoid_long_sequences(reference=impropers)

        # -----> estatistica/tipo_de_jogo_v2_poo.py (reference)
        # i_a: Jogo deve ser do tipo entre aqueles mais comuns (acima de 10%)
        self.game_split = self.game_type(reference=game_types)

        # -----> estatistica/contar_numeros_primos_v2_poo.py
        # j_a: Jogo deve ter quantidade de números primos entre as quantidades mais recorrentes
        self.game_prime_numbers = self.prime_numbers_counter(
            references=[prime_numbers_amount_allowed, most_common_primes]
        )

        # -----> consultas/pontuacao.py
        # Var 3 recebe mais parâmetros por querer saber se já aconteceu (se fosse 0, não precisaria)
        # k_a: Jogo já fez 13 pontos mais de uma vez, mas nunca fez 14 ou 15
        self.game_score_15_void = self.score_admin(single_score=True, score=15, has_comparison=True)
        self.game_score_14_void = self.score_admin(single_score=True, score=14, has_comparison=True)
        self.game_score_13_one_or_plus = self.score_admin(
            single_score=True,
            score=13,
            has_comparison=True,
            operator='greater',
            repeated=1
        )

        # -----> estatistica/frequencia_numeros_poo.py
        # l_a: Jogo deve ter entre 40% a 70% dos números mais recorrentes
        self.good_numbers = self.numbers_frequency(references=[most_frequent_numbers, percentages])

        # -----> Não possui uma base analítica (é mais empírico)
        # m_a: Jogo em relação aos 10 últimos, deve apresentar padrões de interseção mais naturais
        self.proper_intersections = self.ten_last_comparison(reference=ten_last)

        # -----> estatistica/grupos_de_numeros_poo.py
        # n_a: Jogo deve ter qtd. de grupos de 3 números seguidos dentro da margem de "reference"
        self.sequence_group = self.three_in_a_row_counter(reference=most_common_sequences_of_3_amount)

        # -----> estatistica/borda_centro_poo.py
        # o_a: Jogo deve ter qtd. de números de cantos e centro dentro da margem de "references"
        self.game_edges = self.get_border_or_center_size(
            target_game=self.game,
            site='edges',
            references=[most_frequent_edges, most_frequent_centers]
        )

        self.game_center = self.get_border_or_center_size(
            target_game=self.game,
            site='center',
            references=[most_frequent_edges, most_frequent_centers]
        )

        # -----> estatistica/grupos_horizontais_poo.py
        # q_a: Jogo deve ter quantidade de números por linha dentro do estipulado por "reference"
        self.game_horizontal_code = self.horizontal_code(
            reference=common_horizontal_thread_groups,
            target_game=self.game
        )

        # -----> estatistica/grupos_verticais_poo.py
        # r_a: Jogo deve ter quantidade de números por coluna dentro do estipulado por "reference"
        self.game_vertical_code = self.vertical_code(
            reference=common_vertical_thread_groups,
            target_game=self.game
        )

        # -----> estatistica/numeros_centro.py
        # s_a: Jogo deve ter seu número do meio dentro dos estipulados em "reference"
        self.game_middle_number = self.middle_number(reference=good_middle_numbers)

        # ====================================== PARTE FINAL DO ALGORITMO ======================================
        # Var de confirmação de que "self.game" cumpre todos os requisitos (não deve ter índice False)
        self.result = []

        # Todas os requisitos que "self.game" deve ter para ser criado
        self.conditions = {}
        self.verify_game_integrity()

        # p_a: Var de confirmação de que "self.game" difere do "último jogo" (não deve ter índice False)
        self.comparisons = []

        # Todos os requisitos que "self.game" deve ter de diferente do último jogo
        self.conditions_game_vs_last = {}
        self.compare_game_with_last_game()

        # Configuração de todos os dados do jogo que foram aprovados
        self.report = ''
        self.build_game_data_report()

        # Jogo passou em todos os requisitos e difere do último jogo nos aspectos analisados
        if False not in self.result and False not in self.comparisons:
            self.store_approved_game()
            self.display_game_data_report()
            self.display_proof()

        # Jogo reprovado
        if False in self.result or False in self.comparisons:
            CardLoopLess.attempts += 1
            self.game_disqualified()


if __name__ == '__main__':
    CardLoopLess(db=dtb, last_game=dtb[-1])

    # while len(new_obj.storage) < 2:
    #     new_obj.__init__(db=dtb)
    # print(f'\n{new_obj.indent}========== JOGOS CRIADOS ==========')
    # for game in new_obj.storage:
    #     print(new_obj.indent, game)
