'''
    1342. Number of Steps to Reduce a Number to Zero

    This is a simulation problem; all we have to do to arrive at the correct result is follow the instructions.
    Through this problem, you will learn how to identify if a number is even or odd (hint, think about the modulo operator from the previous problem).
    For those who are looking for an added challenge, you can try solving this problem using bitwise operations. 

    Given an integer num, return the number of steps to reduce it to zero.

    In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
'''

class Solution:
    def numberOfSteps(self, num: int) -> int:
        
            counter = 0 
            while num!= 0:
                if (num % 2 == 0):
                    num = num // 2

                else:
                    num = num - 1
                    
                counter=counter + 1

            return counter