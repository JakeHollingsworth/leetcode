'''
You are given an integer array ranks and a character array suits. You have 5 cards where the ith card has a rank of ranks[i] and a suit of suits[i].

The following are the types of poker hands you can make from best to worst:

"Flush": Five cards of the same suit.
"Three of a Kind": Three cards of the same rank.
"Pair": Two cards of the same rank.
"High Card": Any single card.
Return a string representing the best type of poker hand you can make with the given cards.

Note that the return values are case-sensitive.
'''
class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if suits.count(suits[0]) == 5:
            return "Flush"
        elif any([count >= 3 for count in Counter(ranks).values()]):
            return "Three of a Kind"
        elif any([count >= 2 for count in Counter(ranks).values()]):
            return "Pair"
        else:
            return "High Card"
