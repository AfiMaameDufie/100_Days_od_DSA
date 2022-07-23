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