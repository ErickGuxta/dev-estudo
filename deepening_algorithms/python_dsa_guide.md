# 🐍 Guia Completo de Python para Algoritmos e Estruturas de Dados

> Guia de referência rápida para resolução de problemas de programação competitiva, LeetCode e OBI

## 1. Entrada e Saída

### Entrada Básica
```python
# Leitura simples
n = int(input())
texto = input()
x, y = map(int, input().split())

# Múltiplas linhas
arr = []
for _ in range(n):
    arr.append(int(input()))

# Lista em uma linha
nums = list(map(int, input().split()))
```

### Saída Formatada
```python
print(x, y)  # Separado por espaço
print(x, y, sep=', ')  # Separador customizado
print(f"Resultado: {x}")  # f-string
print(f"{x:.2f}")  # 2 casas decimais
```

## 2. Estruturas de Dados Nativas

### Listas (Arrays Dinâmicos)
```python
# Criação
arr = []
arr = [0] * n  # Lista com n zeros
arr = [i for i in range(n)]  # List comprehension

# Operações - O(1) no final, O(n) no início
arr.append(x)  # Adiciona no final
arr.pop()  # Remove do final
arr.insert(i, x)  # Insere na posição i
arr.remove(x)  # Remove primeira ocorrência
arr[i] = x  # Acessa/modifica
len(arr)  # Tamanho
arr.reverse()  # Inverte in-place
arr.sort()  # Ordena in-place
sorted(arr)  # Retorna nova lista ordenada

# Slicing
arr[i:j]  # Elementos de i até j-1
arr[:i]  # Primeiros i elementos
arr[i:]  # Do i até o final
arr[::-1]  # Inverte lista
```

### Deque (Fila de Duas Pontas)
```python
from collections import deque

dq = deque()
dq.append(x)  # Adiciona à direita - O(1)
dq.appendleft(x)  # Adiciona à esquerda - O(1)
dq.pop()  # Remove da direita - O(1)
dq.popleft()  # Remove da esquerda - O(1)
```

### Pilha (Stack)
```python
stack = []
stack.append(x)  # Push - O(1)
stack.pop()  # Pop - O(1)
stack[-1]  # Topo
len(stack) > 0  # Verifica se vazia
```

### Fila (Queue)
```python
from collections import deque
queue = deque()
queue.append(x)  # Enqueue - O(1)
queue.popleft()  # Dequeue - O(1)
```

### Dicionários (Hash Map)
```python
d = {}
d = dict()
d[key] = value  # Inserção/atualização - O(1)
value = d.get(key, default)  # Busca com valor padrão
key in d  # Verifica existência - O(1)
del d[key]  # Remove
d.keys()  # Todas as chaves
d.values()  # Todos os valores
d.items()  # Pares (key, value)

# Counter - contagem de elementos
from collections import Counter
count = Counter(arr)
count[x]  # Frequência de x
count.most_common(k)  # k elementos mais comuns
```

### Conjuntos (Set)
```python
s = set()
s.add(x)  # Adiciona - O(1)
s.remove(x)  # Remove (erro se não existe)
s.discard(x)  # Remove (sem erro)
x in s  # Verifica existência - O(1)
len(s)  # Tamanho

# Operações de conjunto
s1 | s2  # União
s1 & s2  # Interseção
s1 - s2  # Diferença
s1 ^ s2  # Diferença simétrica
```

### Heap (Fila de Prioridade)
```python
import heapq

heap = []
heapq.heappush(heap, x)  # Insere - O(log n)
min_val = heapq.heappop(heap)  # Remove menor - O(log n)
min_val = heap[0]  # Menor elemento sem remover
heapq.heapify(arr)  # Transforma lista em heap - O(n)

# Max heap (negando valores)
heapq.heappush(heap, -x)
max_val = -heapq.heappop(heap)
```

## 3. Algoritmos de Ordenação

```python
# Ordenação nativa - O(n log n)
arr.sort()  # In-place
sorted_arr = sorted(arr)  # Nova lista

# Ordenação customizada
arr.sort(key=lambda x: x[1])  # Ordena por segundo elemento
arr.sort(reverse=True)  # Decrescente
```

## 4. Busca

### Busca Linear
```python
def linear_search(arr, target):
    for i, x in enumerate(arr):
        if x == target:
            return i
    return -1
```

### Busca Binária
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Usando bisect
import bisect
idx = bisect.bisect_left(arr, target)  # Posição de inserção à esquerda
idx = bisect.bisect_right(arr, target)  # Posição de inserção à direita
```

## 5. Técnicas de Programação

### Two Pointers
```python
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == target:
            return [left, right]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return []
```

### Sliding Window
```python
def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

### Prefix Sum
```python
def prefix_sum(arr):
    prefix = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        prefix[i + 1] = prefix[i] + arr[i]
    return prefix

# Soma do intervalo [left, right]
def range_sum(prefix, left, right):
    return prefix[right + 1] - prefix[left]
```

### Programação Dinâmica (DP)

#### Fibonacci
```python
def fibonacci(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```

#### Mochila 0/1
```python
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], 
                              dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]
```

