'''
You are given a 0-indexed 2D integer array brackets where brackets[i] = [upperi, percenti] means that the ith tax bracket has an upper bound of upperi and is taxed at a rate of percenti. The brackets are sorted by upper bound (i.e. upperi-1 < upperi for 0 < i < brackets.length).

Tax is calculated as follows:

The first upper0 dollars earned are taxed at a rate of percent0.
The next upper1 - upper0 dollars earned are taxed at a rate of percent1.
The next upper2 - upper1 dollars earned are taxed at a rate of percent2.
And so on.
You are given an integer income representing the amount of money you earned. Return the amount of money that you have to pay in taxes. Answers within 10-5 of the actual answer will be accepted.
'''
class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = 0
        max_upper = 0
        for upper, percent in brackets:
            current_bracket_amt = ((upper if income > upper else max(max_upper,income)) - max_upper)
            tax += current_bracket_amt * percent / 100
            max_upper = upper
        return tax
