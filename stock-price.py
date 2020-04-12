def max_difference(arr):
    min_value_index = 0
    max_value_index = 1
    current_min_price_index = 0

    if len(arr) < 2:
        return

    for i in range(1, len(arr)):
       
        if arr[i] < arr[current_min_price_index]:
            current_min_price_index = i
        
        if arr[max_value_index] - arr[min_value_index] < arr[i] - arr[current_min_price_index]:
            max_value_index = i
            min_value_index = current_min_price_index

    max_profit = arr[max_value_index] - arr[min_value_index]
    return max_profit

print("Pass" if max_difference([3,4,7,8,6])==5 else "Fail")

prices = [2, 2, 7, 9, 9, 12, 18, 23, 34, 37, 45, 54, 78]
print("Pass" if max_difference(prices) == 76 else "Fail")

prices = [54, 18, 37, 9, 11, 48, 23, 1, 7, 34, 2, 45, 67]
print("Pass" if max_difference(prices) == 66 else "Fail")

prices = [78, 54, 45, 37, 34, 23, 18, 12, 9, 9, 7, 2, 2]
print("Pass" if max_difference(prices) == 0 else "Fail")
