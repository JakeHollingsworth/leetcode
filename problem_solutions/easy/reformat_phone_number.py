'''
You are given a phone number as a string number. number consists of digits, spaces ' ', and/or dashes '-'.

You would like to reformat the phone number in a certain manner. Firstly, remove all spaces and dashes. Then, group the digits from left to right into blocks of length 3 until there are 4 or fewer digits. The final digits are then grouped as follows:

2 digits: A single block of length 2.
3 digits: A single block of length 3.
4 digits: Two blocks of length 2 each.
The blocks are then joined by dashes. Notice that the reformatting process should never produce any blocks of length 1 and produce at most two blocks of length 2.

Return the phone number after formatting.
'''
class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(' ', '')
        number = number.replace('-', '')
        number = [c for c in number]
        n = len(number)
        stop_ind = n - (n % 3) - (3 if n % 3 != 2 else 0)-1
        for i in range(stop_ind, 0, -3):
            number.insert(i+1, '-')
        if n % 3 == 1:
            number.insert(-2, '-')
        return ''.join(number)