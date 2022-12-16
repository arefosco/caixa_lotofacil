

"""
# o_a:
    O método é estático, pois "target_game" é preciso para criar separado: [self.game, self.last_game]
    Caso contrário, precisaria criar um método separado para os 2

# p_a:
    É muito comum os dados do último jogo serem diferentes do próximo (mas não é impossível virem iguais)
    "self.comparisons" guardará todas as comparações que forem consideradas cabíveis entre o jogo cridao e o último

===== PROCEDIMENTO DE IMPLEMENTAÇÃO DE NOVAS FUNÇÕES =====
1. Criar um algoritmo que filtre os melhores dados de acordo com a necessidade almejada
1. Nesses algoritmos, normalmente uma variável ou+ de classe é gerada para uso no algoritmo principal (este módulo)
1. Essa variável é um resultado da filtragem feita pelo algoritmo, e usada nas funções deste módulo
1. Esses algoritmos normalmente ficam no diretório "estatística"
2. Importar essa "var de referência" para este módulo
3. Criar a função que fará uma atividade e inserir no seu contexto, a "var de referência" (externa) como parâmetro
4. Criar a var self que será objeto dessa função nova
5. Colocar essa var self (com a chave apropriada) na var self de condição [verify_game_integrity]
6. Colocar essa var self (com a chave apropriada) na var self que exibe os resultados [build_game_data_report]
"""

from estatistica.primeiros_numeros_poo import allowed_at_start
from estatistica.sequencias_seguidas_v2_poo import worst_sequences
from estatistica.numeros_seguidos_v2_poo import impropers
from estatistica.tipo_de_jogo_v2_poo import game_types
from estatistica.contar_numeros_primos_v2_poo import (prime_numbers_amount_allowed, most_common_primes)
from estatistica.frequencia_numeros_poo import (most_frequent_numbers, percentages)
from estatistica.grupos_de_numeros_poo import most_common_sequences_of_3_amount
from estatistica.borda_centro_poo import (most_frequent_edges, most_frequent_centers)
from estatistica.grupos_horizontais_poo import common_horizontal_thread_groups
from estatistica.grupos_verticais_poo import common_vertical_thread_groups
from estatistica.numeros_centro import good_middle_numbers
from estatistica.historico_numeros import (proper_numbers_by_position, tolerable_mistakes)

from banco_de_dados.banco import dtb, ten_last
from funcoes.banco_de_dados import ink, ink_random


