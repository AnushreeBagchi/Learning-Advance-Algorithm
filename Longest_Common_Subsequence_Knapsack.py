def lcs(string_a, string_b):
    lookup_table = [[0 for x in range(len(string_b) + 1)] for x in range(len(string_a) + 1)]
    for i, char_a in enumerate(string_a):
        for j, char_b in enumerate(string_b):
            if char_a == char_b:
                lookup_table[i+1][j+1] = lookup_table[i][j] + 1
            else: 
                lookup_table[i+1][j+1] = max(lookup_table[i][j+1], lookup_table[i+1][j])
                
    return (lookup_table[-1][-1])

print("Pass" if lcs( "BD", "ABCD") == 2 else "Fail")

print("Pass" if lcs ("WHOWEEKLY", "HOWONLY") == 5 else "Fail")

print("Pass" if lcs ("CATSINSPACETWO", "DOGSPACEWHO") == 7 else "Fail")
