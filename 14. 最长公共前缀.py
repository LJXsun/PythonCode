'''
14. 最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。



示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"
示例 2：

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。


提示：

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] 仅由小写英文字母组成

思路：
利用zip压缩解压的特性，结合set进行比较
strs = ["flow","flower"]
经过zip[*strs]会生成一个可迭代对象
(f,f),(l,l),(o,o),(w,w),("",e),("",r)
利用set函数对比每个元组长度，如果是（f，f）则等于f
zip:
https://www.zhihu.com/tardis/bd/art/268377882
https://blog.csdn.net/qq_45766916/article/details/125960493
'''


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = ""
        for temp in zip(*strs):
            temp_set = set(temp)
            if len(temp_set) == 1:
                ans += temp[0]
            else:
                break
        return ans

'''
class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        if not s:
            return ""
        res = s[0]
        i = 1
        while i < len(s):
            while s[i].find(res) != 0:
                res = res[0:len(res)-1]
            i += 1
        return res
'''


strs0 = input("strs = ")
strs1 = strs0.lstrip('[')
strs2 = strs1.rstrip(']')
strs2 = strs2.split(",")
strs = []
for s in strs2:
    strs.append(s.strip('"'))
print(strs)
solut = Solution()
print(solut.longestCommonPrefix(strs))
