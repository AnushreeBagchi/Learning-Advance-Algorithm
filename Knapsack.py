import collections

Item =  collections.namedtuple('Item', ['weight', 'value'])

def max_value(knapsack_max_weight, items):
    lookup_table = [0] * (knapsack_max_weight+1)
    for item in items:
        for capacity in reversed(range(knapsack_max_weight+1)):
            if capacity >= item.weight:
                lookup_table[capacity] = max(lookup_table[capacity], lookup_table[capacity-item.weight] + item.value)
    return lookup_table
    
items = [Item(10, 7), Item(9, 8), Item(5, 6)]
knapsack_max_weight = 15
print(max_value(knapsack_max_weight, items))