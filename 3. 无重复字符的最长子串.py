'''
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。



示例 1:

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。


提示：

0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成

思路：（滑动窗口）
问题：找得是无重复的最长字符串
那么可以一个一个去添加，如果出现重复就移动向右移动一下，也就是删除最左边的字符

'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        # 记录不重复字符的最长子串在字符串的哪个位置
        head = 0
        # 存在不重复字符的子串
        setlist = set()
        curlen = 0
        maxlen = 0
        for i in s:
            # 判断i是否已经在滑动窗口中了，如果已经在了，则删除最左边的字符，
            #删除完了，再看看是否还存在，直到i不存setlist中
            while i in setlist:
                setlist.remove(s[head])
                head += 1
                curlen -= 1
            # i不存在setlist中，将其添加进去
            setlist.add(i)
            curlen += 1
            # 更新一下无重复最长字符串的长度
            if curlen > maxlen:
                maxlen = curlen
        return maxlen


s = input("s = ")
solu = Solution()
print(solu.lengthOfLongestSubstring(s))

