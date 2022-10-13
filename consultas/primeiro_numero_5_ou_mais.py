

from banco_de_dados.banco import dtb

reproved = 0
starts_at_4 = 0
starts_at_3 = 0
starts_at_2 = 0
starts_at_1 = 0
finishes_wrong = 0
finishes_with_16 = 0
finishes_with_17 = 0
finishes_with_18 = 0
finishes_with_19 = 0
finishes_with_20 = 0
finishes_with_21 = 0
finishes_with_22 = 0

for game in dtb:
    if game[0] >= 5: reproved += 1
    elif game[0] == 4: starts_at_4 += 1
    elif game[0] == 3: starts_at_3 += 1
    elif game[0] == 2: starts_at_2 += 1
    elif game[0] == 1: starts_at_1 += 1

for game in dtb:
    if game[-1] in range(16, 22): finishes_wrong += 1

for game in dtb:
    if game[-1] == 16: finishes_with_16 += 1
    if game[-1] == 17: finishes_with_17 += 1
    if game[-1] == 18: finishes_with_18 += 1
    if game[-1] == 19: finishes_with_19 += 1
    if game[-1] == 20: finishes_with_20 += 1
    if game[-1] == 21: finishes_with_21 += 1
    if game[-1] == 22: finishes_with_22 += 1

print('================================================== RELATÓRIO ==================================================')
print(f'Jogos com lacuna inicial grande (5+)?      {reproved} jogos')
print(f'Jogos cujo primeiro número do volante é 4? {starts_at_4} jogos')
print(f'Jogos cujo primeiro número do volante é 3? {starts_at_3} jogos')
print(f'Jogos cujo primeiro número do volante é 2? {starts_at_2} jogos')
print(f'Jogos cujo primeiro número do volante é 1? {starts_at_1} jogos')
print(f'Jogos cujo último número do volante está entre 16 a 22? {finishes_wrong} jogos')
print(f'Jogos cujo último número do volante é 16? {finishes_with_16} jogos')
print(f'Jogos cujo último número do volante é 17? {finishes_with_17} jogos')
print(f'Jogos cujo último número do volante é 18? {finishes_with_18} jogos')
print(f'Jogos cujo último número do volante é 19? {finishes_with_19} jogos')
print(f'Jogos cujo último número do volante é 20? {finishes_with_20} jogos')
print(f'Jogos cujo último número do volante é 21? {finishes_with_21} jogos')
print(f'Jogos cujo último número do volante é 22? {finishes_with_22} jogos')
