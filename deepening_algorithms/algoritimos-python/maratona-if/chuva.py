def resolver_vazamento(N, M, parede):
    for j in range(M):
        if parede[0][j] == 'o':
            for i in range(1, N):
                if parede[i][j] == '.': parede[i][j] = 'o'
                if parede[i][j] == '#':
                    for k in range(j-1, -1, -1):
                        if parede[i][k] == '.' and (parede[i+1][k] == '#' if i+1 < N else False): parede[i][k] = 'o'
                        else: break
                    for k in range(j+1, M):
                        if parede[i][k] == '.' and (parede[i+1][k] == '#' if i+1 < N else False): parede[i][k] = 'o'
                        else: break
    return parede

# Leitura da entrada
N, M = map(int, input().split())
parede = [list(input().strip()) for _ in range(N)]

# Resolver e imprimir o resultado
resultado = resolver_vazamento(N, M, parede)
print('\n'.join(''.join(linha) for linha in resultado))