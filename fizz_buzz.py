'''
    FizzBuzz is a childhood game that iterates over a range of numbers and uses simple logic to decide whether to say a "Fizz," "Buzz," or a number. 
    Through this problem, you will learn to convert that logic into code, and you will be introduced to frequently used operations like modulo and string concatenation. 
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