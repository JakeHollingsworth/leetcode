'''
A password is said to be strong if it satisfies all the following criteria:

It has at least 8 characters.
It contains at least one lowercase letter.
It contains at least one uppercase letter.
It contains at least one digit.
It contains at least one special character. The special characters are the characters in the following string: "!@#$%^&*()-+".
It does not contain 2 of the same character in adjacent positions (i.e., "aab" violates this condition, but "aba" does not).
Given a string password, return true if it is a strong password. Otherwise, return false.
'''
class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        digits = '0123456789'
        lowers = 'abcdefghijklmnopqrstuvwxyqz'
        uppers = lowers.upper()
        special = '!@#$%^&*()-+'
        num_digits, num_lowers, num_uppers, num_specials = 0,0,0,0
        for i,c in enumerate(password):
            if (i and password[i-1] == c) or len(password) < 8:
                return False
            if c in digits:
                num_digits += 1
            elif c in lowers:
                num_lowers += 1
            elif c in uppers:
                num_uppers += 1
            elif c in special:
                num_specials += 1
        return all(n for n in [num_digits, num_lowers, num_uppers, num_specials])
