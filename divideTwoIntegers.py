class Solution(object):
    def divide(self, dividend, divisor):
        MAX_INT = 2147483647
        if divisor == 0:
            return MAX_INT
        if dividend == 0:
            return 0
        negative = (dividend > 0) ^ (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        ans = 0
        while dividend >= divisor:
            x = divisor
            i = 1
            while dividend >= x + x:
                x += x
                i += i
            dividend -= x
            ans += i
        ans = MAX_INT if not negative and ans > MAX_INT else ans
        return -ans if negative else ans
