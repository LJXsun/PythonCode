'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。


示例 1：

输入：s = "()"
输出：true
示例 2：

输入：s = "()[]{}"
输出：true
示例 3：

输入：s = "(]"
输出：false


提示：

1 <= s.length <= 104
s 仅由括号 '()[]{}' 组成

思路：
不能通过数量来进行判断，可能会出现 {(}) 这种情况，应该按照位置进行判断
其实就是栈的思想。


'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {'}': '{', ')': '(', ']': '['}
        stack = []
        for i in s:
            # 如果栈不为空且i属于dic中的键
            if stack and i in dic:
                if stack[-1] == dic[i]:
                    # 将stack栈（列表）最后一个元素去掉
                    stack.pop()
                else:
                    return False
            else:
                #栈为空或者不属于stack则执行这个操作
                stack.append(i)
        # 判断栈是否为空
        return not stack


s = input("s = ")
obj = Solution()
print(obj.isValid(s))
