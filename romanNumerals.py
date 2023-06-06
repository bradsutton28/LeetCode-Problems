"""
LeetCode Problem #13 Roman to Integer
--Prompt--
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
--Constraints--
1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        conversionsDict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        # Not the most efficient algorithm, however solves all cases with easy
        # -> to read and replicate code. Useful for this example since
        # -> Very large strings of roman numerals are non practical and there are few rules
        finalNum = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

        for letter in s:
            finalNum += conversionsDict[letter]
        return finalNum
