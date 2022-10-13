

"""
Os testes serão feitos pela classe "CardLoopLess" (explicação abaixo)

Porque criar duas classes iguais, uma com e outra sem loop?
  . Antes, tinhamos apenas a classe normal "Card" em "executavel/exe.py"
  . Esse classe possuia loop, parando somente quando fizesse o jogo com os padrões apropriados
  . Porém, ao adicionar esse loop, isso comprometeu o tempo de execução dos testes
  . Razão 1: Ter que passar e input e esperar o algoritmo criar um jogo apropriado
  . Razão 2: Após achar o jogo, ter que passar input novamente até o número de testes acabarem

  ========== SOLUÇÃO (aplicada) ==========
  Criar uma cópia do arquivo em "executavel/exe.py" com o nome "executavel/exe_loop.py"
  Em "executavel/exe.py", retirar a parte do loop e dos tratamentos "try & except" (servirá apenas como teste)
  Fazendo isso, os testes voltam a executar normalmente sem a interferência dos inputs e loops
  Porém, cada mudança feita em "executavel/exe_loop.py" deve ser replicada em "executavel/exe.py"

  ========== SOLUÇÃO 2 (não aplicada) ==========
  Criar um novo atributo de classe "test_enabled" que receberá um booleano
  Antes dos tratamentos, criar um "if" perguntando o valor de "test_enabled"
  Se True, passar a versão do código, excluindo os tratamentos, input e loop
  Se False, passar a versão do código, incluindo os tratamentos, input e loop
  Porque não foi aplicada?
      . Haveria muita repetição de código num documento só, então os arquivos foram separados
      . Mesmo assim, eles terão que se manter idênticos, com exceção dos tratamentos, input e loop
"""

from unittest import TestCase
from executavel.exe import CardLoopLess

from banco_de_dados.banco import dtb
from estatistica.primeiros_numeros import allowed_at_start
from estatistica.numeros_seguidos_v2 import impropers
from estatistica.tipo_de_jogo_v2 import game_types              # a_b


