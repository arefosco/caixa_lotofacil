

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

from banco_de_dados.banco import dtb, ten_last
from funcoes.banco_de_dados import ink, ink_random


class Card:

    attempts = 0
    storage = []

    # a_a: Tudo começa criando um jogo de 15 números aleatórios
    def create_game(self, length: int):
        from random import choice

        self.game = set({})

        # Lotofácil possui 25 números
        card = [*range(1, 26)]

        while len(self.game) < length:
            self.game.add(choice(card))

        return list(self.game)

    # b_a: Se deseja saber a sequência horizontal do jogo (ver documentação da função)
    def sequence_horizontal(self,) -> dict:
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

        self.game_horizontal = [row_1, row_2, row_3, row_4, row_5]

        if 0 not in self.game_horizontal:
            return {'blank_free': True, 'sequence': self.game_horizontal}
        return {'blank_free': False, 'sequence': self.game_horizontal}

    # c_a: Se deseja saber a sequência vertical do jogo (ver documentação da função)
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

        self.game_vertical = [column_1, column_2, column_3, column_4, column_5]

        if 0 not in self.game_vertical:
            return {'blank_free': True, 'sequence': self.game_vertical}
        return {'blank_free': False, 'sequence': self.game_vertical}

    # d_a: Executa 3 tipos de verificação (ver o esqueleto da função)
    def proper_gap(self, reference) -> dict:
        """
        Mais informações || consultas/primeiros_numeros.py (executar)
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
            return {'is_proper': False, 'sequence': calculus, 'data': result}

        # O jogo aceitável pode ter: apenas "True" em "result" (máx de 1 lacuna de 3) & (máx de 1 lacuna de 4)
        if False not in result \
                and 'overflow_gap_3' not in result \
                and 'overflow_gap_4' not in result \
                and self.game[0] in reference:
            return {'is_proper': True, 'sequence': calculus, 'data': result}

    # e_a: Controlar a quantidade de pares e ímpares seguidos que o jogo deve ter (ver documentação da função)
    def avoid_large_odd_even_sequence(self, reference) -> dict:
        """
        Mais informações || consultas/sequencias_seguidas_v2.py (executar)
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
            return {'is_proper': False, 'game_string': game_string, 'proof': must_have_false_only}
        return {'is_proper': True, 'game_string': game_string, 'proof': must_have_false_only}

    # f_a: Impedir de criar jogos com linhas de padrão repetido (versão antiga em: executavel/old_codes.py)
    def row_repetition(self) -> dict:
        """
        Mais informações: consultas/linhas_repetidas.py (executar)
        """

        # Teremos aqui 1 array com 1=15 & 0=10 (Volante têm 25 números, 15 são escolhidos e 10 ficam de fora)
        array_of_ones = []
        arrays_of_zeros = []

        # List comprehension p/ não digitar 0 e 1 manualmente
        [array_of_ones.append(1) for n in range(15)]
        [arrays_of_zeros.append(0) for n in range(10)]

        # É preciso saber os números que vão receber 0 (10 números) e os que vão receber 1 (15 números)
        all_numbers = set(range(1, 26))
        ones_to_receive_1 = set(self.game)
        ones_to_receive_zero = all_numbers.difference(ones_to_receive_1)

        # "self.game" trás os números que recebem 1, pois estão no jogo, os que estão fora, receberão 0
        # Junta cada número com o valor pertencente a ele em uma tupla
        # Se temos num jogo (1, 2, 3, ...), será criado [(1, 1), (2, 1), (3, 1)]
        # Se não temos num jogo (4, 5, 6, ...), será criado [(4, 0), (5, 0), (6, 0)]
        ones_inside_game = list(zip(self.game, array_of_ones))
        ones_outside_game = list(zip(ones_to_receive_zero, arrays_of_zeros))

        # Depois de organizar separadamente quem é 0 e quem é 1, vamos juntá-los. Todos farão parte de um mesmo array
        for outsider in ones_outside_game:
            ones_inside_game.append(outsider)

        # Como o índice 0 de cada tupla é o número do volante, vamos arrumar o array com números na ordem crescente
        # [(4, 0), (5, 0), (6, 0), (1, 1), (2, 1), (3, 1)] se torna [(1, 1), (2, 1), (3, 1), (4, 0), (5, 0), (6, 0)]
        tuples_ordered = sorted(ones_inside_game, key=lambda index_1st: index_1st[0])

        # Sabendo quem é zero e quem é 1 e estando organizados, pegamos apenas o índice 1 de cada tupla (seus binários)
        binary_result = [index[1] for index in tuples_ordered]

        # Temos um array com 25 números de 0 e 1, os 1 são números no jogo, os 0 são os ausentes
        # Se quer saber se a fila horizontal do jogo repete, pois o volante têm 5 filas horizontais (desmembra as filas)
        # Então se quebra as 5 filas, convertendo os valores para string para poder tornar o array um valor string
        binary_group_1 = "".join([str(index) for index in binary_result[0:5]])
        binary_group_2 = "".join([str(index) for index in binary_result[5:10]])
        binary_group_3 = "".join([str(index) for index in binary_result[10:15]])
        binary_group_4 = "".join([str(index) for index in binary_result[15:20]])
        binary_group_5 = "".join([str(index) for index in binary_result[20:25]])

        # Temos os código string de cada fila, e havendo uma fila de padrão repetido, será excluída no conjunto
        row_code = [binary_group_1, binary_group_2, binary_group_3, binary_group_4, binary_group_5]
        row_code_as_set = set(row_code)

        """ EXEMPLO
        row_code = ['11000', '11000', '11111', '11100', '00111']
        row_code_as_set = {'11000', '11111', '11100', '00111'}
        . Uma será exluída, pois ['11000' e '11000'] indica (1, 2, 6, 7) = filas idênticas = jogo reprovado
        """

        # Nenhuma fileira é repetida (o conjunto não detectou e o tamanho é mantido = não há linhas repetidas)
        if len(row_code_as_set) == 5:
            return {'empty': True, 'set': row_code_as_set, 'size': len(row_code_as_set)}
        # Alguma fileira é repetida (o conjunto excluiu e o tamanho diminui = há linhas repetidas)
        elif len(row_code_as_set) < 5:
            return {'empty': False, 'set': row_code_as_set, 'size': len(row_code_as_set)}

    # g_a: Impedir de criar jogos com colunas de padrão repetido (versão antiga em: executavel/old_codes.py)
    def column_repetition(self) -> dict:
        """
        Mais informações: consultas/colunas_repetidas.py (executar)
        """

        # Teremos aqui 1 array com 1=15 & 0=10 (Volante têm 25 números, 15 são escolhidos e 10 ficam de fora)
        array_of_ones = []
        arrays_of_zeros = []

        # List comprehension p/ não digitar 0 e 1 manualmente
        [array_of_ones.append(1) for n in range(15)]
        [arrays_of_zeros.append(0) for n in range(10)]

        # É preciso saber os números que vão receber 0 (10 números) e os que vão receber 1 (15 números)
        all_numbers = set(range(1, 26))
        ones_to_receive_1 = set(self.game)
        ones_to_receive_zero = all_numbers.difference(ones_to_receive_1)

        # Juntamos cada número ao valor pertencente a ele em uma tupla. 1 p/ os que estão no jogo, e 0 aos fora do jogo
        # Ou seja, se temos num jogo (1, 2, 3, ...), será criado [(1, 1), (2, 1), (3, 1)]
        # Ou seja, se não temos num jogo (4, 5, 6, ...), será criado [(4, 0), (5, 0), (6, 0)]
        ones_inside_game = list(zip(self.game, array_of_ones))
        ones_outside_game = list(zip(ones_to_receive_zero, arrays_of_zeros))

        # Depois de organizar separadamente quem é 0 e quem é 1, vamos juntá-los. Todos farão parte de um mesmo array
        for tuple_element in ones_outside_game:
            ones_inside_game.append(tuple_element)

        # Como o índice 0 de cada tupla é o número do volante, vamos arrumar o array com números na ordem crescente
        # [(4, 0), (5, 0), (6, 0), (1, 1), (2, 1), (3, 1)] se torna [(1, 1), (2, 1), (3, 1), (4, 0), (5, 0), (6, 0)]
        tuples_ordered = sorted(ones_inside_game, key=lambda index_1st: index_1st[0])

        # Para o código caber na linha abaixo
        x = tuples_ordered

        # Como as colunas estão sendo analisada, e em cada uma temos um tupla (número, binário), pegamos o binário [1]
        # Colunas: [1, 6, 11, 16, 21] [2, 7, 12, 17, 22] [3, 8, 13, 18, 23] [4, 9, 14, 19, 24] [5, 10, 15, 20, 25]
        # Portanto, o que está nos arrays abaixo são os binários de cada número nas colunas
        # Conversão para tupla mandatória, pois conjunto não aceita array como dado
        binary_group_1 = tuple([x[0][1], x[5][1], x[10][1], x[15][1], x[20][1]])
        binary_group_2 = tuple([x[1][1], x[6][1], x[11][1], x[16][1], x[21][1]])
        binary_group_3 = tuple([x[2][1], x[7][1], x[12][1], x[17][1], x[22][1]])
        binary_group_4 = tuple([x[3][1], x[8][1], x[13][1], x[18][1], x[23][1]])
        binary_group_5 = tuple([x[4][1], x[9][1], x[14][1], x[19][1], x[24][1]])

        # Para não ficar código repetido
        del tuples_ordered

        # Cada tupla é inserida num array, e após ser convertida p/ conjunto, se houver tuplas iguais, serão exluídas
        row_code = [binary_group_1, binary_group_2, binary_group_3, binary_group_4, binary_group_5]
        row_code_as_set = set(row_code)

        # Nenhuma coluna é repetida (o conjunto não detectou e o tamanho é mantido = não há colunas repetidas)
        if len(row_code_as_set) == 5:
            return {'empty': True, 'set': row_code_as_set, 'size': len(row_code_as_set)}
        # Alguma coluna é repetida (o conjunto excluiu e o tamanho diminui = há colunas repetidas)
        elif len(row_code_as_set) < 5:
            return {'empty': False, 'set': row_code_as_set, 'size': len(row_code_as_set)}

    # h_a: Impedir que jogos com mais de 6 números seguidos sejam aprovados (ver documentação da função)
    def avoid_long_sequences(self, reference: list, first_index=0, second_index=1) -> dict:
        """
        Mais informações || consultas/numeros_seguidos.py (executar)
        Teste            || testes.py/test_avoid_long_sequences
        """

        # Recebe os cálculos no loop, recebe string dos cálculos, strings não permitidas (seq. seguidas longas)
        integer_list, answer = [], []

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

        "Código antigo substituído"
        # Se for achado entre 6 a 8 números seguidos, o jogo é reprovado (+ números seguidos é praticamente impossível)
        # if in_row_7 in answer_code or in_row_8 in answer_code or in_row_9 in answer_code:
        #     return {'is_proper': False, 'calculus': integer_list, 'code': answer, 'code_str': answer_code}
        # Até 5 valores seguidos (aceitável)
        # return {'is_proper': True, 'calculus': integer_list, 'code': answer, 'code_str': answer_code}

        report = []
        for code in reference:
            if code not in answer_code: report.append(True)
            else: report.append(False)

        # O parâmetro "reference" contém os padrões menos comuns (ruins). "False" indica a presença desses padrões
        if False in report:
            return {'is_proper': False, 'calculus': integer_list, 'code_str': answer_code, 'report': report}
        return {'is_proper': True, 'calculus': integer_list, 'code_str': answer_code, 'report': report}

    # i_a: Controlar a distribuição dos números num jogo (ver documentação da função)
    def game_type(self, reference) -> dict:
        """
        Mais informações || consultas/tipo_de_jogo_v2.py
        Teste            || testes.py/test_game_type
        """

        # Contador da parte 1, contador da parte2, parte 1 do volante, parte 2 do volante
        upper, lower, upper_area, lower_area = 0, 0, tuple(range(1, 16)), tuple(range(16, 26))

        for number in self.game:
            if number in upper_area:
                upper += 1
            elif number in lower_area:
                lower += 1

        game_class = f"{upper}/{lower}"

        "Substituído por [core_var]"
        # De acordo com "consultas/tipo_de_jogo.py" esses tipos são os mais recorrentes
        # right = ['8/7', '9/6', '10/5']

        if game_class in reference:
            return {'is_proper': True, 'type': game_class}
        return {'is_proper': False, 'type': game_class}

    # j_a: Controlar a qtd. de números primos que um jogo pode ter (ver documentação da função)
    def prime_numbers_counter(self, references) -> dict:
        """
        Mais informações || consultas/contar_numeros_primos_v2.py
        Teste            || testes.py/test_prime_numbers_counter
        """

        prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23]
        prime_numbers_box = []

        "Substituída por [primes]"
        # De acordo com "consultas/contar_numeros_primos.py" a qtd. de números primos mais comuns: [4, 5, 6, 7]
        # proper_amounts = range(4, 8)

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

        if len(prime_numbers_box) in references[0]:
            return {'is_proper': True, 'primes': prime_numbers_box, 'amount': len(prime_numbers_box)}
        return {'is_proper': False, 'primes': prime_numbers_box, 'amount': len(prime_numbers_box)}

    # k_a: Verificar ou programar se uma pontuação do jogo possui valor indesejado
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
        similarities = []

        # Os jogos são tuplas, mas p/ saber a interseção é preciso conversão p/ conjunto
        # O método [ intersection() ] está dentro de [ len() ] p/ que o retorno seja inteiro
        for i in range(len(self.database)):
            similarity_target_game_vs_db_game = len(set(self.game).intersection(set(self.database[i])))
            similarities.append(similarity_target_game_vs_db_game)

        precisions = [
            similarities.count(6), similarities.count(7), similarities.count(8), similarities.count(9),
            similarities.count(10), similarities.count(11), similarities.count(12), similarities.count(13),
            similarities.count(14), similarities.count(15)
        ]

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

        # Quando for desejado saber um dos pontos (entre 6 a 15) (via "target_score")
        if single_score:
            # Pontuação: quantas vezes fez essa pontuação
            scores = {
                6: precisions[0], 7: precisions[1], 8: precisions[2], 9: precisions[3], 10: precisions[4],
                11: precisions[5], 12: precisions[6], 13: precisions[7], 14: precisions[8], 15: precisions[9],
            }

            # Via "target_score" se pega o valor da chave "key", então "box_with_score" recebe o valor da chave achada
            box_with_score = []
            [box_with_score.append(scores[key]) for key in scores if score == key]

            correct = {'is_proper': True, 'banner': score_panel, 'amount': box_with_score[0]}
            incorrect = {'is_proper': False, 'banner': score_panel, 'amount': box_with_score[0]}

            # (has_comparison, operator, repeated) (comparação desejada, comparador, pontuação)
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

    # l_a: Controlar quantos dos números mais frequentes devem vir
    def numbers_frequency(self, references) -> dict:
        """
        Mais informações || consultas/frequencia_numeros.py
        Teste            || testes/test_numbers_frequency
        """
        # "reference" sempre possuirá muitos índices, pois a distribuição de números é sempre justa

        similarity = set(self.game).intersection(set(references[0]))
        similarity_amount = len(similarity)

        # No tempo que esta função foi feita, "len(reference)=10"
        # "self.game" deve ter a partir de 4 entre todos os números mais frequentes, e não exceder 7
        if references[1]['40%'] <= similarity_amount <= references[1]['70%']:
            return {'is_proper': True, 'data': similarity}
        return {'is_proper': False, 'data': similarity}

    # m_a
    def ten_last_comparison(self, reference) -> dict:
        """
        Mais informações || não possui
        Teste            || testes_test_ten_last_comparison
        """

        result = []
        for index, game in enumerate(reference):
            result.append(len(set(game).intersection(set(self.game))))

        must_not_have_false = []
        bad_codes = ['888', '8888', '88888', '999', '9999', '99999', '101010', '10101010', '1010101010']
        intersection_code = "".join([str(index) for index in result])

        # Impedir que as sequências de interseções seguidas acima saiam
        for code in bad_codes:
            if code not in intersection_code: must_not_have_false.append(True)
            else: must_not_have_false.append(False)

        few_twins_intersections_in_row = None
        if must_not_have_false.count(False) == 0:
            few_twins_intersections_in_row = True
        else:
            few_twins_intersections_in_row = False

        too_similar = False
        if result.count(11) > 2: too_similar = True

        # Interseções em ordem crescente ou decrescente são algo sem lógica
        where_the_error_is = []
        result_str = "".join([str(number) for number in result])

        if '891011' in result_str: where_the_error_is.append(0)
        if '111098' in result_str: where_the_error_is.append(1)
        if '8910' in result_str: where_the_error_is.append(2)
        if '91011' in result_str: where_the_error_is.append(3)
        if '11109' in result_str: where_the_error_is.append(4)
        if '1098' in result_str: where_the_error_is.append(5)

        "EM RELAÇÃO AOS 10 ÙLTIMOS JOGOS"
        # O jogo criado não pode ter tido: interseção (5 ao 7) e (12 ao 15)
        # O jogo criado deve ter tido:     interseção (8 a 11)
        # A interseção do jogo criado com o último não pode ser de (11, 15) e nem 7, ou seja: 8 até 10
        # Máximo de 2 interseções iguais seguidas
        # Interseção do último jogo != da do penúltimo
        if 5 not in result and 6 not in result and 7 not in result and 12 not in result and 13 not in result \
                and 14 not in result and 15 not in result \
                and 8 in result and 9 in result and 10 in result and 11 in result \
                and result[-1] not in range(11, 16) and result[-1] != 7 \
                and result[-1] != result[-2] \
                and few_twins_intersections_in_row \
                and not too_similar \
                and where_the_error_is == []:
            return {'is_proper': True, 'intersections': result}
        return {'is_proper': False, 'intersections': result}

    # n_a: Controlar quantas sequência de 3 números seguidos podem vir com base em "reference"
    def three_in_a_row_counter(self, reference) -> dict:
        """
        Mais informações || consultas/grupos_de_numeros.py (Executar)
        Teste            || testes/test_three_in_a_row_counter
        """

        i, i2, i3 = 1, 2, 3
        rows = []
        for n in range(23):
            rows.append([i, i2, i3])
            i += 1
            i2 += 1
            i3 += 1

        game_cells = [
            self.game[0:3], self.game[1:4], self.game[2:5], self.game[3:6], self.game[4:7],
            self.game[5:8], self.game[6:9], self.game[7:10], self.game[8:11], self.game[9:12],
            self.game[10:13], self.game[11:14], self.game[12:15]
        ]

        three_in_a_row_sequence = 0
        for cell in game_cells:
            if cell in rows:
                three_in_a_row_sequence += 1

        # Em "reference" temos as sequências que alcançaram + de 10% (mais comuns), abaixo disso (menos comuns)
        if three_in_a_row_sequence in reference:
            return {'is_proper': True, 'amount': three_in_a_row_sequence}
        return {'is_proper': False, 'amount': three_in_a_row_sequence}

    # o_a: Controlar quantos números de canto e centro um jogo pode ter (mais infos: docstring)
    @staticmethod
    def get_border_or_center_size(target_game, site, references):

        card_edges = []
        card_center = []

        # Todos os números de borda do volante
        for n in list(target_game):
            if n == 1 or n == 2 or n == 3 or n == 4 or n == 5 or \
                    n == 10 or n == 15 or n == 20 or n == 25 or \
                    n == 24 or n == 23 or n == 22 or n == 21 or \
                    n == 16 or n == 11 or n == 6:
                card_edges.append(n)

        # Todos os números de centro do volante
        for n in list(target_game):
            if n == 7 or n == 8 or n == 9 or n == 12 or n == 13 or n == 14 or n == 17 or n == 18 or n == 19:
                card_center.append(n)

        if site == 'edges':
            if len(card_edges) in references[0]:
                return {'is_proper': True, 'report': card_edges}
            return {'is_proper': False, 'report': card_edges}
        elif site == 'center':
            if len(card_center) in references[1]:
                return {'is_proper': True, 'report': card_center}
            return {'is_proper': False, 'report': card_center}

    # q_a
    def impropers_start_and_end(self):

        start = None
        end = None

        game_as_code = "".join([str(number) for number in self.game])

        if '135' in game_as_code[0:3] and '24' not in game_as_code[0:2]: start = False
        if '24' in game_as_code[0:2] and '135' not in game_as_code[0:3]: start = False
        if '135' not in game_as_code[0:3] and '24' not in game_as_code[0:2]: start = True
        if '2224' in game_as_code[-4:] and '212325' not in game_as_code[-6:]: end = False
        if '212325' in game_as_code[-6:] and '2224' not in game_as_code[-4:]: end = False
        if '2224' not in game_as_code[-4:] and '212325' not in game_as_code[-6:]: end = True

        if start and end:
            return {'is_proper': True, 'report': (start, end)}
        return {'is_proper': False, 'report': (start, end)}

    def __init__(self, db, last_game):
        self.indent = ' ' * 7
        self.warn = f'\n{self.indent}========== AVISO ==========\n'

        self.msg = {
            'error-only-numbers': f'{self.warn}{self.indent}Por favor, informar somente números inteiros\n',
            'shut-down': f'{self.warn}{self.indent}Algoritmo interrompido\n'
        }

        self.database = db

        try:
            # Inserido ao final do algoritmo, junto ao tratamento acima
            self.games_amount = int(input('Criar quantos jogos? (clique após a seta e digite) -------> '))

            # Para contar dados incrementáveis, é melhor criar uma "var de classe" ao invés de uma "var self"
            while len(Card.storage) < self.games_amount:

                # a_a
                self.game = self.create_game(length=15)

                # p_a: Todos os dados que vierem abaixo desta hash, serão dados comparáveis
                self.last_game = last_game
                self.label = f'{ink("green", "JOGO CRIADO")} / {ink("yellow", "ÚLTIMO JOGO")}'

                # =================================== PARA USO EM: self.comparisons ===================================
                self.last_game_edge = self.get_border_or_center_size(
                    target_game=self.last_game,
                    site='edges',
                    references=[most_frequent_edges, most_frequent_centers]
                )['report']

                self.last_game_center = self.get_border_or_center_size(
                    target_game=self.last_game,
                    site='center',
                    references=[most_frequent_edges, most_frequent_centers]
                )['report']

                # Variáveis usadas dentro da condição principal
                self.game_horizontal_blank_free = self.sequence_horizontal()['blank_free']                   # b_a
                self.game_vertical_blank_free = self.sequence_vertical()['blank_free']                       # c_a
                self.game_gap = self.proper_gap(reference=allowed_at_start)['is_proper']  # d_a
                self.game_odd_even_sequence_proper = self.avoid_large_odd_even_sequence(reference=worst_sequences)['is_proper']  # e_a
                self.game_row_pattern = self.row_repetition()['empty']                                                # f_a
                self.game_column_pattern = self.column_repetition()['empty']                                          # g_a
                self.game_sequence_in_row = self.avoid_long_sequences(reference=impropers)['is_proper']               # h_a
                self.game_split = self.game_type(reference=game_types)['is_proper']                                   # i_a
                self.game_prime_numbers = self.prime_numbers_counter(references=[prime_numbers_amount_allowed, most_common_primes])['is_proper']  # j_a

                # k_a: Dados que ficam melhor separados dos outros (13 recebe + pars devido ser > 0)
                self.game_score_15_void = self.score_admin(single_score=True, score=15, has_comparison=True)['is_proper']
                self.game_score_14_void = self.score_admin(single_score=True, score=14, has_comparison=True)['is_proper']
                self.game_score_13_one_or_plus = self.score_admin(single_score=True, score=13, has_comparison=True, operator='greater', repeated=1)['is_proper']

                self.good_numbers = self.numbers_frequency(references=[most_frequent_numbers, percentages])['is_proper']  # l_a
                self.proper_intersections = self.ten_last_comparison(reference=ten_last)['is_proper']             # m_a
                self.sequence_group = self.three_in_a_row_counter(reference=most_common_sequences_of_3_amount)['is_proper']   #

                # o_a
                self.game_edges = self.get_border_or_center_size(
                    target_game=self.game,
                    site='edges',
                    references=[most_frequent_edges, most_frequent_centers]
                )['is_proper']

                self.game_center = self.get_border_or_center_size(
                    target_game=self.last_game,
                    site='center',
                    references=[most_frequent_edges, most_frequent_centers]
                )['is_proper']

                # q_a
                self.game_start_and_end = self.impropers_start_and_end()['is_proper']

                # Variáveis opcionais usadas fora da condição principal
                self.game_horizontal = self.sequence_horizontal()['sequence']
                self.game_vertical = self.sequence_vertical()['sequence']
                self.game_gap_scan = self.proper_gap(reference=allowed_at_start)['sequence']
                self.game_odd_even_sequence = self.avoid_large_odd_even_sequence(reference=worst_sequences)['game_string']
                self.game_line_set = self.row_repetition()['size']
                self.game_column_set = self.column_repetition()['size']
                self.game_sequence_in_row_code = self.avoid_long_sequences(reference=impropers)['code_str']
                self.game_split_code = self.game_type(reference=game_types)['type']
                self.game_prime_numbers_box = self.prime_numbers_counter(references=[prime_numbers_amount_allowed, most_common_primes])['primes']

                # Dados que ficam melhor separados dos outros
                self.game_score_query_15 = self.score_admin(single_score=True, score=15, has_comparison=True)['amount']
                self.game_score_query_14 = self.score_admin(single_score=True, score=14, has_comparison=True)['amount']
                self.game_score_query_13 = self.score_admin(single_score=True, score=13, has_comparison=True, operator='greater', repeated=1)['amount']

                self.good_numbers_report = self.numbers_frequency(references=[most_frequent_numbers, percentages])['data']
                self.proper_intersections_report = self.ten_last_comparison(reference=ten_last)['intersections']
                self.sequence_group_report = self.three_in_a_row_counter(reference=most_common_sequences_of_3_amount)['amount']
                self.game_start_and_end_report = self.impropers_start_and_end()['report']

                # =================================== PARA USO EM: self.comparisons ===================================
                self.game_edges_report = self.get_border_or_center_size(
                    target_game=self.game, site='edges', references=[most_frequent_edges, most_frequent_centers]
                )['report']

                self.game_center_report = self.get_border_or_center_size(
                    target_game=self.game, site='center', references=[most_frequent_edges, most_frequent_centers]
                )['report']

                # ====================================== PARTE FINAL DO ALGORITMO ======================================
                self.result = []

                self.conditions = {
                    1: self.result.append(True) if self.game_horizontal_blank_free else self.result.append(False),
                    2: self.result.append(True) if self.game_vertical_blank_free else self.result.append(False),
                    3: self.result.append(True) if self.game_gap else self.result.append(False),
                    4: self.result.append(True) if self.game_odd_even_sequence_proper else self.result.append(False),
                    5: self.result.append(True) if self.game_row_pattern else self.result.append(False),
                    6: self.result.append(True) if self.game_column_pattern else self.result.append(False),
                    7: self.result.append(True) if self.game_sequence_in_row else self.result.append(False),
                    8: self.result.append(True) if self.game_split else self.result.append(False),
                    9: self.result.append(True) if self.game_prime_numbers else self.result.append(False),
                    10: self.result.append(True) if self.game_score_15_void else self.result.append(False),
                    11: self.result.append(True) if self.game_score_14_void else self.result.append(False),
                    12: self.result.append(True) if self.game_score_13_one_or_plus else self.result.append(False),
                    13: self.result.append(True) if self.good_numbers else self.result.append(False),
                    14: self.result.append(True) if self.proper_intersections else self.result.append(False),
                    15: self.result.append(True) if self.sequence_group else self.result.append(False),
                    16: self.result.append(True) if self.game_edges else self.result.append(False),
                    17: self.result.append(True) if self.game_center else self.result.append(False),
                    18: self.result.append(True) if self.game_start_and_end else self.result.append(False),
                }

                # p_a: Recebe resultados das comparações do jogo criado em relação ao último (ver + no docstring)
                self.comparisons = []

                self.conditions_game_vs_last = {
                    1: self.comparisons.append(True) if self.last_game_edge != self.game_edges
                    else self.comparisons.append(False),
                    2: self.comparisons.append(True) if len(self.last_game_edge) != len(self.game_edges_report)
                    else self.comparisons.append(False),
                    3: self.comparisons.append(True) if self.last_game_center != self.game_center
                    else self.comparisons.append(False),
                    4: self.comparisons.append(True) if len(self.last_game_center) != len(self.game_center_report)
                    else self.comparisons.append(False),
                }

                self.report = f"""
                |1| Sem linhas em branco?                      -> {self.result[0]} / {self.game_horizontal}
                |2| Sem colunas em branco?                     -> {self.result[1]} / {self.game_vertical}
                |3| Lacunas apropriadas?                       -> {self.result[2]} / {self.game_gap_scan}
                |4| Sequência de pares e ímpares apropriadas?  -> {self.result[3]} / {self.game_odd_even_sequence}
                |5| Linhas todas de padrão diferente?          -> {self.result[4]} / {self.game_line_set}
                |6| Colunas todas de padrão diferente?         -> {self.result[5]} / {self.game_column_set}
                |7| Sequências de números seguidos apropriada? -> {self.result[6]} / {self.game_sequence_in_row_code}
                |8| Tipo de [8/7, 9/6, 10/5]?                  -> {self.result[7]} / {self.game_split_code}
                |9| Quantidade de números primos apropriados?  -> {self.result[8]} / {self.game_prime_numbers_box}
                |10| Nunca fez 15 pontos?                      -> {self.result[9]} / {self.game_score_query_15}
                |10| Nunca fez 14 pontos?                      -> {self.result[10]} / {self.game_score_query_14}
                |10| Já fez 13 pontos?                         -> {self.result[11]} / [ {self.game_score_query_13} jogos ]
                |11| Possui os números mais frequentes (4+)?   -> {self.result[12]} / {self.good_numbers_report}
                |12| Interseções [8, 9, 10, 11] presentes?     -> {self.result[13]} / {self.proper_intersections_report}
                |13| Possui qtd. de sequência de 3 apropriada? -> {self.result[14]} / {self.sequence_group_report}
                |14| Possui cantos com qtds. mais comuns?      -> {self.result[15]} / {self.game_edges_report}
                |14| Possui centro com qtds. mais comuns?      -> {self.result[16]} / {self.game_center_report}
                |15| Início e final do jogo apropriado?        -> {self.result[17]} / {self.game_start_and_end_report} / {self.game[0:3]} {self.game[-3:]}
    
                =========== JOGO CRIADO vs ÚLTIMO JOGO ===========
    
                ========== CONDIÇÃO 1 ==========
                |1| Bordas diferentes? [{ink('blue', str(self.comparisons[0]))}]
                {self.label}
                {ink('green', str(self.game_edges_report))} / {ink('yellow', str(self.last_game_edge))}
    
                ========== CONDIÇÃO 2 ==========
                |2| Bordas em quantidades diferentes? [{ink('blue', str(self.comparisons[1]))}]
                {self.label}
                {ink('green', str(len(self.game_edges_report)))} / {ink('yellow', str(len(self.last_game_edge)))}
    
                ========== CONDIÇÃO 3 ==========
                |1| Centros diferentes? [{ink('blue', str(self.comparisons[2]))}]
                {self.label}
                {ink('green', str(self.game_center_report))} / {ink('yellow', str(self.last_game_center))}
    
                ========== CONDIÇÃO 4 ==========
                |2| Centros em quantidades diferentes? [{ink('blue', str(self.comparisons[3]))}]
                {self.label}
                {ink('green', str(len(self.game_center_report)))} / {ink('yellow', str(len(self.last_game_center)))}
                """

                print(self.report)

                # Segunda condição adicionada com a criação de "p_a"
                if False not in self.result and False not in self.comparisons:
                    # print(self.indent, '========== JOGO CRIADO ==========')
                    print(f"{self.indent} Tentativas do algoritmo? {Card.attempts}")
                    Card.storage.append(self.game)
                    # print(self.indent, self.game)

                if False in self.result:
                    Card.attempts += 1
                    print(self.indent, self.result)
                    print(self.indent, f"Condições falsas? {self.result.count(False)}")
                    print(self.indent, 'Jogo reprovado')

                print(f'\n{self.indent}========== JOGOS CRIADOS: {len(Card.storage)} ==========')
                for game in Card.storage:
                    print(self.indent, game)

        except ValueError:
            print(ink_random(self.msg['error-only-numbers']))
            self.__init__(db=dtb, last_game=dtb[-1])
        except KeyboardInterrupt:
            print(ink_random(self.msg['shut-down']))


if __name__ == '__main__':
    Card(db=dtb, last_game=dtb[-1])

    # while len(new_obj.storage) < 2:
    #     new_obj.__init__(db=dtb)
    # print(f'\n{new_obj.indent}========== JOGOS CRIADOS ==========')
    # for game in new_obj.storage:
    #     print(new_obj.indent, game)
