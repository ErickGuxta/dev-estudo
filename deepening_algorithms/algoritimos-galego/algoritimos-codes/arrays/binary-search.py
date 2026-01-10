def binary_search(nums, n):
    l = 0
    r = len(nums)

    while l < r:
        meio = int((l+r)/2)

        if meio == n:
            print(meio)
            break
        elif meio > n:
            r = meio
        else :
            l = meio + 1
    print( -1)
        


a = [1,2,3,4,5,6,8,9,10,11]
binary_search(a,11)
