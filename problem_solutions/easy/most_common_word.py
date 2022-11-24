'''
Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.
'''
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub(r'[^\w\s]',' ',paragraph)        
        words = paragraph.lower().split(' ')
        banned = set([word.lower() for word in banned])
        word_count = {}
        for word in words:
            word_count[word] = word_count[word] + 1 if word in word_count else 1
        word_count[""] = 0
        max_word = ""
        for word, count in word_count.items():
            if count > word_count[max_word] and word not in banned:
                max_word = word
        return max_word
