

from banco_de_dados.do_1_ao_1000 import from_one_to_thousand
from banco_de_dados.do_1001_ao_2000 import from_thousand_one_to_two_thousand
from banco_de_dados.do_2001_ao_3000 import from_two_thousand_one_to_three_thousand

"FUNCIONAMENTO DO BANCO"
# Atualmente temos 3 arquivos python localizados na pasta "banco_de_dados"
# Cada arquivo armazena 1000 tuplas de jogos
# Vamos usar o primeiro arquivo "do_1_ao_1000" para entender a lógica da organização
# A ordem dos índices é decrescente (de cima para baixo)
# Portanto, "from_one_to_thousand[0]" é o índice 0, e conforme se vai descendo, os índices vão aumentando
# Há um exemplo em "if" abaixo mostrando como é organização

"Banco atual (concatenação de todos os jogos tupla vindo das importações acima)"
dtb = from_one_to_thousand + from_thousand_one_to_two_thousand + from_two_thousand_one_to_three_thousand

"Quanto menor o índice, mais perto do fim é o jogo, então 'dtb[-1]' é o último jogo do banco e da loteria"
ten_last = [dtb[-1], dtb[-2], dtb[-3], dtb[-4], dtb[-5], dtb[-6], dtb[-7], dtb[-8], dtb[-9], dtb[-10]]

if __name__ == '__main__':
    print(f'Tamanho do banco: {len(dtb)}')

    # Apenas para verificar se os 10 últimos jogos estão configurados corretamente
    for index, game in enumerate(ten_last):
        index = index + 1
        print([index], game)

    "Se cada arquivo possui 1 array com 1000 tuplas"
    # Aqui temos o primeiro arquivo
    print(dtb[0] == from_one_to_thousand[0])
    print(dtb[999] == from_one_to_thousand[999])
    # Aqui temos o segundo arquivo
    print(dtb[1000] == from_thousand_one_to_two_thousand[0])
    print(dtb[1999] == from_thousand_one_to_two_thousand[999])
    # Aqui temos o arquivo 3, que está incompleto, pois não se chegou ao jogo 3000 (índice 2999) ainda
    print(dtb[2000] == from_two_thousand_one_to_three_thousand[0])
