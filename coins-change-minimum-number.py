import pprint
import math
pp = pprint.PrettyPrinter()

def minimum_coins(coins, target):
    lookup = [[12 for _ in range(target+1)] for _ in range(len(coins))]

    for i in range(len(coins)):
        for j in range(target+1):
            if i == 0 and j%coins[i]==0:
                lookup[i][j] = math.floor(j/coins[i])
            else:
                if j<coins[i]:
                    lookup[i][j] = lookup[i-1][j]
                else:
                    lookup[i][j] = min(lookup[i-1][j], 1+lookup[i][j-coins[i]])
    # pp.pprint(lookup)
    if lookup[-1][-1] > target:
        return -1
    else: 
        return lookup[-1][-1]
    

print("Pass" if minimum_coins([1,5,6,9], 10) == 2 else "Fail")
print("Pass" if minimum_coins([5,6,9], 11) == 2 else "Fail" )
print("Pass" if minimum_coins([1,2,5], 11) == 3 else "Fail" )
print("Pass" if minimum_coins([1,4,6,5], 23) == 4 else "Fail" )
print("Pass" if minimum_coins([5,7,8], 2) == -1 else "Fail" )


