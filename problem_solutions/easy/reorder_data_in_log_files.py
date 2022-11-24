'''
You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits.
Reorder these logs so that:

The letter-logs come before all digit-logs.
The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
The digit-logs maintain their relative ordering.
Return the final order of the logs.
'''
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        ledger = [1 if l[-1] in "1234567890" else 0 for l in logs]
        letters = [l.split() for l, dig in zip(logs, ledger) if not dig]
        ids = []
        for li in letters:
            ids.append(li.pop(0))
        letters = [" ".join(l) for l in letters]
        separated = list(zip(letters, ids))
        separated.sort()
        letters = [identifier + " " + code for code, identifier in separated]
        digits = [l for l, dig in zip(logs, ledger) if dig]
        return letters + digits
