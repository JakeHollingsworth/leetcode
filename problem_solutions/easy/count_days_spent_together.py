'''
Alice and Bob are traveling to Rome for separate business meetings.

You are given 4 strings arriveAlice, leaveAlice, arriveBob, and leaveBob. Alice will be in the city from the dates arriveAlice to leaveAlice (inclusive), while Bob will be in the city from the dates arriveBob to leaveBob (inclusive). Each will be a 5-character string in the format "MM-DD", corresponding to the month and day of the date.

Return the total number of days that Alice and Bob are in Rome together.

You can assume that all dates occur in the same calendar year, which is not a leap year. Note that the number of days per month can be represented as: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31].
'''
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        def date_strings_to_start_day(date_string):
            days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            arrive_month, arrive_day = int(date_string[:2])-1, int(date_string[3:])
            return sum(days_per_month[:arrive_month]) + arrive_day
        
        arrive_bob_day = date_strings_to_start_day(arriveBob)
        leave_bob_day = date_strings_to_start_day(leaveBob)
        arrive_alice_day = date_strings_to_start_day(arriveAlice)
        leave_alice_day = date_strings_to_start_day(leaveAlice)
        arrive_day, leave_day = max(arrive_bob_day, arrive_alice_day), min(leave_bob_day, leave_alice_day)
        return max(0, leave_day - arrive_day + 1)
