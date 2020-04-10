import pprint
pp= pprint.PrettyPrinter()

def max_pallindrome(string):
    length = len(string)
    lookup = [[0 for _ in range(length)] for _ in range(length)]
    for i in range(length):
        lookup[i][i] = 1
    for n in range(1, length):
        for start_index in range(length-1):
            end_index = start_index + n
            if end_index < length:
                if string[start_index] == string[end_index]:
                    lookup[start_index][end_index] = lookup[start_index+1][end_index-1] + 2
                else:
                    lookup[start_index][end_index] = max(lookup[start_index][end_index-1], lookup[start_index+1][end_index])
        
    # pp.pprint(lookup)
    return lookup[0][length-1]

print("Pass" if max_pallindrome("BANANA") == 5 else "Fail");
print("Pass" if max_pallindrome("BANANO") == 3 else "Fail");
print("Pass" if max_pallindrome("TACOCAT") == 7 else "Fail");
