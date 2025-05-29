d = int(input())
a = int(input()) 
n = int(input())

chegada = n

if chegada > 15:
    chegada  = 15


diaria = d + ((chegada - 1) * a)

total = diaria * (31 - n + 1) #somei 1 por que é inclusive
print(total)
