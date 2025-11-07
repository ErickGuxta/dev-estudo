nums = [3, 2, 4]
target = 6

ordenado = sorted(nums)

left = 0
right = len(nums) - 1 

while left < right:

    if ordenado[left] + ordenado[right] == target:
        print
        print ([left, right])
    
    if ordenado[left] + ordenado[right] < target:
        left +=1
    else:
        right -=1
    
