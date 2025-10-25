class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
    
    
        """
        weeks, days = divmod(n, 7)
        total = 0
        # sum full weeks: each week starts at 1 + w and has 7 consecutive days
        for w in range(weeks):
            start = 1 + w
            # sum of start..start+6 = 7*start + 21
            total += 7 * start + 21
        # remaining days in the last (partial) week
        start = 1 + weeks
        for d in range(days):
            total += start + d
        return total

if __name__ == "__main__":
    n = int(input("Amit"))
    print(Solution().totalMoney(n))
