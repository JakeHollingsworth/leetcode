'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
'''
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_dict = {}
        mag_dict = {}
        for char in ransomNote:
            if char not in ransom_dict:
                ransom_dict[char] = ransomNote.count(char)
        for char in magazine:
            if char not in mag_dict:
                mag_dict[char] = magazine.count(char)
        for char, count in ransom_dict.items():
            if char not in mag_dict or count > mag_dict[char]:
                return False
        return True
