'''
    383. Ransom Note

    Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

    Each letter in magazine can only be used once in ransomNote.

    

    Example 1:

    Input: ransomNote = "a", magazine = "b"
    Output: false
    Example 2:

    Input: ransomNote = "aa", magazine = "ab"
    Output: false
    Example 3:

    Input: ransomNote = "aa", magazine = "aab"
    Output: true
    

    Constraints:

    1 <= ransomNote.length, magazine.length <= 105
    ransomNote and magazine consist of lowercase English letters.
'''


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_ransom = collections.Counter(ransomNote)
        hash_magazine = collections.Counter(magazine)
        
        
        for i in hash_ransom:
            if i in hash_magazine:
                if i in hash_magazine[i] > hash_ransom[i]:
                    return False
            else:
                return False
        return True


'''
    "collections.counter()" counts every charcter in the string and return a dictonary. key as character and value as count example- "aabbcddd" >>{"a":2,"b":2,"c":1,"d":3}
    in the first for loop, we get the keys of the the ransom note into i to get counts of ransom and magazine
    then the next if checks if char in hash ransom is in hash magazine
    then the next if checks the count because in the question it stated that the count for num of char in ransom note is less than that in magazine
    So it returns a false or exits the loop and comtinues
    if the char in hash ransom is not in hash maagzine, return false
    if no conditions are met, return false
    
'''