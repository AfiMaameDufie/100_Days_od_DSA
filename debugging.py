def max(lst):
    max_num = -float('inf')
    for num in lst:
        breakpoint()
        print(num, max_num)
        if num > max_num:
            max_num = num
    return max_num

print(max([1, -3, 2, 9, 5]))
1 -inf
# -3 1
# 2 1
# 9 2
# 5 9
# 9

# Debugging with Print statements
# Built in breakpoint for Python is pdb

def max(lst):
    max_num = -float('inf')
    for num in lst:
        breakpoint()
        if num > max_num:
            max_num = num
    return 
    


# >>> print(max([1, -3, 2]))
# > <stdin>(5)max()
# (Pdb) n
# > <stdin>(6)max()
# (Pdb) n
# > <stdin>(3)max()
# (Pdb) n
# > <stdin>(4)max()
# (Pdb) n
# > <stdin>(5)max()
# (Pdb)
# (Pdb) n
# > <stdin>(3)max()
# (Pdb) n
# > <stdin>(4)max()
# (Pdb) n
# > <stdin>(5)max()
# (Pdb) n
# > <stdin>(6)max()
# (Pdb) n
# > <stdin>(3)max()
# (Pdb) n
# > <stdin>(7)max()
# (Pdb) n
# --Return--
# > <stdin>(7)max()->2
# (Pdb) n
# 2
# --Return--
# > <stdin>(1)<module>()->None