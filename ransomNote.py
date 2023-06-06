"""
LeetCode problem # 383 Ransom Note
-- Prompt --
Given two strings ransomNote and magazine,
return true if ransomNote can be constructed by using the letters from
magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

--Constraints--
1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.

Test Case below which failed on original design (so using it to test again)

ransomNote = "fihjjjjei"
magazine = "hjibagacbhadfaefdjaeaebgi"


def canConstruct(ransomNote: str, magazine: str) -> bool:
    mylist = list(magazine)
    for letter in ransomNote:
        if mylist.__contains__(letter):
            #print("The Magazine contains the letters '{}'", letter) #Testing Purposes
            mylist.remove(letter)
        else:
            #print("False") #Testing Purposes
            return False
    #print("True") #Testing Purposes
    return True


canConstruct(ransomNote, magazine)
"""
# Actual Code submitted in class solution
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mylist = list(magazine)
        for letter in ransomNote:
            if mylist.__contains__(letter):
                #print("The Magazine contains the letter '{}'", letter)
                mylist.remove(letter)
            else:
                #print("False")
                return False
        #print("True")
        return True

