import doctest

"""
    Still on the FizzBuzz example, enum can be used.
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
        ['fizzbuzz', 22, 14, 'buzz', 97, 'fizz']
    """
    # Using enumerate()
    for i, num in enumerate(numbers):
        num = numbers[i]
        if num % 3 == 0 :
            numbers[i] = "fizz"
        if num % 5 == 0 :
            numbers[i] = "buzz"
        if num % 3 == 0  and num % 5 == 0:
            numbers[i] = "fizzbuzz"

if __name__ == '__main__':
    doctest.testmod()



"""
    Output: 
    afimaamedufie@Afis-MacBook-Pro 100_Days_od_DSA % python enumerate.py -v
    Trying:
        numbers = [45, 90, 14, 65, 97, 72]
    Expecting nothing
    ok
    Trying:
        fizz_buzz(numbers)
    Expecting nothing
    ok
    Trying:
        numbers
    Expecting:
        ['fizzbuzz', 22, 14, 'buzz', 97, 'fizz']
    ok
    1 items had no tests:
        __main__
    1 items passed all tests:
    3 tests in __main__.fizz_buzz
    3 tests in 2 items.
    3 passed and 0 failed.
    Test passed.

"""

numbers = [45, 90, 14, 65, 97, 72]
def fizz_buzz(numbers):
    for i, num in enumerate(numbers):
        num = numbers[i]
        if num % 3 == 0 :
            numbers[i] = "fizz"
        if num % 5 == 0 :
            numbers[i] = "buzz"
        if num % 3 == 0  and num % 5 == 0:
            numbers[i] = "fizzbuzz"
