'''
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you do not have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.
'''
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5: 0, 10:0, 20: 0}
        for b in bills:
            if b == 5:
                change[5] += 1
            if b == 10:
                if change[5] == 0:
                    return False
                change[5] -= 1
                change[10] += 1
            if b == 20:
                if change[5] >= 3 or (change[10] >= 1 and change[5] >= 1):
                    if change[10] >= 1:
                        change[10] -= 1
                        change[5] -= 1
                    else:
                        change[5] -= 3
                else:
                    return False
        return True
