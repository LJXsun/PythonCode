"""
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

例如，121 是回文，而 123 不是。
"""


class Solution(object):
    def isPalindrome(self, x):
        x1 = str(x)
        x2 = x1[::-1]
        return x > -1 and x1 == x2


if __name__ == "__main__":
    so = Solution()
    num = int(input())
    print(so.isPalindrome(num))
