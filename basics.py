"""
    Enumerate vs Range ()
    >> ipython --no-banner -i $file.py
    >>call function and pass args
    >>exit() shell

    Sample Easy Question

"""

def fizz_buzz(numbers):
    """
        Given a list of integers, 
        1. Replace all integers divisible by 3 with "fizz"
        2. Replace all integers divisible by 5 with "buzz"
        3. Replace all integers divisible by both 3 and 5 with "fizzbuzz"

        >>> numbers = [45, 22, 14, 65, 97, 72]
        >>> fizz_buzz(numbers)
        >>> numbers
        # ['fizzbuzz', 22, 14, 'buzz', 97, 'fizz']
    """
    # Using range()
    for i in range(len(numbers)):
        num = numbers[i]
        if num % 3 == 0 :
            numbers[i] = "fizz"
        if num % 5 == 0 :
            numbers[i] = "buzz"
        if num % 3 == 0  and num % 5 == 0:
            numbers[i] = "fizzbuzz"


"""
    Output :
    >>> numbers = [45, 22, 14, 65, 97, 72]
    >>> def fizz_buzz(numbers):
    ...     for i in range(len(numbers)):
    ...         num = numbers[i]
    ...         if num % 3 == 0 :
    ...             numbers[i] = "fizz"
    ...         if num % 5 == 0 :
    ...             numbers[i] = "buzz"
    ...         if num % 3 == 0  and num % 5 == 0:
    ...             numbers[i] = "fizzbuzz"
    ...
    >>> fizz_buzz(numbers)
    >>> numbers
    ['fizzbuzz', 22, 14, 'buzz', 97, 'fizz']
"""