class CardLoopLessTest(TestCase):

    def setUp(self) -> None:
        self.obj = CardLoopLess(db=dtb, last_game=dtb[-1])

        self.games = {
            # test_sequence_horizontal
            'all_rows_filled': (1, 3, 5, 7, 9, 10, 11, 12, 13, 16, 17, 20, 23, 24, 25),
            'at_least_one_row_blank': (1, 2, 3, 4, 5, 11, 12, 13, 16, 17, 19, 22, 23, 24, 25),
            # test_sequence_vertical
            'all_columns_filled': (1, 2, 3, 6, 7, 10, 13, 14, 15, 18, 19, 20, 21, 22, 25),
            'at_least_one_column_blank': (2, 3, 4, 5, 7, 8, 9, 10, 12, 13, 14, 15, 17, 20, 23),
            # test_proper_gap
            'no_gaps': (1, 2, 3, 4, 5, 8, 10, 12, 14, 16, 18, 20, 21, 22, 23),
            '1_gap_3': (1, 2, 3, 7, 8, 10, 13, 15, 16, 17, 19, 21, 22, 23, 25),
            'starts_with_5': (5, 6, 7, 8, 9, 10, 14, 15, 18, 20, 21, 22, 23, 24, 25),
            'two_gaps': (1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 21, 23),
            # a_a: test_avoid_large_odd_even_sequence
            '4_odds_in_a_row': (1, 3, 5, 7, 8, 9, 10, 12, 13, 14, 16, 17, 18, 19, 20),
            '5_odds_in_a_row': (1, 3, 5, 7, 9, 10, 12, 13, 14, 16, 17, 18, 19, 20, 22),
            # test_row_repetition
            'no_repeated_row_pattern': (1, 2, 3, 7, 8, 9, 13, 14, 15, 16, 18, 20, 21, 24, 25),
            'repeat_row_pattern': (1, 2, 3, 6, 7, 10, 13, 14, 15, 18, 19, 20, 21, 22, 25),
            # test_column_repetition
            'no_repeated_column_pattern': (1, 2, 3, 6, 7, 8, 11, 12, 13, 14, 16, 18, 20, 21, 22),
            'repeated_column_pattern': (1, 2, 4, 5, 6, 7, 11, 12, 13, 14, 15, 16, 17, 21, 22),
            # test_avoid_long_sequences
            '5_in_a_row': (1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17),
            '6_in_a_row': (1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 15, 16, 17),
            '7_in_a_row': (1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 17),
            # a_b: test_game_type
            'proper_game_type': (1, 2, 3, 6, 7, 10, 13, 14, 15, 18, 19, 20, 21, 22, 25),
            'improper_game_type': (1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 17),
            # a_c: test_prime_numbers_counter
            'prime_numbers_len_ok': (1, 3, 5, 7, 9, 10, 11, 12, 13, 16, 17, 20, 23, 24, 25),
            'prime_numbers_len_not_ok': (1, 2, 3, 4, 5, 7, 11, 13, 17, 19, 20, 21, 22, 24, 25),
            # test_score_admin
            'standard_game': (1, 5, 7, 9, 10, 11, 13, 15, 16, 17, 20, 21, 22, 24, 25),
            'winner_game': (2, 3, 5, 6, 9, 10, 11, 13, 14, 16, 18, 20, 23, 24, 25),
            # test_numbers_frequency
            'has_more_than_40%_of_overall_commons': (1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 14, 15, 16, 17, 18),
            'has_less_than_40%_of_overall_commons': (1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 15, 16, 17, 18, 19),
            # test_ten_last_comparison
            'wrong_compared_game': (*tuple(range(1, 13)), 16, 17, 18),
            # a_e: test_three_in_a_row_counter
            '3_sequences_of_3_numbers_in_a_row': [1, 2, 3, 5, 7, 8, 10, 11, 12, 15, 16, 17, 20, 22, 23],
            '1_sequence_of_3_numbers_in_a_row': [1, 2, 3, 5, 7, 8, 10, 11, 13, 15, 16, 18, 20, 22, 23],
            # a_f: test_get_border_or_center_size
            'proper_numbers_in_border': (1, 2, 3, 4, 5, 7, 8, 9, 12, 13, 21, 22, 23, 24, 25),
            'improper_numbers_in_border': (1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 17, 18, 19),
            'proper_numbers_in_center': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16),
            'improper_numbers_in_center': (1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 17, 18, 19),
            # a_g: test_impropers_start_and_end
            'proper_start': tuple(range(1, 16)),
            'proper_end': tuple(range(1, 16)),
            'improper_start': (1, 3, 5, *tuple(range(6, 18))),
            'improper_end': (*tuple(range(1, 13)), 21, 23, 25),
        }

        # a_c
        self.prime_numbers_amount_allowed = [5, 6, 4, 7]
        self.most_common_primes = [11, 13, 5, 3]

        # a_d: consultas/frequencia_numeros
        self.most_frequent = [20, 10, 11, 25, 24, 13, 14, 5, 3, 4]
        self.percentages = {'40%': 4, '70%': 7}

        # a_e: consultas/grupos_de_numeros
        self.three_in_a_row_common = [4, 5, 3, 6]

        # a_f: consultas/borda_centro.py
        self.most_frequent_edges = [10, 9, 11, 8]
        self.most_frequent_centers = [5, 6, 4, 7]

    def test_sequence_horizontal(self):
        self.obj.game = self.games['all_rows_filled']
        self.assertEqual(self.obj.sequence_horizontal()['blank_free'], True)

        self.obj.game = self.games['at_least_one_row_blank']
        self.assertEqual(self.obj.sequence_horizontal()['blank_free'], False)

    def test_sequence_vertical(self):
        self.obj.game = self.games['all_columns_filled']
        self.assertEqual(self.obj.sequence_vertical()['blank_free'], True)

        self.obj.game = self.games['at_least_one_column_blank']
        self.assertEqual(self.obj.sequence_vertical()['blank_free'], False)

    def test_proper_gap(self):
        # Mudanças: "allowed_at_end" obsoleto (mantido aqui e no algoritmo por preguíça)
        self.obj.game = self.games['no_gaps']
        self.assertEqual(self.obj.proper_gap(reference=allowed_at_start)['is_proper'], True)

        # Jogo com 1 lacuna de 3
        self.obj.game = self.games['1_gap_3']
        self.assertEqual(self.obj.proper_gap(reference=allowed_at_start)['is_proper'], True)

        # Jogo que começa com 5
        self.obj.game = self.games['starts_with_5']
        self.assertEqual(self.obj.proper_gap(reference=allowed_at_start)['is_proper'], False)

        # Jogo com 1 lacuna de 3 e 4 (não passa pela lacuna de 4)
        self.obj.game = self.games['two_gaps']
        self.assertEqual(self.obj.proper_gap(reference=allowed_at_start)['is_proper'], False)

    # a_a
    # OBS: [PROBLEMA] parâmetro é variável, ou seja, o teste pode passar ou falhar com o passar do tempo
    # OBS: [SOLUÇÃO]  o parâmetro ganha um valor fixo apenas neste teste
    def test_avoid_large_odd_even_sequence(self):
        # Valor do parâmetro é dado como fixo para evitar o teste de falhar (seu valor atual)
        worst_sequences = [
            'pppp', 'iiiii', 'ppppp', 'iiiiii', 'pppppp', 'iiiiiii', 'ppppppp', 'iiiiiiii', 'pppppppp',
            'ppppppppp', 'pppppppppp', 'ppppppppppp', 'pppppppppppp', 'iiiiiiiii', 'iiiiiiiiii',
            'iiiiiiiiiii', 'iiiiiiiiiiii', 'iiiiiiiiiiiii'
        ]

        # Sequência de 4 ímpares seguidos (passa) (não está em "worst_sequence")
        self.obj.game = self.games['4_odds_in_a_row']
        self.assertEqual(self.obj.avoid_large_odd_even_sequence(reference=worst_sequences)['is_proper'], True)

        # Sequência de 5 ímpares seguidos (não passa) (está em "worst_sequences")
        self.obj.game = self.games['5_odds_in_a_row']
        self.assertEqual(self.obj.avoid_large_odd_even_sequence(reference=worst_sequences)['is_proper'], False)

    def test_row_repetition(self):
        # Jogo sem filas de padrão repetido
        self.obj.game = self.games['no_repeated_row_pattern']
        self.assertEqual(self.obj.row_repetition()['empty'], True)

        # Jogo com filas 3 e 4 com padrões repetidos
        self.obj.game = self.games['repeat_row_pattern']
        self.assertEqual(self.obj.row_repetition()['empty'], False)

    def test_column_repetition(self):
        # Jogo não possui colunas de padrão repetido
        self.obj.game = self.games['no_repeated_column_pattern']
        self.assertEqual(self.obj.column_repetition()['empty'], True)

        # Jogo possui colunas 1 e 2 com padrão idêntico
        self.obj.game = self.games['repeated_column_pattern']
        self.assertEqual(self.obj.column_repetition()['empty'], False)

    def test_avoid_long_sequences(self):
        # Jogo com o máximo de números seguidos (5)
        self.obj.game = self.games['5_in_a_row']
        self.assertEqual(self.obj.avoid_long_sequences(reference=impropers)['is_proper'], True)

        # Jogo com o máximo de números seguidos (6)
        self.obj.game = self.games['6_in_a_row']
        self.assertEqual(self.obj.avoid_long_sequences(reference=impropers)['is_proper'], True)

        # Jogo com números seguidos excedentes (7+)
        self.obj.game = self.games['7_in_a_row']
        self.assertEqual(self.obj.avoid_long_sequences(reference=impropers)['is_proper'], False)

    # a_b
    def test_game_type(self):
        # Jogo com tipo mais recorrente (passa) (está em "game_types")
        self.obj.game = self.games['proper_game_type']
        self.assertEqual(self.obj.game_type(reference=game_types)['is_proper'], True)

        # Jogo com tipo menos recorrente (não passa) (não está em "game_types")
        self.obj.game = self.games['improper_game_type']
        self.assertEqual(self.obj.game_type(reference=game_types)['is_proper'], False)

    # a_c
    # [PROBLEMA]: Os parâmetros são variáveis, podendo mudar conforme novos jogos são divulgados
    # [SOLUÇÃO]: Dar valores fixos aos parâmetros somente para este teste
    def test_prime_numbers_counter(self):
        # Jogo possui quantidade de primos apropriada
        self.obj.game = self.games['prime_numbers_len_ok']
        self.assertEqual(self.obj.prime_numbers_counter(
            references=[self.prime_numbers_amount_allowed, self.most_common_primes])['is_proper'], True)

        # Jogo não possui quantidade de primos apropriada
        self.obj.game = self.games['prime_numbers_len_not_ok']
        self.assertEqual(self.obj.prime_numbers_counter(
            references=[self.prime_numbers_amount_allowed, self.most_common_primes])['is_proper'], False)

    # [PROBLEMA]: com o passar do tempo, este jogo pode fazer 14/15 pontos e esse teste falhará
    # [SOLUÇÃO]:  executar o algoritmo e pegar outro jogo para substituir o primeiro "self.obj.game"
    def test_score_admin(self):
        # Jogo que ainda não fez 14 e 15 pontos (passa) (mas pode fazer, e se fizer: executar SOLUÇÃO)
        self.obj.game = self.games['standard_game']
        self.assertEqual(self.obj.score_admin(single_score=True, score=15, has_comparison=True)['is_proper'], True)
        self.assertEqual(self.obj.score_admin(single_score=True, score=14, has_comparison=True)['is_proper'], True)

        # Primeiro jogo da Lotofácil, já fez 15 pontos (não passa)
        self.obj.game = self.games['winner_game']
        self.assertEqual(self.obj.score_admin(single_score=True, score=15, has_comparison=True)['is_proper'], False)

    # a_d
    # OBS: [PROBLEMA] parâmetros são variáveis, ou seja, o teste pode passar ou falhar com o passar do tempo
    # OBS: [SOLUÇÃO]  os parâmetros ganham um valor fixo apenas neste teste
    def test_numbers_frequency(self):
        # Jogo possui 4 números da lista dos números mais frequentes
        self.obj.game = self.games['has_more_than_40%_of_overall_commons']
        self.assertEqual(
            self.obj.numbers_frequency(references=[self.most_frequent, self.percentages])['is_proper'], True
        )

        # Jogo possui 3 números da lista dos números mais frequentes (não passa) (permitido: 4 até 7)
        self.obj.game = self.games['has_less_than_40%_of_overall_commons']
        self.assertEqual(
            self.obj.numbers_frequency(references=[self.most_frequent, self.percentages])['is_proper'], False
        )

    # OBS: [PROBLEMA] parâmetro é variável, ou seja, o teste pode passar ou falhar com o passar do tempo
    # OBS: [SOLUÇÃO]  o parâmetro ganha um valor fixo apenas neste teste
    def test_ten_last_comparison(self):
        # É preciso de um jogo qualquer, simulando "self.game", a ser comparado com 10 outros
        self.obj.game = list(range(1, 16))

        # Parâmetro recebe valor fixo para que seja possível testar sem causar erros no teste
        # Os jogos abaixo satisfazem todas as condições da função testada
        # A ordem das interseções não podem ser crescentes nem decrescentes (8, 9, 10, 11) (11, 10, 9, 8)
        self.ten_last = [
            (*tuple(range(1, 9)), 16, 17, 18, 19, 20, 21, 22),  # 8
            (*tuple(range(1, 12)), 16, 17, 18, 19),             # 11
            (*tuple(range(1, 10)), 16, 17, 18, 19, 20, 21),     # 9
            (*tuple(range(1, 11)), 16, 17, 18, 19, 20),         # 10
            (*tuple(range(1, 9)), 16, 17, 18, 19, 20, 21, 22),  # 8
            (*tuple(range(1, 12)), 16, 17, 18, 19),             # 11
            (*tuple(range(1, 10)), 16, 17, 18, 19, 20, 21),     # 9
            (*tuple(range(1, 11)), 16, 17, 18, 19, 20),         # 10
            (*tuple(range(1, 9)), 16, 17, 18, 19, 20, 21, 22),  # 8
            (*tuple(range(1, 10)), 16, 17, 18, 19, 20, 21),     # 9
        ]

        self.assertEqual(self.obj.ten_last_comparison(reference=self.ten_last)['is_proper'], True)

        # O primeiro jogo é substituído por um com uma interseção fora das condições da função
        self.ten_last[0] = self.games['wrong_compared_game']

        # Para provar, mude o "par2=True" e veja o teste falhar
        self.assertEqual(self.obj.ten_last_comparison(reference=self.ten_last)['is_proper'], False)

    # a_e
    # OBS: [PROBLEMA] parâmetro é variável, ou seja, o teste pode passar ou falhar com o passar do tempo
    # OBS: [SOLUÇÃO]  o parâmetro ganha um valor fixo apenas neste teste
    def test_three_in_a_row_counter(self):
        # Jogo com 3 sequências de 3 números seguidos (permitidos: [3, 4, 5, 6])
        self.obj.game = self.games['3_sequences_of_3_numbers_in_a_row']
        self.assertEqual(self.obj.three_in_a_row_counter(reference=self.three_in_a_row_common)['is_proper'], True)

        # Jogo com 1 sequência de 3 números seguidos (não passa)
        self.obj.game = self.games['1_sequence_of_3_numbers_in_a_row']
        self.assertEqual(self.obj.three_in_a_row_counter(reference=self.three_in_a_row_common)['is_proper'], False)

    # a_f
    # OBS: [PROBLEMA] parâmetros são variáveis, ou seja, os testes pode passar ou falhar com o passar do tempo
    # OBS: [SOLUÇÃO]  os parâmetros ganham um valor fixo apenas neste teste
    def test_get_border_or_center_size(self):

        # Jogo com 10 números de borda (passa)
        self.assertEqual(
            self.obj.get_border_or_center_size(
                target_game=self.games['proper_numbers_in_border'],
                site='edges',
                references=[self.most_frequent_edges, self.most_frequent_centers]
            )['is_proper'], True
        )

        # Jogo com 6 números de borda (não passa)
        self.assertEqual(
            self.obj.get_border_or_center_size(
                target_game=self.games['improper_numbers_in_border'],
                site='edges',
                references=[self.most_frequent_edges, self.most_frequent_centers]
            )['is_proper'], False
        )

        # Jogo com 5 números de centro (passa)
        self.assertEqual(
            self.obj.get_border_or_center_size(
                target_game=self.games['proper_numbers_in_center'],
                site='center',
                references=[self.most_frequent_edges, self.most_frequent_centers]
            )['is_proper'], True
        )

        # Jogo com 9 números de centro (não passa)
        self.assertEqual(
            self.obj.get_border_or_center_size(
                target_game=self.games['improper_numbers_in_center'],
                site='center',
                references=[self.most_frequent_edges, self.most_frequent_centers]
            )['is_proper'], False
        )

    # a_g
    def test_impropers_start_and_end(self):
        # Não começa com (1, 3, 5) nem (2, 4)
        self.obj.game = self.games['proper_start']
        self.assertEqual(self.obj.impropers_start_and_end()['is_proper'], True)

        # Não termina com (22, 24) nem (21, 23, 25)
        self.obj.game = self.games['proper_end']
        self.assertEqual(self.obj.impropers_start_and_end()['is_proper'], True)

        # Começa com (1, 3, 5) nem (2, 4)
        self.obj.game = self.games['improper_start']
        self.assertEqual(self.obj.impropers_start_and_end()['is_proper'], False)

        # Termina com (22, 24) nem (21, 23, 25)
        self.obj.game = self.games['improper_end']
        self.assertEqual(self.obj.impropers_start_and_end()['is_proper'], False)
