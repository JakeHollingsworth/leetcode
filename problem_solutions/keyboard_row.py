'''
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".
'''
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set(['q','w','e','r','t','y','u','i','o','p'])
        row2 = set(['a','s','d','f','g','h','j','k','l'])
        row3 = set(['z','x','c','v','b','n','m'])
        ans = []
        for word in words:
            proxy = word.lower()
            for row in [row1, row2, row3]:
                if all([ch in row for ch in proxy]):
                    ans.append(word)
        return ans
