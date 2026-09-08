class Solution:
    def countCommas(self, n: int) -> int:
        l=len(str(n))
        if l<=3:
            return 0
        else:
            return n-999

