# Python 3.10.2 (main, May 10 2022, 11:34:48) [Clang 13.1.6 (clang-1316.0.21.2.3)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> lst = [1, 2, 5, -4 ]
# >>> def square(x):
# ...     return x * x
# ...
# >>> map
# <class 'map'>
# >>> map(square, lst)
# <map object at 0x104a27be0>
# >>> list(map(square, lst))
# [1, 4, 25, 16]
# >>>
# >>> result = []
# >>> for num in lst:
# ...     result.append(square(num))
# ...
# >>> result
# [1, 4, 25, 16]
# >>>


# most Pythonic way ; using the brackets and calling square on num for num in the list 
# >>>
# >>> [square(num) for num in lst]
# [1, 4, 25, 16]


# Checking if function is odd or not

# >>> lst = [1, 2, -5, 4, 9, 10]
# >>>
# >>> filter
# <class 'filter'>
# >>>
# >>> def is_odd(x):
# ...     return x % 2 == 1
# ...
# >>> filter(is_odd, lst)
# <filter object at 0x104a27100>
# >>>
# >>> list(filter(is_odd, lst))
# [1, -5, 9]


# >>> [is_odd(num) for num in lst]
# [True, False, True, False, True, False]



# Grid Question
grid = [[0,0,0],
        [0,0,0]]

num_rows = 2
num_cols = 3

for _ in range(num_rows):
     curr_row = []
     for _ in range(num_cols):
             curr_row.append(0)
     grid.append(curr_row)


grid
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

grid
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]




# Finally, haha
# afimaamedufie@Afis-MacBook-Pro 100_Days_od_DSA % python3
# Python 3.10.2 (main, May 10 2022, 11:34:48) [Clang 13.1.6 (clang-1316.0.21.2.3)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> num_rows = 2
# >>>
# >>> num_cols = 3
# >>>
# >>> grid = []
# >>>
# >>> for _ in range(num_rows):
# ...     curr_row = []
# ...     for _ in range(num_cols):
# ...             curr_row.append(0)
# ...     grid.append(curr_row)
# ...
# >>>
# >>> grid
# [[0, 0, 0], [0, 0, 0]]
# >>>
