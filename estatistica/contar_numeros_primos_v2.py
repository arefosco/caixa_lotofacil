

"""
# a_a
    all_data = [
        (0, '0 jogos', 0.0, '0.0%'), (1, '2 jogos', 0.08, '0.08%'), (2, '11 jogos', 0.42, '0.42%'),
        (3, '123 jogos', 4.69, '4.69%'), (4, '444 jogos', 16.91, '16.91%'), (5, '804 jogos', 30.63, '30.63%'),
        (6, '773 jogos', 29.45, '29.45%'), (7, '377 jogos', 14.36, '14.36%'), (8, '85 jogos', 3.24, '3.24%'),
        (9, '6 jogos', 0.23, '0.23%')
    ]

# a_b
    rank_organized = [
        (5, '804 jogos', 30.63, '30.63%'), (6, '773 jogos', 29.45, '29.45%'), (4, '444 jogos', 16.91, '16.91%'),
        (7, '377 jogos', 14.36, '14.36%'), (3, '123 jogos', 4.69, '4.69%'), (8, '85 jogos', 3.24, '3.24%'),
        (2, '11 jogos', 0.42, '0.42%'), (9, '6 jogos', 0.23, '0.23%'), (1, '2 jogos', 0.08, '0.08%'),
        (0, '0 jogos', 0.0, '0.0%')
    ]

# a_c
    primes = [5, 6, 4, 7]

# b_a
    research = [
        (2, 1564, 11.01), (3, 1589, 11.19), (5, 1599, 11.26), (7, 1538, 10.83), (11, 1626, 11.45),
        (13, 1603, 11.29), (17, 1560, 10.99), (19, 1569, 11.05), (23, 1552, 10.93)
    ]

# b_b
    research_ordered = [
        (11, 1626, 11.45), (13, 1603, 11.29), (5, 1599, 11.26), (3, 1589, 11.19), (19, 1569, 11.05),
        (2, 1564, 11.01), (17, 1560, 10.99), (23, 1552, 10.93), (7, 1538, 10.83)
    ]
"""

from banco_de_dados.banco import dtb


def prime_numbers_counter(game_var):
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    prime_numbers_box = []

    for number_ in game_var:
        if number_ in prime_numbers:
            prime_numbers_box.append(number_)

    return len(prime_numbers_box)

# ============================== FREQUÊNCIA DAS QUANTIDADES DE NÚMEROS PRIMOS MAIS COMUNS ==============================


# Onde os resultados serão inseridos
rank = []

# Inserir resultado da contagem de números primos de cada jogo
for game in dtb: rank.append(f"{prime_numbers_counter(game)}")

# Var usada para calcular porcentagem
absolute_frequence = len(dtb)

# Quantidade de números primos achados (0 a 9 possíveis) (para índice 0 em "a_a")
primes_amount_int = [*range(10)]

# Quantidade de números primos achados (0 a 9 possíveis) (para índices 1, 2 e 3 em "a_a")
primes_amount_str = [str(n) for n in range(10)]

# a_a: (qtd. encontrados, freq. dele, porcentagem da freq., porcentagem em str) -> (2, '100 jogos', 15.00, 15.00%)
all_data = []
for index, prime in enumerate(primes_amount_str):
    all_data.append((
        primes_amount_int[index],
        f'{rank.count(prime)} jogos',
        float(f'{(rank.count(prime) * 100) / absolute_frequence:.2f}'),
        f"{float(f'{(rank.count(prime) * 100) / absolute_frequence:.2f}')}%"
    ))

# a_b: Dados organizados pelo valor de porcentagem (índice 2) de [0, 1, 2, 3]
rank_organized = sorted(all_data, key=lambda this_index: this_index[2], reverse=True)

"VAR para uso em [ prime_numbers_counter ] (quantidades de números primos mais recorrentes) [int, int, ...]"
# a_c: As quantidades seguidas com porcentagem acima de 10 são consideradas para o algoritmo
primes = []
[primes.append(tuple_index[0]) if tuple_index[2] > 10 else None for tuple_index in rank_organized]

# ===================================== FREQUÊNCIA DOS NÚMEROS PRIMOS MAIS COMUNS =====================================

# Coletar a frequência que cada número primo aparece (feito manualmente por ser um dicionário pequeno)
prime_numbers_ = [2, 3, 5, 7, 11, 13, 17, 19, 23]
prime_numbers_dict = {
    2: {'qt': 0}, 3: {'qt': 0}, 5: {'qt': 0}, 7: {'qt': 0}, 11: {'qt': 0}, 13: {'qt': 0}, 17: {'qt': 0}, 19: {'qt': 0},
    23: {'qt': 0}
}

# Dentro de cada jogo do banco, se itera sob os índices em busca dos números primos p/ registrar sua quantidade
for game in dtb:
    for number in game:
        if number in prime_numbers_:
            if number == 2: prime_numbers_dict[2]['qt'] += 1
            if number == 3: prime_numbers_dict[3]['qt'] += 1
            if number == 5: prime_numbers_dict[5]['qt'] += 1
            if number == 7: prime_numbers_dict[7]['qt'] += 1
            if number == 11: prime_numbers_dict[11]['qt'] += 1
            if number == 13: prime_numbers_dict[13]['qt'] += 1
            if number == 17: prime_numbers_dict[17]['qt'] += 1
            if number == 19: prime_numbers_dict[19]['qt'] += 1
            if number == 23: prime_numbers_dict[23]['qt'] += 1

absolute_freq = sum([prime_numbers_dict[key]['qt'] for key in prime_numbers_dict])

# b_a: Receberá a cópia dos dados de "prime_numbers_dict" e + um dado adicional: cálculo de porcentagem
research = []
for key in prime_numbers_dict:
    research.append(
        (key, prime_numbers_dict[key]['qt'], float(f"{(prime_numbers_dict[key]['qt'] * 100) / absolute_freq:.2f}"))
    )

# b_b: "research" carrega os dados necessário, mais eles estão fora de ordem. Organizamos aqui via índice 1
research_ordered = sorted(research, key=lambda index_n: index_n[2], reverse=True)

"VAR retirada de [ prime_numbers_counter ] (jogo deveria ter ao menos 1 dos números primos mais frequentes)"
# b_c: De "research_ordered", extrai-se o índice 0 dos 3 primeiros índices (números primos mais recorrentes)
top_3_primes = [tuple_[0] for tuple_ in research_ordered[0:3]]

if __name__ == '__main__':
    print(f"{all_data = }")
    print(f"{rank_organized = }")
    print(f"{primes = }\n")

    print(f"{research = }")
    print(f"{research_ordered = }")
    print(f"{top_3_primes = }")
