'''
There are numBottles water bottles that are initially full of water. You can exchange numExchange empty water bottles from the market with one full water bottle.

The operation of drinking a full water bottle turns it into an empty bottle.

Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.
'''
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        numEmpties = 0
        total = 0
        while numBottles > 0 or numEmpties > numExchange:
            total += numBottles
            numEmpties += numBottles % numExchange
            numBottles //= numExchange
            numBottles += (numEmpties // numExchange)
            numEmpties %= numExchange
        return total
        