## 6. Grafos

### Representação
```python
# Lista de adjacência
graph = [[] for _ in range(n)]
graph[u].append(v)  # Aresta de u para v

# Dicionário
graph = {}
graph[u] = [v1, v2, v3]

# Matriz de adjacência
graph = [[0] * n for _ in range(n)]
graph[u][v] = 1  # Aresta de u para v
```

### BFS (Busca em Largura)
```python
from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        # Processar node
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

### DFS (Busca em Profundidade)
```python
def dfs(graph, node, visited):
    visited.add(node)
    # Processar node
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Iterativo
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            # Processar node
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
```

### Dijkstra (Caminho Mínimo)
```python
import heapq

def dijkstra(graph, start, n):
    dist = [float('inf')] * n
    dist[start] = 0
    heap = [(0, start)]
    
    while heap:
        d, node = heapq.heappop(heap)
        
        if d > dist[node]:
            continue
        
        for neighbor, weight in graph[node]:
            new_dist = dist[node] + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    
    return dist
```

### Union-Find (Disjoint Set)
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        
        return True
```

## 7. Árvores

### Árvore Binária
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Travessia em ordem
def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

# Travessia em pré-ordem
def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

# Travessia em pós-ordem
def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]

# Travessia por nível
def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    
    return result
```

## 8. Strings

```python
# Operações básicas
s = "hello"
s[i]  # Acesso - O(1)
len(s)  # Tamanho
s.lower()  # Minúsculas
s.upper()  # Maiúsculas
s.strip()  # Remove espaços das pontas
s.split()  # Divide em palavras
''.join(arr)  # Junta lista em string

# Verificações
s.isalpha()  # Somente letras
s.isdigit()  # Somente dígitos
s.isalnum()  # Letras e/ou dígitos

# Substring
s[i:j]  # Do i ao j-1
s.find(substring)  # Índice da primeira ocorrência (-1 se não encontrar)
s.count(substring)  # Conta ocorrências

# Palíndromo
def is_palindrome(s):
    return s == s[::-1]
```

## 9. Matemática e Bits

### Operações Bit a Bit
```python
x & y  # AND
x | y  # OR
x ^ y  # XOR
~x  # NOT
x << k  # Shift esquerda (multiplica por 2^k)
x >> k  # Shift direita (divide por 2^k)

# Verificar se bit i está setado
(x >> i) & 1

# Setar bit i
x | (1 << i)

# Limpar bit i
x & ~(1 << i)

# Toggle bit i
x ^ (1 << i)

# Contar bits setados
bin(x).count('1')
```

### Funções Matemáticas
```python
import math

math.gcd(a, b)  # Máximo divisor comum
math.lcm(a, b)  # Mínimo múltiplo comum (Python 3.9+)
math.sqrt(x)  # Raiz quadrada
math.floor(x)  # Arredonda para baixo
math.ceil(x)  # Arredonda para cima
abs(x)  # Valor absoluto
pow(x, y)  # x elevado a y
x ** y  # Exponenciação

# Números primos
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Crivo de Eratóstenes
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    
    return [i for i in range(n + 1) if is_prime[i]]
```

## 10. Técnicas Avançadas

### Backtracking (Permutações)
```python
def permutations(nums):
    result = []
    
    def backtrack(path, remaining):
        if not remaining:
            result.append(path[:])
            return
        
        for i in range(len(remaining)):
            path.append(remaining[i])
            backtrack(path, remaining[:i] + remaining[i+1:])
            path.pop()
    
    backtrack([], nums)
    return result
```

### Memoização
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Manual
memo = {}
def fib(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]
```

## 11. Complexidade de Tempo

| Operação | List | Deque | Dict | Set | Heap |
|----------|------|-------|------|-----|------|
| Acesso | O(1) | O(n) | O(1) | - | - |
| Busca | O(n) | O(n) | O(1) | O(1) | O(n) |
| Inserção (fim) | O(1) | O(1) | O(1) | O(1) | O(log n) |
| Inserção (início) | O(n) | O(1) | - | - | - |
| Remoção (fim) | O(1) | O(1) | O(1) | O(1) | O(log n) |
| Remoção (início) | O(n) | O(1) | - | - | - |

## 12. Dicas para Competições

1. **Leia o problema com atenção** - entenda os limites e restrições
2. **Pense na complexidade** - calcule se sua solução vai passar no tempo
3. **Comece simples** - implemente a solução mais básica primeiro
4. **Use nomes claros** - facilita debugar
5. **Teste casos extremos** - array vazio, um elemento, valores máximos
6. **Desenhe exemplos** - visualize o problema
7. **Identifique o padrão** - muitos problemas seguem templates conhecidos

### Templates Úteis
```python
# Leitura padrão OBI
n = int(input())
arr = list(map(int, input().split()))

# Leitura de matriz
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Inicialização de matriz 2D
dp = [[0] * cols for _ in range(rows)]

# Direções (cima, baixo, esquerda, direita)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 8 direções
directions = [(-1, 0), (1, 0), (0, -1), (0, 1), 
              (-1, -1), (-1, 1), (1, -1), (1, 1)]
```