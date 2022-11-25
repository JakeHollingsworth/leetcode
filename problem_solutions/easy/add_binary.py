'''
Given two binary strings a and b, return their sum as a binary string.
'''
class Solution:
    '''
    To me, it seems as though the problem does not want you to convert to integers, and so used boolean arithmetic in place of 
    casting to ints.
    '''
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]
        a,b = (a,b) if len(a) > len(b) else (b,a)
        carry = "0"
        result = ""
        for i in range(len(b)):
            total = (a[i] == "1") + (b[i] == "1") + (carry == "1")
            if total == 3:
                result = result + "1"
                carry = "1"
            elif total == 2:
                result = result + "0"
                carry = "1"
            elif total == 1:
                result = result + "1"
                carry ="0"
            else:
                result = result + "0"
                carry == "0"
        for i in range(len(b), len(a)):
            total = (a[i] == "1") + (carry == "1")
            if total == 2:
                result = result + "0"
                carry = "1"
            elif total == 1:
                result = result + "1"
                carry ="0"
            else:
                result = result + "0"
                carry = "0"
        if carry == "1":
            result = result + "1"
        return result[::-1]
   
