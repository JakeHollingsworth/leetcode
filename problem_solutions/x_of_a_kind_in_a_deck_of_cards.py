'''
In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.
'''
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        deck_dict = {}
        for card in deck:
            deck_dict[card] = deck_dict[card] + 1 if card in deck_dict else 1
        x = min([count for _, count in deck_dict.items()])
        primes = [x]
        for p in range(2, round(math.sqrt(x)) + 2):
            if not x % p:
                primes.append(p)
        return any([(all([not count % p for _, count in deck_dict.items()]) and p >= 2) for p in primes])
