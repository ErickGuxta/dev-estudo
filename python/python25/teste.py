

nums = [3, 3]
target = 6

visto = []

for i in nums:
    result = target - i

    if result in nums:
        pos_i = nums.index(i)
        pos_result = nums.index(result)

        visto = [pos_i, pos_result]



print(visto)