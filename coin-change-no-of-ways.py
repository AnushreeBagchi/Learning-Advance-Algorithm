# explanation of the tabal https://www.youtube.com/watch?v=L27_JpN6Z1Q
import pprint
pp= pprint.PrettyPrinter()

def number_of_ways(coins, target):
    lookup = [[0 for _ in range(target+1)] for _ in range(len(coins))]
    # for i in range(len(lookup)):
        # lookup[i][0] = 1 #To get value = 0 there is 1 way(not to include those coins)
    
    for i in range(len(coins)):
        for j in range(target+1):
            if i == 0 and j%coins[i] == 0:
                lookup[i][j] = 1
            else:
                if j < coins[i]:
                    lookup[i][j] = lookup[i-1][j]
                else: 
                    lookup[i][j] = lookup[i-1][j] + lookup[i][j-coins[i]]
    # pp.pprint(lookup)
    return lookup[-1][-1]     
            
    
print("Pass" if number_of_ways([2,3,5,10], 15) == 9 else "Fail")
print("Pass" if number_of_ways([2,3], 6) == 2 else "Fail")