class Card:

    attempts = 0
    storage = []

    # a_a
    def create_game(self, length: int):
        """
        ===== self.game ===== \n
        * o jogo é inicialmente um conjunto vazio \n
        * motivo? conjuntos não repetem dados, e um jogo da Lotofácil segue esse padrão \n

        ===== card ===== \n
        * representa semanticamente o volante de um jogo da Lotofácil (cartilha com 25 números, 1 ao 25) \n

        ===== loop ===== \n
        * enquanto "self.game" não tiver 15 números diferentes: não há jogo
        """

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
        ===== Mais informações ===== \n
        * consultas/espaco_horizontal_branco.py \n

        ===== Teste da função ===== \n
        * testes/testes.py/test_sequence_horizontal \n

        ===== row_int ===== \n
        * sequência de 5 vars que são contadoras de qtd. de números por linha (horizontal) \n
        * "self.game" possui 15 números escolhidos entre 1 a 25, a incrementação das vars "row" é explicada a seguir \n
        *  "row_1: 1 ao 5"   "row_2: 6 ao 10"   "row_3: 11 ao 15"   "row_4: 16 ao 20"   "row_5: 21 ao 25" \n
        * essa incrementação acontece no loop for (ver Análise [1]) \n

        ===== game_horizontal ===== \n
        * ao termos todas as incrementação feitas nas vars "row_int", esses valores são anexados nesta var \n
        * temos um array com um código de sequências de inteiros que representam a contagem de números por linha \n

        ===== condição final ===== \n
        * o objetivo da função é não deixar passar "self.game" com linhas vazias (padrão incomum) \n
        * isso é detectado pela presença de 0 dentre os índices de "game_horizontal" \n
        * não havendo 0 em "game_horizontal": jogo válido
        """

        row_1, row_2, row_3, row_4, row_5 = 0, 0, 0, 0, 0

        row_1_numbers = [*range(1, 6)]
        row_2_numbers = [*range(6, 11)]
        row_3_numbers = [*range(11, 16)]
        row_4_numbers = [*range(16, 21)]
        row_5_numbers = [*range(21, 26)]

        # Análise [1]
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
        ===== Mais informações ===== \n
        * consultas/espaco_vertical_branco.py \n

        ===== Teste da função ===== \n
        * testes/testes.py/test_sequence_vertical \n

        ===== column_int ===== \n
        * sequência de 5 vars que são contadoras de qtd. de números por coluna (vertical) \n
        * "self.game" possui 15 números escolhidos entre 1 a 25, a incrementação das vars "column" é explicada abaixo \n
        * ex: column_1 é incrementada conforme um dos números de self.game" for encontrado em "column_1_numbers" \n
        * a lógica acima se aplica até o inteiro 5, pois temos 5 linhas e 5 colunas \n
        * essa incrementação acontece no loop for (ver Análise [1]) \n

        ===== game_vertical ===== \n
        * ao termos todas as incrementação feitas nas vars "column_int", esses valores são anexados nesta var \n
        * temos um array com um código de sequências de inteiros que representam a contagem de números por coluna \n

        ===== condição final ===== \n
        * o objetivo da função é não deixar passar "self.game" com colunas vazias (padrão incomum) \n
        * isso é detectado pela presença de 0 dentre os índices de "game_vertical" \n
        * não havendo 0 em "game_vertical": jogo válido
        """

        column_1, column_2, column_3, column_4, column_5 = 0, 0, 0, 0, 0

        column_1_numbers = [1, 6, 11, 16, 21]
        column_2_numbers = [2, 7, 12, 17, 22]
        column_3_numbers = [3, 8, 13, 18, 23]
        column_4_numbers = [4, 9, 14, 19, 24]
        column_5_numbers = [5, 10, 15, 20, 25]

        # Análise [1]
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
        ===== Mais informações ===== \n
        * estatistica/primeiros_numeros_poo.py

        ===== Teste ===== \n
        * testes/testes.py/test_proper_gap \n

        ===== result ===== \n
        * var que recebe booleanos e strings vindo de 3 análises diferentes
        * as análises estão marcadas por (# Análise int) no conteúdo da função

        ===== calculus ===== \n
        * recebe a subtração do índice posterior pelo índice anterior de "self.game"
        * (índice 1 - índice 0)...(índice 2 - índice 1)...(índice 3 - índice 2)...
        * esses valores são essenciais p/ as vars "gap_of_3_amount" e "gap_of_4_amount"

        ===== gap_of_3_amount ===== \n
        * var que verifica "result", procurando valores 4 (lacunas de 3)
        * lacunas de 3 acontecem com alguma frequência, mas não são maioria
        * é estipulado que um jogo normal, tenha no máximo 1 lacuna de 3, ou nenhuma
        * se seu valor for > 1 (mais de uma lacuna de 3): jogo invalidado, pois "result" recebe "gap_overflow_3"

        ===== gap_of_4_amount ===== \n
        * var que verifica "result", procurando valores 5 (lacunas de 4)
        * lacunas de 4 são incomuns, por isso devem ser evitadas/barradas
        * é estipulado que um jogo normal, não tenha lacunas de 4
        * se seu valor for != 0 (há alguma lacuna de 4): jogo invalidado, pois "result" recebe "gap_overflow_4"

        ===== Condições finais ===== \n
        * "result" não tendo "overflow_gap_3", "overflow_gap_4": jogo válido
        """

        result = []
        calculus = []

        index_first = 0
        index_second = 1

        while index_second < len(self.game):
            calculus.append(self.game[index_second] - self.game[index_first])

            index_first += 1
            index_second += 1

        gap_of_3_amount = calculus.count(4)
        gap_of_4_amount = calculus.count(5)

        # Análise [1]: O jogo só pode ter 1 lacuna de 3
        if gap_of_3_amount > 1: result.append('overflow_gap_3')
        # Análise [2]: O jogo não pode ter qualquer lacuna de 4
        if gap_of_4_amount != 0: result.append('overflow_gap_4')

        # Jogo reprovado
        if 'overflow_gap_3' in result or 'overflow_gap_4' in result or self.game[0] not in reference:
            return {'ok': False, 'report': calculus, 'data': result}

        # Jogo aprovado
        if 'overflow_gap_3' not in result and 'overflow_gap_4' not in result and self.game[0] in reference:
            return {'ok': True, 'report': calculus, 'data': result}

    # e_a
    def avoid_large_odd_even_sequence(self, reference) -> dict:
        """
        ===== Mais informações ===== \n
        * estatistica/sequencias_seguidas_v2_poo.py

        ===== Teste da função ===== \n
        * testes/testes.py/test_avoid_large_odd_even_sequence \n

        ===== box ===== \n
        * recebe strings ['i' = ìmpar] e ['p' = par] ao iterar sob cada índice de "self.game" \n

        ===== game_string ===== \n
        * converte a lista com 'i' e 'p' p/ uma string de todas elas mescladas \n
        * o valor dessa string não deve estar em "reference", senão será invalidado \n

        ===== reference ===== \n
        * var fonte que possui todas as piores sequências string de 'i' e 'p' (mais incomuns) \n

        ===== must_have_false_only ===== \n
        * var de confirmação que recebe "True" e "False" \n
        * se há "True", "self.game" possui uma sequência de 'i' e 'p' dentre as piores sequências: jogo inválido
        """

        box = []
        odd, even = 'p', 'i'
        [box.append(odd) if not number % 2 else box.append(even) for number in self.game]
        game_string = "".join(box)

        must_have_false_only = []

        for code in reference: must_have_false_only.append(code in game_string)

        if True in must_have_false_only:
            return {'ok': False, 'report': game_string, 'proof': must_have_false_only}
        return {'ok': True, 'report': game_string, 'proof': must_have_false_only}

    # f_a
    def row_repetition(self) -> dict:
        """
        ===== Mais informações ===== \n
        * consultas/linhas_repetidas.py \n

        ===== Testes da função ===== \n
        * testes/testes.py/test_row_repetition \n

        ===== array_of_ones ===== \n
        * array com 15 índices 1, onde "1" é a representação de números que foram chamados no jogo \n

        ===== array_of_zeros ===== \n
        * array com 10 índices 0, onde "0" é a representação de números que não foram chamados no jogo \n

        ===== ones_to_receive_1 ===== \n
        * possui todos os índices de "self.game" \n
        * sua conversão p/ conjunto é necessária, pois é preciso coletar os números que não vieram \n

        ===== ones_to_receive_zero ===== \n
        * possui todos os números que "self.game" não possui (fora do jogo) \n

        ===== ones_inside_game ===== \n
        * junção de "self.game" + "array_of_ones" (o que é possível por terem a mesma qtd. de índices) \n

        ===== ones_outside_game ===== \n
        * junção de "self.game" + "array_of_zeros" (o que é possível por terem a mesma qtd. de índices) \n
        * essa var será mesclada a "ones_inside_game" (ver # Junção) \n

        ===== tuples_ordered ===== \n
        * "ones_outside_game" passa a ser parte integrante de "ones_inside_game", deixando os dados desordenados \n
        * essa var organiza os números em ordem crescente, pois eles precisam estar na sua posição original \n
        * ex: tuples_ordered = [[1, 1], [2, 0], [3, 0], [4, 1], [5, 1]] \n

        ===== binary_result ===== \n
        * anexa todos os índices aninhados [1] de "tuples_ordered" \n
        * usando o exemplo acima, binary_result = [1, 0, 0, 1, 1] \n
        * esse procedimento é feito em todas as linhas, gerando 25 índices de 0 e 1 \n

        ===== binary_group_int ===== \n
        * var que desmembra os índices de "binary_result" em grupos de 5 (5 x 5 = 25 números) \n
        * o objetivo disso é ter as 5 linhas de forma binária e saber se alguma deles é repetida \n
        * todas as vars binárias "binary_group_int" são inseridas em "row_code" \n

        ===== row_code ===== \n
        * conjunto que recebe 5 strings binárias (se nenhuma delas for igual) \n
        * caso haja igualdade, apenas uma das duas é anexada a esta var, causando uma perda de tamanho \n
        * essa perda de tamanho é o fator essencial p/ saber se o jogo possui linhas de padrão repetido \n
        * portanto: "row_code" tendo tamanho 5, todas as linhas têm padrão diferente: jogo válido
        """

        array_of_ones = []
        arrays_of_zeros = []
        [array_of_ones.append(1) for n in range(15)]
        [arrays_of_zeros.append(0) for n in range(10)]

        all_numbers = set(range(1, 26))
        ones_to_receive_1 = set(self.game)
        ones_to_receive_zero = all_numbers.difference(ones_to_receive_1)

        ones_inside_game = list(zip(self.game, array_of_ones))
        ones_outside_game = list(zip(ones_to_receive_zero, arrays_of_zeros))

        # Junção: [(número de "self.game", 1), (número fora de "self.game", 0), ...]
        for outsider in ones_outside_game:
            ones_inside_game.append(outsider)

        tuples_ordered = sorted(ones_inside_game, key=lambda index_1st: index_1st[0])

        binary_result = [index[1] for index in tuples_ordered]

        binary_group_1 = "".join([str(index) for index in binary_result[0:5]])
        binary_group_2 = "".join([str(index) for index in binary_result[5:10]])
        binary_group_3 = "".join([str(index) for index in binary_result[10:15]])
        binary_group_4 = "".join([str(index) for index in binary_result[15:20]])
        binary_group_5 = "".join([str(index) for index in binary_result[20:25]])

        row_code = [binary_group_1, binary_group_2, binary_group_3, binary_group_4, binary_group_5]
        row_code_as_set = set(row_code)

        if len(row_code_as_set) == 5:
            return {'ok': True, 'set': row_code_as_set, 'report': len(row_code_as_set)}
        return {'ok': False, 'set': row_code_as_set, 'report': len(row_code_as_set)}

    # g_a
    def column_repetition(self) -> dict:
        """
        ===== Mais informações ===== \n
        * consultas/colunas_repetidas.py \n

        ===== Testes da função ===== \n
        * testes/testes.py/test_column_repetition \n

        ===== array_of_ones ===== \n
        * array com 15 índices 1, onde "1" é a representação de números que foram chamados no jogo \n

        ===== array_of_zeros ===== \n
        * array com 10 índices 0, onde "0" é a representação de números que não foram chamados no jogo \n

        ===== ones_to_receive_1 ===== \n
        * possui todos os índices de "self.game" \n
        * sua conversão p/ conjunto é necessária, pois é preciso coletar os números que não vieram \n

        ===== ones_to_receive_zero ===== \n
        * possui todos os números que "self.game" não possui (fora do jogo) \n

        ===== ones_inside_game ===== \n
        * junção de "self.game" + "array_of_ones" (o que é possível por terem a mesma qtd. de índices) \n

        ===== ones_outside_game ===== \n
        * junção de "self.game" + "array_of_zeros" (o que é possível por terem a mesma qtd. de índices) \n
        * essa var será mesclada a "ones_inside_game" (ver # Junção) \n

        ===== tuples_ordered ===== \n
        * "ones_outside_game" passa a ser parte integrante de "ones_inside_game", deixando os dados desordenados \n
        * essa var organiza os números em ordem crescente, pois eles precisam estar na sua posição original \n
        * ex: tuples_ordered = [[1, 1], [6, 0], [11, 0], [16, 1], [21, 1]] \n

        ===== binary_result ===== \n
        * anexa todos os índices aninhados [1] de "tuples_ordered" \n
        * usando o exemplo acima, binary_result = [1, 0, 0, 1, 1] \n
        * esse procedimento é feito em todas as colunas, gerando 25 índices de 0 e 1 \n

        ===== binary_group_int ===== \n
        * var que desmembra os índices de "binary_result" em grupos de 5 (5 x 5 = 25 números) \n
        * o objetivo disso é ter as 5 colunas de forma binária e saber se alguma delas é repetida \n
        * todas as vars binárias "binary_group_int" são inseridas em "column_code" \n

        ===== column_code ===== \n
        * conjunto que recebe 5 strings binárias (se nenhuma delas for igual) \n
        * caso haja igualdade, apenas uma das duas é anexada a esta var, causando uma perda de tamanho \n
        * essa perda de tamanho é o fator essencial p/ saber se o jogo possui colunas de padrão repetido \n
        * portanto: "column_code" tendo tamanho 5, todas as colunas têm padrão diferente: jogo válido
        """

        array_of_ones = []
        arrays_of_zeros = []
        [array_of_ones.append(1) for n in range(15)]
        [arrays_of_zeros.append(0) for n in range(10)]

        all_numbers = set(range(1, 26))
        ones_to_receive_1 = set(self.game)
        ones_to_receive_zero = all_numbers.difference(ones_to_receive_1)

        ones_inside_game = list(zip(self.game, array_of_ones))
        ones_outside_game = list(zip(ones_to_receive_zero, arrays_of_zeros))

        # Junção
        for tuple_element in ones_outside_game:
            ones_inside_game.append(tuple_element)

        tuples_ordered = sorted(ones_inside_game, key=lambda index_1st: index_1st[0])

        # O nome da variável foi modificada apenas p/ caber na linha abaixo
        x = tuples_ordered

        binary_group_1 = tuple([x[0][1], x[5][1], x[10][1], x[15][1], x[20][1]])
        binary_group_2 = tuple([x[1][1], x[6][1], x[11][1], x[16][1], x[21][1]])
        binary_group_3 = tuple([x[2][1], x[7][1], x[12][1], x[17][1], x[22][1]])
        binary_group_4 = tuple([x[3][1], x[8][1], x[13][1], x[18][1], x[23][1]])
        binary_group_5 = tuple([x[4][1], x[9][1], x[14][1], x[19][1], x[24][1]])

        # Para não ficar código repetido
        del tuples_ordered

        column_code = [binary_group_1, binary_group_2, binary_group_3, binary_group_4, binary_group_5]
        column_code_as_set = set(column_code)

        if len(column_code_as_set) == 5:
            return {'ok': True, 'set': column_code_as_set, 'report': len(column_code_as_set)}
        return {'ok': False, 'set': column_code_as_set, 'report': len(column_code_as_set)}

    # h_a
    def avoid_long_sequences(self, reference: list, first_index=0, second_index=1) -> dict:
        """
        ===== Mais informações ===== \n
        * consultas/numeros_seguidos_v2_poo.py \n

        ===== Teste da função ===== \n
        * testes/testes.py/test_avoid_long_sequences \n

        ===== integer_list ===== \n
        * recebe a subtração do índice posterior pelo índice anterior de "self.game" \n
        * (índice 1 - índice 0)...(índice 2 - índice 1)...(índice 3 - índice 2)... \n

        ===== answer ===== \n
        * itera sob todos os índices de "integer_list" (que são inteiros) e os converte em strings específicas \n
        * se o índice for 0, ele se torna 'y', se for acima de zero, ele se torna 'n' \n
        * 'y' = número seguido ao outro -> 'n' = salto entre números \n
        * self.game = [2, 4, 5, 7, 9, 12, 13, 14, 15, 16, 18, 19, 21, 22, 25] \n
        * ex: answer = ['n', 'y', 'n', 'n', 'n', 'y', 'y', 'y', 'y', 'n', 'y', 'n', 'y', 'n'] \n

        ===== answer_code ===== \n
        * conversão do array "answer" em uma string \n
        * ex: answer_code = nynnnyyyynynyn (conversão de "answer" acima) \n

        ===== reference ===== \n
        * var fonte que filtra as piores sequências de 'y' e 'n' de todos os jogos do banco \n
        * ex: reference = ['yyyyyyyyyy', 'yyyyyyyyy', 'yyyyyyy', 'yyyyyy', 'yyyyyyyy'] = [11, 10, 8, 7, 9] \n
        * essa var é comparada com "answer_code", e se ela for achada em "answer_code": jogo inválido \n
        * pela lógica do exemplo, dentro de "answer_code", não deve haver nenhum dos índices em "reference" \n

        ===== report ===== \n
        * a cada índice em "reference" não encontrado, "report" recebe "True", se ele receber "False": jogo inválido
        """

        integer_list = []
        answer = []

        while second_index < len(self.game):
            integer_list.append((self.game[second_index] - self.game[first_index]) - 1)
            first_index += 1
            second_index += 1

        [answer.append('y') if integer == 0 else answer.append('n') for integer in integer_list]

        answer_code = "".join(answer)

        report = []
        for code in reference:
            if code not in answer_code: report.append(True)
            else: report.append(False)

        if False in report:
            return {'ok': False, 'calculus': integer_list, 'report': answer_code, 'proof': report}
        return {'ok': True, 'calculus': integer_list, 'report': answer_code, 'proof': report}

    # i_a
    def game_type(self, reference) -> dict:
        """
        ===== Mais informações ===== \n
        * consultas/tipo_de_jogo_v2_poo.py \n

        ===== Teste ===== \n
        * testes/testes.py/test_game_type \n

        ===== upper ===== \n
        * var incrementadora quando "self.game" possui um dos números da parte de cima do volante \n

        ===== lower ===== \n
        * var incrementadora quando "self.game" possui um dos números da parte de baixo do volante \n

        ===== loop ===== \n
        * sintaxe usada p/ fazer a detecção e incrementação das vars "upper" e "lower" \n

        ===== game_class ===== \n
        * string que representa respectivamente as quantidades: números de cima (1 ao 15)/números de baixo (16/25) \n

        ===== reference ===== \n
        * var fonte que filtra as strings de sequências de tipo de jogo mais comuns (acima de 10% de frequência) \n

        ===== condição final ===== \n
        * se o tipo de jogo de "self.game" estiver em "reference": jogo válido
        """

        upper, lower, upper_area, lower_area = 0, 0, tuple(range(1, 16)), tuple(range(16, 26))

        for number in self.game:
            if number in upper_area: upper += 1
            elif number in lower_area: lower += 1

        game_class = f"{upper}/{lower}"

        if game_class in reference:
            return {'ok': True, 'report': game_class}
        return {'ok': False, 'report': game_class}

    # j_a
    @staticmethod
    def prime_numbers_counter(target_game, references) -> dict:
        """
        ===== Mais informações ===== \n
        * estatistica/contar_numeros_primos_v2_poo.py \n

        ===== Teste da função ===== \n
        * testes/testes.py/test_prime_numbers_counter \n

        ===== prime_numbers_box ===== \n
        * var container p/ os números primos achados do parâmetro "target_game" (jogo criado) \n

        ===== array_size ===== \n
        * tamanho do array "prime_numbers_box" \n

        ===== target_game ===== \n
        * var que se faz necessário, pois essa é uma função de comparação (se não fosse, usaria apenas "self.game") \n

        ===== references ===== \n
        * ex: reference[0] = [5, 6, 4, 7] \n
        * contêm dois arrays, mas o índice [1] passou a ser desconsiderado \n
        * seu índice [0] é um array que contêm os índices que representam as qtds. mais comuns de números primos \n

        ===== condição final ===== \n
        * se o tamanho de "array_size" estiver dentro de "references[0]": jogo válido \n
        * ex: prime_numbers_box = [5, 7, 13, 23] -> array_size = 4 -> está dentro de references[0]
        """

        prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23]
        prime_numbers_box = []

        for number in target_game:
            if number in prime_numbers:
                prime_numbers_box.append(number)

        array_size = len(prime_numbers_box)

        if array_size in references[0]:
            return {'ok': True, 'report': f'{prime_numbers_box} [ {array_size} número(s) ]', 'array': prime_numbers_box}
        return {'ok': False, 'report': f'{prime_numbers_box} [ {array_size} número(s) ]', 'array': prime_numbers_box}

    # k_a
    def score_admin(self,
                    single_score: bool,
                    score: int,
                    has_comparison=False,
                    operator='equals',
                    repeated=0
                    ) -> [int, str]:
        """
        ===== Mais informações ===== \n
        * consultas/pontuacao.py \n

        ===== Teste da função ===== \n
        * testes/test_score_admin \n

        ===== similarities ===== \n
        * var container do tamanho de cada uma das interseções de "self.game" em relação a todos os jogos \n

        ===== precisions ===== \n
        * var container que filtra de "similarities" a contagem de todas as qtds. separadamente \n
        * ex: similarities = [6, 9, 11, 9] -> precisions = [.count(6), .count(9), .count(11)] -> [1, 2, 1] \n

        ===== score_panel ===== \n
        * desempacotamento de "precisions", exibindo todas as similaridades de "self.game" \n

        ===== scores ===== \n
        * var relatório das contagens de cada pontuação (6: qtd. int., ...15: qtd. int) \n
        * só é criada se "single_score" = True (desejado saber uma quantidade específica) \n

        ===== single_score ===== \n
        * parâmetro usável quando se quer saber a qtd. de uma pontuação específica do relatório de "scores" \n

        ===== score ===== \n
        * parâmetro que representa a pontuação desejada p/ consultar em "self.game" em relação a todos os jogos \n
        * ex: score = 13 (quantas vezes "self.game" fez 13 pontos no total) \n
        * esse valor é usado para ser procurado em "scores" \n

        ===== box_with_score ===== \n
        * var de captura que usa o parâmetro "score" como chave para pegar o valor da chave em "scores" \n
        * ex: score = 13 -> scores = {13: 1072} -> box_with_score = [1072] \n

        ===== score_found ===== \n
        * var que acessa o índice único de "box_with_score" \n

        ===== has_comparison ===== \n
        * parâmetro p/ dizer se é desejado saber uma pontuação especifica de "self.game" em relação a todos os jogos \n

        ===== correct & incorrect ===== \n
        * resultado obtido pela consulta função \n

        ===== operator ===== \n
        * parâmetro que define a hierarquia que "repeated" deve seguir \n
        * ex: score = 13 -> operator = 'greater' -> repeated = 2 (jogo deve ter feito 13 pontos mais de 2 vezes) \n

        ===== repeated ===== \n
        * parâmetro que representa quantas vezes o parâmetro "score" deve ter em qtd.
        """

        similarities = []

        for i in range(len(self.database)):
            game_main_as_set = set(self.game)
            game_comparared_as_set = set(self.database[i])
            similarity_target_game_vs_db_game = len(game_main_as_set.intersection(game_comparared_as_set))
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

        if single_score:
            scores = {
                6: precisions[0], 7: precisions[1], 8: precisions[2], 9: precisions[3], 10: precisions[4],
                11: precisions[5], 12: precisions[6], 13: precisions[7], 14: precisions[8], 15: precisions[9],
            }

            box_with_score = []
            [box_with_score.append(scores[key]) for key in scores if score == key]

            score_found = box_with_score[0]
            correct = {'ok': True, 'banner': score_panel, 'report': score_found}
            incorrect = {'ok': False, 'banner': score_panel, 'report': score_found}

            if has_comparison and operator == 'equals':
                if box_with_score[0] == repeated:
                    return correct
                return incorrect
            if has_comparison and operator == 'greater':
                if box_with_score[0] > repeated:
                    return correct
                return incorrect
            if has_comparison and operator == 'lesser':
                if box_with_score[0] < repeated:
                    return correct
                return incorrect

            if not has_comparison:
                return box_with_score[0]

        else:
            return score_panel

    # l_a
    def numbers_frequency(self, references) -> dict:
        """
        ===== Mais informações ===== \n
        * estatistica/frequencia_numeros_poo.py \n

        ===== Testes da função ===== \n
        * testes/testes.py/test_numbers_frequency \n

        ===== references[0] ===== \n
        * conjunto de números que possuem frequência acima de 60% do total de jogos da Lotofácil \n
        * seu tamanho muda conforme novos jogos vão sendo lançados, pois as porcentagens mudam com eles \n
        * ele é comparado com "self.game" (jogo criado pelo algoritmo) \n
        * o objetivo é detectar quantos números de "self.game" estão entre os que vêm acima de 60% \n
        * a análise é guardada em "similatiry" (em dados) e contada em "similarity_amount" \n

        ===== similarity (set) ===== \n
        * resultado da comparação entre "self.game" e os números mais comuns do Lotofácil

        ===== similarity_amount (int) ===== \n
        * conversão dos dados de "similarity" p/ um dado numérico \n

        ===== references[1] ===== \n
        * apesar de haver muitos números com frequência acima de 60%, todos não virão de uma vez \n
        * foi especulado algo entre 40% a 70%, que é uma margem lógica aceitável \n
        * ela está diretamente conectada a "references[0]" \n
        * suas chaves são ['40%'] e ['70%'], que são o cálculos representantes do tamanho de "references[0]" \n
        * ex: "len(references[0]) = 10" -> "references[1]['40%'] = 4" -> "references[1]['70%'] = 7" \n
        * essas chaves são os valores que determinam o "range" permitido de números mais comuns (aqui: 4 a 7) \n
        * "references[0]" é alterável, o que afeta diretamente "references[1]" \n
        * razões que alteram? novos jogos lançados, outros números podem alcançar 60%+ de frequência \n

        ===== Condição final ====== \n
        * se os números de "self.game" não respeitarem a margem de 40% a 70%: jogo inválido
        """

        similarity = set(self.game).intersection(set(references[0]))
        similarity_amount = len(similarity)

        if references[1]['40%'] <= similarity_amount <= references[1]['70%']:
            return {'ok': True, 'report': similarity}
        return {'ok': False, 'report': similarity}

    # m_a
    def ten_last_comparison(self, reference) -> dict:
        """
        ===== Teste de função ===== \n
        * testes/testes.py/test_ten_last_comparison \n

        ===== bad_codes ===== \n
        * sequências de interseções ruins (que são muitos seguidas) \n

        ===== exceeding_patterns ===== \n
        * var que age sob "bad_codes" p/ confirmar com booleanos \n

        ===== bad_combinations ===== \n
        * sequências de interseções improváveis (que são muito lineares/padronizadas) \n

        ===== stupid_patterns ===== \n
        * var que age sob "bad_combinations" p/ confirmar com booleanos \n

        ===== too_similar ===== \n
        * var que procura interseções de 11 frequentes (definido: 2) entre "self.game" em relação aos 10 últimos jogos
        * se isso acontecer, o valor booleano dessa var é alterada e o jogo é invalidado (ver análise [1])

        ===== result ===== \n
        * guarda todas as interseções (convertidas em inteiro) entre "self.game" e os 10 últimos jogos \n

        ===== intersection_code ===== \n
        * string do resultado de todas as similaridades (ex: result = [6, 10, 11, 8]) (ex: intersection_code = 610118)
        * esse código é comparado com cada índice de "bad_code" e "bad_combinations"
        * se esse código for achado nestas vars, o jogo é invalidado (ver análise [2]) (ver análise [3]) \n

        ===== conditions ===== \n
        * Carrega todas as condições requisito p/ "self.game" passar pelos critérios da função \n
        * 1: Similaridades de 5 a 7 ausentes (muito distantes) \n
        * 2: Similaridades de 13 a 15 ausentes (muito próximas) \n
        * 3: Similaridades de 8 a 11 presentes (muito comuns) \n
        * 4: Similaridade de "self.game" em relação ao último jogo deve estar entre 8 a 10 \n
        * 5: A similaridades dos dois últimos jogos devem ser diferentes \n
        * 6: As similaridades não se repetem muitas vezes seguidas (não mais do que 2) \n
        * 7: Não há sequências crescentes e decrescentes de interseções \n
        * 8: Não há mais do que duas similaridades de 11 entre "self.game" e os 10 últimos jogos \n
        """

        bad_codes = ('888', '8888', '88888', '999', '9999', '99999', '101010', '10101010', '1010101010')
        exceeding_patterns = []

        bad_combinations = (
            '891011', '111098', '8910', '91011', '11109', '1098',
            '8989', '810810', '811811',
            '9898', '910910', '911911',
            '108108', '109109', '10111011',
            '118118', '119119', '11101110',
        )
        stupid_patterns = []

        too_similar = False

        result = []
        for index, game in enumerate(reference):
            result.append(len(set(game).intersection(set(self.game))))

        intersection_code = "".join([str(index) for index in result])

        # Análise [1]: Condição satisfeita: jogo invalidado
        if result.count(11) > 2: too_similar = True

        # Análise [2]: else satisfeito, jogo invalidado
        for code in bad_codes:
            if code not in intersection_code: exceeding_patterns.append(False)
            else: exceeding_patterns.append(True)

        # Análise [3]: else satisfeito, jogo invalidado
        for code in bad_combinations:
            if code not in intersection_code: stupid_patterns.append(False)
            else: stupid_patterns.append(True)

        # Todas as condições em "conditions" devem ser "True", ou seja, não deve haver "False" anexado a "box"
        box = []
        before_last_game = result[-2]
        last_game = result[-1]
        very_similar_range = range(11, 16)
        very_different_range = 7
        conditions = {
            1: box.append(True) if 5 not in result and 6 not in result and 7 not in result else box.append(False),
            2: box.append(True) if 12 not in result and 13 not in result and 14 not in result and 15 not in result else box.append(False),
            3: box.append(True) if 8 in result and 9 in result and 10 in result and 11 in result else box.append(False),
            4: box.append(True) if last_game not in very_similar_range and last_game != very_different_range else box.append(False),
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
        ===== Mais informações ====== \n
        * estatistica/grupos_de_numeros_poo.py \n

        ===== Teste da função ===== \n
        * testes/testes.py/test_three_in_a_row_counter \n

        ===== rows ===== \n
        * armazena arrays com todas as combinações possíveis de 3 números seguidos (23 combinações) \n
        * ex: [1, 2, 3] [2, 3, 4]...[23, 24, 25] \n

        ===== game_cells ===== \n
        * armazena o jogo criado em partes fragmentas em índices de 3 \n
        * ex: (1, 4, 5, 7, 8, 10, 12, 13, 14, 15, 17, 21, 22, 23, 24) \n
        * game_cells = [[1, 4, 5], [4, 5, 7], [5, 7, 8]...[22, 23, 24]] \n

        ===== three_in_a_row_sequence ===== \n
        * var contadora das quantidades encontradas dos grupos de 3 números seguidos \n
        * cada índice array de "game_cells" (jogo) é procurado em "rows" (todos os números do jogo) \n
        * se for encontrado, esta var é incrementada a cada sequência achada \n
        * em quase todos os jogos, sempre saem sequências de 3 números seguidos \n
        * no período deste projeto, as quantidades mais comuns são: 4, 5, 3, 6 \n
        * isso significa que dentre todos os jogos, é mais comum ter 3, 4, 5 ou 6 grupos de 3 números seguidos \n
        * [4, 5, 3, 6] são as qtds. com recorrência acima de 10%, enquanto as outras estão abaixo disso \n
        * portanto, esta var deve ser um inteiro entre [4, 5, 3, 6], senão: jogo inválido \n

        ===== reference ===== \n
        * var fonte que trás o tamanho do array com as sequências de grupos de 3 seguidos mais comuns \n
        * essa var é a referência onde o valor de "three_in_a_row_sequence" deve estar contido \n

        ===== Condição final ===== \n
        * Se a qtd. de grupos de 3 números seguidos em "self.game" estiver contido em "reference": jogo válido
        """

        rows = []
        i, i2, i3 = 1, 2, 3
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

        if three_in_a_row_sequence in reference:
            return {'ok': True, 'report': three_in_a_row_sequence}
        return {'ok': False, 'report': three_in_a_row_sequence}

    # o_a
    @staticmethod
    def get_border_or_center_size(target_game, site, references):
        """
        ===== Mais informações ===== \n
        * estatistica/borda_centro_poo.py \n

        ===== Teste da função ===== \n
        * testes/testes.py/test_get_border_or_center_size \n

        ===== card_edges ===== \n
        * anexa os números de borda encontrados em cada índice de "self.game" \n
        * no loop 1, cada índice do jogo é verificado via "target_game" e este array recebe os números de borda

        ===== card_center ===== \n
        * anexa os números de centro encontrados em cada índice de "self.game" \n
        * no loop 2, cada índice do jogo é verificado via "target_game" e este array recebe os números de centro \n

        ===== target_game ===== \n
        * parâmetro que representa o jogo analizado \n
        * essa é uma função de comparação, o que significa que não apenas "self.game" será usado \n

        ===== edge_amount ===== \n
        * var contadora da qtd. de índices em "card_edges" (qtd. de números de borda) \n

        ===== center_amount ===== \n
        * var contadora da qtd. de índices em "card_center" (qtd. de números de centro) \n

        ===== site (str) ===== \n
        * parâmetro que indica qual orientação usar: borda ou centro \n

        ===== references[0] ====== \n
        * var container p/ a qtd. de números de borda mais recorrentes (freq. de 10%+) \n

        ===== references[1] ====== \n
        * var container p/ a qtd. de números de centro mais recorrentes (freq. de 10%) \n

        ===== Condição final ===== \n
        * se as qtds. de números de borda (edge_amount) ou centro (center_amount) estiverem em "reference": jogo válido
        """

        card_edges = []
        card_center = []

        for n in list(target_game):
            if n == 1 or n == 2 or n == 3 or n == 4 or n == 5 or \
             n == 10 or n == 15 or n == 20 or n == 25 or \
             n == 24 or n == 23 or n == 22 or n == 21 or \
             n == 16 or n == 11 or n == 6:
                card_edges.append(n)

        for n in list(target_game):
            if n == 7 or n == 8 or n == 9 or n == 12 or n == 13 or n == 14 or n == 17 or n == 18 or n == 19:
                card_center.append(n)

        edge_amount = len(card_edges)
        if site == 'edges':
            if edge_amount in references[0]:
                return {'ok': True, 'report': edge_amount, 'array': card_edges}
            return {'ok': False, 'report': edge_amount, 'array': card_edges}

        center_amount = len(card_center)
        if site == 'center':
            if center_amount in references[1]:
                return {'ok': True, 'report': center_amount, 'array': card_center}
            return {'ok': False, 'report': center_amount, 'array': card_center}

    # q_a
    @staticmethod
    def horizontal_code(reference, target_game):
        """
        ===== Mais informações ===== \n
        * estatistica/grupos_horizontais_poo.py \n

        ===== Teste da função ===== \n
        * testes/testes.py/test_horizontal_code \n

        ===== rows ===== \n
        * var container com chaves que têm valores incrementáveis com base nos índices do parâmetro "target_game" \n

        ===== loop ===== \n
        * onde as chaves de "rows" são incrementadas, cada índice de "target_game" é encontrado em um range \n

        ===== game_code_tuple ===== \n
        * var com todas chaves de "rows" (5 números inteiros) = qtd. de números por linha do jogo \n

        ===== game_code_str ===== \n
        * var conversora de todos os inteiros em "game_code_tuple" para string, e em seguida mescladas como string \n
        * ex: game_code_tuple = (4, 3, 3, 2, 3) -> game_code_str = "".join(('4', '3', '3', '2', '3')) ... '43323' \n

        ===== reference ===== \n
        * var fonte que armazena os grupos horizontais mais comuns dentre todos os jogos da Lotofácil (freq. 1% +) \n
        * como há muitas combinações, muitas já sairam, e foram filtradas somente aquelas com mais de 1% \n

        ===== condição final ===== \n
        * se "game_code_str" estiver dentre os índices de "reference": jogo válido
        """

        rows = {'1st': 0, '2nd': 0, '3rd': 0, '4th': 0, '5th': 0}

        for number in target_game:
            if number in range(1, 6): rows['1st'] += 1
            elif number in range(6, 11): rows['2nd'] += 1
            elif number in range(11, 16): rows['3rd'] += 1
            elif number in range(16, 21): rows['4th'] += 1
            elif number in range(21, 26): rows['5th'] += 1

        game_code_tuple = tuple(rows.values())

        game_code_str = "".join([str(int_index) for int_index in game_code_tuple])

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
        """
        ===== Mais informações ===== \n
        * estatistica/grupos_verticais_poo.py \n

        ===== Teste da função ===== \n
        * testes/testes.py/test_vertical_code \n

        ===== columns ===== \n
        * dicionário com chave contendo todos os 25 números possíveis, quebrados em forma de coluna \n
        * dicionário com chave contendo valores incrementáveis com base nos índices encontrados em "target_game" \n

        ===== target_game ===== \n
        * var do jogo criado, onde cada índice dessa tupla é procurada em todas as chaves "sequence" de "columns" \n

        ===== loop ===== \n
        * forma de gerar a interação especificada em "target_game" \n
        * cada "number" do loop é um índice do jogo, que é comparado com todas as chaves "sequence" de "columns" \n

        ===== game_code_tuple ===== \n
        * var com todas chaves "countage" de "columns" (5 números inteiros) = qtd. de números por coluna do jogo \n

        ===== game_code_str ===== \n
        * var conversora de todos os inteiros em "game_code_tuple" para string, e em seguida mescladas como string \n
        * ex: game_code_tuple = (4, 3, 3, 2, 3) -> game_code_str = "".join(('4', '3', '3', '2', '3')) ... '43323' \n

        ===== reference ===== \n
        * var fonte que armazena os grupos verticais mais comuns dentre todos os jogos da Lotofácil (freq. 1% +) \n
        * como há muitas combinações, muitas já sairam, e foram filtradas somente aquelas com mais de 1% \n

        ===== condição final ===== \n
        * se "game_code_str" estiver dentre os índices de "reference": jogo válido
        """

        columns = {
            '1st': {'sequence': [1, 6, 11, 16, 21], 'countage': 0},
            '2nd': {'sequence': [2, 7, 12, 17, 22], 'countage': 0},
            '3rd': {'sequence': [3, 8, 13, 18, 23], 'countage': 0},
            '4th': {'sequence': [4, 9, 14, 19, 24], 'countage': 0},
            '5th': {'sequence': [5, 10, 15, 20, 25], 'countage': 0}
        }

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

        game_code_tuple = (
            columns['1st']['countage'], columns['2nd']['countage'], columns['3rd']['countage'],
            columns['4th']['countage'], columns['5th']['countage']
        )

        game_code_str = "".join([str(int_index) for int_index in game_code_tuple])

        if game_code_str in reference:
            return {
                'ok': True,
                'report': game_code_str,
                'full_report': f'{game_code_str} [{reference.index(game_code_str)}]'
            }
        return {'ok': False, 'report': game_code_str, 'full_report': f' {game_code_str} [inexistente]'}

    # s_a
    def middle_number(self, reference: list) -> dict:
        middle_number = self.game[7]
        if middle_number in reference:
            return {'ok': True, 'report': middle_number}
        return {'ok': False, 'report': middle_number}

    # Não está sendo usado
    def divisible_3(self, reference: list) -> dict:
        box = []
        for number in self.game:
            if not number % 3:
                box.append(number)

        string_code = "".join([str(index) for index in box])
        if string_code in reference:
            return {'ok': True, 'report': f'{string_code} {box}'}
        return {'ok': False, 'report': f'{string_code} {box}'}

    # Não está sendo usado
    def mean_first_15_numbers(self, reference: list) -> dict:
        upper = []
        for number in self.game:
            if number in range(1, 16):
                upper.append(number)
        mean_calculus = f'{sum(upper) / len(upper):.1f}'

        if mean_calculus in reference:
            return {'ok': True, 'report': mean_calculus}
        return {'ok': False, 'report': mean_calculus}

    # Não está sendo usado
    def has_most_frequent_recent_numbers(self, reference: dict) -> dict:
        game_as_set = set(self.game)
        reference_common_numbers = set(reference)
        similarity = set(game_as_set).intersection(set(reference_common_numbers))
        similarity_length = len(similarity)

        if reference['40%'] <= similarity_length <= reference['70%']:
            return {'ok': True, 'report': similarity}
        return {'ok': False, 'report': similarity}

    def game_numbers_position(self, references: list) -> dict:
        """
        Vamos tomar o valor abaixo como exemplo
        Ele representa o histórico de cada índice de cada jogo na história da Lotofácil
        Ex: '1st' representa os números mais comuns ao primeiro número dentre todos os jogos
        Ex: '2nd' representa os números mais comuns ao segundo número dentre todos os jogos
        E assim suscesivamente...
        references[0] = {
            '1st': [1, 2, 3],
            '2nd': [2, 3, 4],
            '3rd': [3, 4, 5, 6],
            '4th': [4, 5, 6, 7, 8],
            '5th': [6, 7, 8, 9, 10],
            '6th': [8, 9, 10, 11, 12],
            '7th': [9, 10, 11, 12, 13],
            '8th': [11, 12, 13, 14, 15],
            '9th': [13, 14, 15, 16, 17],
            '10th': [14, 15, 16, 17, 18],
            '11th': [16, 17, 18, 19, 20],
            '12th': [18, 19, 20, 21, 22],
            '13th': [20, 21, 22, 23],
            '14th': [22, 23, 24],
            '15th': [24, 25]
        }

        No loop for, é desejado saber se cada índice de "self.game" está dentro de cada um dos dados em "references[0]"
        Obviamente, para isso dar certo, "self.game" e "references[0]" possuem qtd. de índices equivalentes
        "references[0]" vêm a partir de "proper_numbers_by_position", criado em "estatistica/historico_numeros"
        Neste loop, cada índice de "self.game" é procurado em cada chave. O resultado do procura é inserido em "result"
        Se o índice em "self.game" é achado na chave correspondente: "result" recebe "True", senão, recebe "False"
        Para saber os erros, é contado quantos "False" foram anexados a "result", via "mistakes"
        Após se ter o resultado, "mistakes" é comparado a "tolerable_mistakes", criado em "estatistica/historico_numeros"
        "tolerable_mistakes" é a var em "references[1]"
        "tolerable_mistakes" contêm as qtds. de erros mais comuns (as >= a 10% foram consideradas)
        No tempo que essa função foi criada, as qtds. eram [0, 1, 2, 3], enquanto as outras não alcançaram 10%
        Porém, essa variável pode mudar conforme novos jogos vão acontecendo

        INTREPRETAÇÃO:
            "self.game", pela lógica, é aceitável se possuir: 15, 14, 13, 12 números dentro de "references[0]"
        """
        # Recebe uma sequência de "True" e "False" (15 no total)
        result = []

        # "reference" têm todas essas chaves, que estão na mesma qtd. de "self.game" (15)
        positions = [
            '1st', '2nd', '3rd', '4th', '5th',
            '6th', '7th', '8th', '9th', '10th',
            '11th', '12th', '13th', '14th', '15th'
        ]

        # Leia a documentação da função
        for index in range(len(self.game)):
            if self.game[index] in references[0][positions[index]]: result.append(True)
            else: result.append(False)

        # Leia a documentação da função
        mistakes = result.count(False)

        "CÓDIGO REMOVIDO"
        # suitable_percentage = 70
        # data_length = len(self.game)
        # percentage_70 = int((suitable_percentage * data_length) / 100)
        # max_mistakes = data_length - percentage_70

        if mistakes in references[1]:
            return {'ok': True, 'report': f'Erros cometidos: {mistakes}'}
        return {'ok': False, 'report': f'Erros cometidos: {mistakes}'}

    def verify_game_integrity(self) -> None:
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
            21: self.result.append(True) if self.game_history_numbers['ok'] else self.result.append(False)
        }

    def compare_game_with_last_game(self) -> None:
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
            else self.comparisons.append(False),
            5: self.comparisons.append(True) if self.last_game_prime_numbers['array'] != self.game_prime_numbers['array']
            else self.comparisons.append(False)
        }

    def build_game_data_report(self) -> None:
        different_border_assertion = ink('blue', str(self.comparisons[0]))
        different_center_assertion = ink('blue', str(self.comparisons[1]))
        different_horizontal_group_assertion = ink('blue', str(self.comparisons[2]))
        different_vertical_group_assertion = ink('blue', str(self.comparisons[3]))
        different_prime_numbers_assertion = ink('blue', str(self.comparisons[4]))

        new_game_data = {
            'edge_drawing': ink('green', str(self.game_edges['array'])),
            'edge_length': ink('green', str(self.game_edges['report'])),
            'center_drawing': ink('green', str(self.game_center['array'])),
            'center_length': ink('green', str(self.game_center['report'])),
            'horizontal_code_drawing': ink('green', str(self.game_horizontal_code['report'])),
            'vertical_code_drawing': ink('green', str(self.game_vertical_code['report'])),
            'prime_numbers': ink('green', str(self.game_prime_numbers['report']))
        }

        last_game_data = {
            'edge_drawing': ink('yellow', str(self.last_game_edge['array'])),
            'edge_length': ink('yellow', str(self.last_game_edge['report'])),
            'center_drawing': ink('yellow', str(self.last_game_center['array'])),
            'center_length': ink('yellow', str(self.last_game_center['report'])),
            'horizontal_code_drawing': ink('yellow', str(self.last_game_horizontal_code['report'])),
            'vertical_code_drawing': ink('yellow', str(self.last_game_vertical_code['report'])),
            'prime_numbers': ink('yellow', str(self.last_game_prime_numbers['report']))
        }

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
        |18| Há números de índice comuns ao histórico? || {self.result[20]} / {self.game_history_numbers['report']}

        =========== JOGO CRIADO vs ÚLTIMO JOGO ===========
        |1| Bordas diferente? [{different_border_assertion}]
        {self.label}
        {new_game_data['edge_drawing']} / {new_game_data['edge_length']}
        {last_game_data['edge_drawing']} / {new_game_data['edge_length']}

        |2| Centros diferente? [{different_center_assertion}]
        {self.label}
        {new_game_data['center_drawing']} / {new_game_data['center_length']}
        {last_game_data['center_drawing']} / {last_game_data['center_length']}

        |3| Grupo horizontal diferente? [{different_horizontal_group_assertion}]
        {self.label}
        {new_game_data['horizontal_code_drawing']} / {last_game_data['horizontal_code_drawing']}
        
        |4| Grupo vertical diferente? [{different_vertical_group_assertion}]
        {self.label}
        {new_game_data['vertical_code_drawing']} / {last_game_data['vertical_code_drawing']}
        
        |5| Números primos diferente? [{different_prime_numbers_assertion}]
        {self.label}
        {new_game_data['prime_numbers']} / {last_game_data['prime_numbers']}
        """

    def store_approved_game(self) -> None:
        Card.storage.append(self.game)

    def display_game_data_report(self) -> None:
        print(self.report)

    def display_proof(self) -> None:
        existing_conditions = len(self.result)
        satisfied_conditions = self.result.count(True)
        is_game_ok = "".join(["sim" if False not in self.result else "não"])

        report = f""" {self.indent}========== RELATÓRIO FINAL ==========
        CONDIÇÕES EXISTENTES  || {existing_conditions}
        CONDIÇÕES SATISFEITAS || {satisfied_conditions}
        JOGO APROVADO?        || {is_game_ok}
        PROVA                 || {self.result}
        TENTATIVAS            || {Card.attempts} vezes
        JOGOS CRIADOS         || {len(Card.storage)}"""

        print(report)
        for game in Card.storage:
            print(self.indent, game)

    def game_disqualified(self) -> None:
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

        try:
            # Inserido ao final do algoritmo, junto ao tratamento acima
            self.games_amount = int(input('Criar quantos jogos? (clique após a seta e digite) -------> '))

            # Para contar dados incrementáveis, é melhor criar uma "var de classe" ao invés de uma "var self"
            while len(Card.storage) < self.games_amount:

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
                    target_game=self.last_game,
                    reference=common_horizontal_thread_groups
                )

                self.last_game_vertical_code = self.vertical_code(
                    target_game=self.last_game,
                    reference=common_vertical_thread_groups
                )

                self.last_game_prime_numbers = self.prime_numbers_counter(
                    target_game=self.last_game,
                    references=[prime_numbers_amount_allowed, most_common_primes]
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
                    target_game=self.game,
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

                # -----> estatistica/historico_numeros.py
                # Jogo deve ter cada número de índice dentro dos mais comuns em suas respectivas posições
                self.game_history_numbers = self.game_numbers_position(
                    references=[proper_numbers_by_position, tolerable_mistakes]
                )

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
                    Card.attempts += 1
                    self.game_disqualified()

        except ValueError:
            print(self.game_horizontal_code)
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
