'''
Given two strings first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.

Return an array of all the words third for each occurrence of "first second third".
'''
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        result = []
        words = text.split(' ')
        for i, w in enumerate(words):
            if i > 1 and words[i-2] == first and words[i-1]==second:
                result.append(w)
        return result
