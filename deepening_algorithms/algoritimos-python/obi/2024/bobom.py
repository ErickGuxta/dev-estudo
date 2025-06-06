cartas = [input().strip() for _ in range(7)]
carta_dominante = cartas[0][1]
#A J Q K
#C E O P

# 1 naipe é o dominande
# 2, 3 e 4 naipe Luana
# 5, 6 e 7 Edu
p_luana = 0
p_edu = 0

for i in range(1, 4):
    # Verifica a figura
    if cartas[i][0] == 'A': p_luana += 10
    elif cartas[i][0] == 'J': p_luana += 11
    elif cartas[i][0] == 'Q': p_luana += 12
    elif cartas[i][0] == 'K': p_luana += 13
    
    # Verifica o naipe
    if cartas[i][1] == carta_dominante: p_luana += 4

for i in range(4, 7):
    # Verifica a figura
    if cartas[i][0] == 'A': p_edu += 10
    elif cartas[i][0] == 'J': p_edu += 11
    elif cartas[i][0] == 'Q': p_edu += 12
    elif cartas[i][0] == 'K': p_edu += 13
    
    # Verifica o naipe
    if cartas[i][1] == carta_dominante: p_edu += 4

if p_edu > p_luana:
    print("Edu")
elif p_edu < p_luana:
    print("Luana")
else:
    print("empate")




