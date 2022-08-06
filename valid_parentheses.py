'''
    Valid Parentheses

    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    

    Example 1:

    Input: s = "()"
    Output: true
    Example 2:

    Input: s = "()[]{}"
    Output: true
    Example 3:

    Input: s = "(]"
    Output: false
    

    Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'

'''

class Solution:
    def isValid(self, s: str) -> bool:
        
        char_pattern = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        
        list = []
        
        
        for char in s:
            if char in "({[":
                list.append(char_pattern[char])
                
            else:
                if not list or list.pop()!= char:
                    return False
                else:
                    continue
                    
        if not list:
            return True
            
        else:
            return False

# Algorithm Complexity
# O(n)

