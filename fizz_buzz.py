'''
    FizzBuzz is a childhood game that iterates over a range of numbers and uses simple logic to decide whether to say a "Fizz," "Buzz," or a number. 
    Through this problem, you will learn to convert that logic into code, and you will be introduced to frequently used operations like modulo and string concatenation. 

    Complexity Analysis

    Time Complexity: O(N)O(N)
    Space Complexity: O(1)O(1)
'''

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [ ]
        
        for n in range(1, n+1): 
            if (n % 3 == 0 and n % 5 == 0):
                answer.append("FizzBuzz")
            elif (n % 3 == 0):
                answer.append("Fizz")
            elif (n % 5 == 0):
                answer.append("Buzz")
            else:
                answer.append(str(n))
                
        return answer


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        
        for n in range(1, n+1): 
            
            divisible_by_3 = (n % 3 == 0)
            divisible_by_5 = (n % 5 == 0)
        
        
            if divisible_by_3 and divisible_by_5:
            # Finds the modulo of n and if its divisible by 3 and 5 append, FizzBuzz
                answer.append("FizzBuzz")
            elif divisible_by_3:
            # Finds the modulo of n and if its divisible by 3, Fizz
                answer.append("Fizz")
            elif divisible_by_5:
            # Finds the modulo of n and if its divisible by 5, Buzz            
                answer.append("Buzz")
            else:
                answer.append(str(n))
                
        return answer