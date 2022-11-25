'''
We distribute some number of candies, to a row of n = num_people people in the following way:

We then give 1 candy to the first person, 2 candies to the second person, and so on until we give n candies to the last person.

Then, we go back to the start of the row, giving n + 1 candies to the first person, n + 2 candies to the second person, and so on until we give 2 * n candies to the last person.

This process repeats (with us giving one more candy each time, and moving to the start of the row after we reach the end) until we run out of candies.  The last person will receive all of our remaining candies (not necessarily one more than the previous gift).

Return an array (of length num_people and sum candies) that represents the final distribution of candies.
'''
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        n = num_people
        m = (-1 + sqrt(1 + 8 * candies)) // (2 * n)
        remaining = int(candies - ((m*n)*(m*n + 1))//2)
        totals = [int((m * (m-1) // 2)*(n)+m*(i+1))  for i in range(n)]
        next_divy = int(m*n + 1)
        i = 0
        while remaining > 0:
            totals[i] += min(next_divy, remaining)
            remaining -= next_divy
            next_divy += 1
            i += 1
        return totals
