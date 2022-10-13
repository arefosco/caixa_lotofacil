

from banco_de_dados.banco import dtb
from executavel.exe import Card

# Para usar a função "avoid_large_odd_even_sequence" sem recriá-la aqui, vamos instanciar um objeto de classe "Card"
obj = Card()

# Onde os resultados serão inseridos
rank = []

for game in dtb:
    # Como a função da classe precisa de "self.game", é preciso dizer que cada jogo do banco é "self.game"
    obj.game = game
    # Após cada análise, se insere em "rank" o resultado se o jogo possui ou não uma linha em branco
    rank.append(f"{obj.avoid_large_odd_even_sequence()['is_acceptable']}")

if __name__ == '__main__':
    print('=============================================== RELATÓRIO ===============================================')
    print(f'Quantos jogos têm sequência de pares e ímpares menores que 4? {rank.count("True")} jogos')
    print(f'Quantos jogos têm sequência de pares e ímpares maiores que 4? {rank.count("False")} jogos')
