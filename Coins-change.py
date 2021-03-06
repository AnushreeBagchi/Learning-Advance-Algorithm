# Brute force method to get minimum number of coins required to get target
def min_coins_brute_force(coins, target):
    amount = 0
    count = 0
    while len(coins)>0:
        max_coin = max(coins)
        if amount + max_coin <= target:
            amount += max_coin
            count+=1
        else:
            coins.remove(max_coin)
    if count == 0:
        return -1 
    else:
        return count

print("Pass" if min_coins_brute_force([1,2,5], 11) == 3 else "Fail")
print("Pass" if min_coins_brute_force([1,4,5,6], 23) == 4 else "Fail")
print("Pass" if min_coins_brute_force([5,7,8], 2) == -1 else "Fail")