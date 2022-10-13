

from banco_de_dados.banco import dtb


def score_admin(
        target_game, game_from_db, single_score, target_score, has_comparison=False, operator='equals', repeated=0
):

    similarities = []

    for i in range(len(game_from_db)):
        # Os jogos são tuplas, mas p/ saber a interseção é preciso conversão p/ conjunto, dentro de [ intersection() ]
        # O método [ intersection() ] está dentro de [ len() ] p/ que o retorno seja inteiro
        similarity_target_game_vs_db_game = len(set(target_game).intersection(set(game_from_db[i])))
        similarities.append(similarity_target_game_vs_db_game)

    precisions = [
        similarities.count(6), similarities.count(7), similarities.count(8), similarities.count(9),
        similarities.count(10), similarities.count(11), similarities.count(12), similarities.count(13),
        similarities.count(14), similarities.count(15)
    ]

    score_panel = f"""
    Jogo analisado: {target_game}
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
        [box_with_score.append(scores[key]) for key in scores if target_score == key]

        # (has_comparison, operator, repeated) (comparação desejada, comparador, pontuação)
        if has_comparison and operator == 'equals':
            if box_with_score[0] == repeated:
                return True
            return False
        if has_comparison and operator == 'greater':
            if box_with_score[0] > repeated:
                return True
            return False
        if has_comparison and operator == 'lesser':
            if box_with_score[0] < repeated:
                return True
            return False

        if not has_comparison:
            return box_with_score[0]

    else:
        return score_panel


if __name__ == '__main__':

    # Jogo alvo a ser comparado com cada jogo existente na história da Lotofácil
    sample_game = (1, 3, 4, 5, 8, 10, 11, 15, 16, 17, 20, 22, 23, 24, 25)

    "MÉTODO 1 - Jogo em [target_game] fez as seguintes pontuações de 6 a 15"
    sample_game_score_panel = score_admin(
        target_game=sample_game, game_from_db=dtb, single_score=False, target_score=None
    )
    print('========== 1 ==========')
    print(sample_game_score_panel)

    "MÉTODO 2 - Jogo em [target_game] fez a pontuação [target_score]"
    sample_game_score_specific = score_admin(
        target_game=sample_game, game_from_db=dtb, single_score=True, target_score=14
    )
    print('========== 2 ==========')
    print(sample_game_score_specific)

    "MÉTODO 3 - Jogo em [target_game] fez a pontuação [target_score] na quantidade [repeated] na comparação [operator]"
    sample_game_score_specific_repetition = score_admin(
        target_game=sample_game, game_from_db=dtb, single_score=True, target_score=13,
        has_comparison=True, operator='greater', repeated=3
    )
    print('========== 3 ==========')
    print(sample_game_score_specific_repetition)
