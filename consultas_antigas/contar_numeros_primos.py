

from banco_de_dados.banco import dtb
from collections import Counter
from banco_de_dados.banco import ten_last


def prime_numbers_counter_query(the_game):
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    prime_numbers_box = []

    # De acordo com "consultas/contar_numeros_primos.py" o qtd. de números primos mais comuns: [4, 5, 6, 7]

    for number in the_game:
        if number in prime_numbers:
            prime_numbers_box.append(number)

    if len(prime_numbers_box) in range(4, 8):
        return {'is_proper': True, 'primes': prime_numbers_box}
    return {'is_proper': False, 'primes': prime_numbers_box}


# TODO: Para usar no algoritmo, onde "right_amount" é o "ALVO" neste documento
def prime_numbers_counter(the_game, right_amount):
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    prime_numbers_box = []

    for number in the_game:
        if number in prime_numbers:
            prime_numbers_box.append(number)

    if len(prime_numbers_box) in right_amount:
        return {'amount_found': len(prime_numbers_box), 'found': prime_numbers_box, 'acceptable': True}
    if len(prime_numbers_box) not in right_amount:
        return {'amount_found': len(prime_numbers_box), 'found': prime_numbers_box, 'acceptable': False}


# Quantos números primos vieram nos 10 últimos jogos (ordem: do último jogo ao décimo)
ten_last_prime_amount = [prime_numbers_counter_query(the_game=game) for game in ten_last]

print('Números primos encontrados nos 10 últimos jogos')
print(ten_last_prime_amount)

prime_counter_all_games = []
# List comprehension que analisa todos os jogos e passa p/ o array acima quanto n primos fora achados em cada jogo
[prime_counter_all_games.append(str(prime_numbers_counter_query(the_game=index))) for index in dtb]
print('Números primos encontrados em cada jogo')
print(prime_counter_all_games)

print('Rank dos números primos por número de repetições')
prime_counter_all_games_election = Counter([int_ for int_ in prime_counter_all_games])
print(prime_counter_all_games_election)

# Caso queira aumentar o rank, mudar parâmetro em "most_common"
print('Rank dos números primos por número de repetições (3 primeiros)')
prime_amount_rank_3 = [int(number) for number in tuple(dict(prime_counter_all_games_election.most_common(3)).keys())]
print(prime_amount_rank_3)

# Cópia da var acima p/ exportação no algoritmo principal (não mandatório)
prime_numbers_amount_main_rank = prime_amount_rank_3
