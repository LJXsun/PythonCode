'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。
示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]
提示：
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
只会存在一个有效答案

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/two-sum

注意：要排除两个数的下标一样的情况
6,[3,2,4]
答案：
[1,2]
而不是
[0,0]
'''
def twoSum(nums,target):
    hashmap = {}
    for i,num in enumerate(nums):
        if hashmap.get(target - num) is not None: #字典的get函数获取某键的值，如不存在则None
            return [hashmap.get(target - num),i]
        hashmap[num] = i


if __name__ == '__main__':
    target = 6
    nums = [3,2,4]
    print(twoSum(nums,target))
'''
知识拓展——=、==和is的区别
1、=在任何编程语言中都是赋值，赋值是引用，引用是引用内存地址。
2、==是比较两个值是否相等，比较的是两个对象的内容是否相等，即内存地址可以不同，内容相同就行。
3、 is是比较两个实例对象是不是完全相同，它们是不是同一个对象，即id是不是相同，是不是占用同一块内存空间。
4、 is 运算符比==效率高，在变量和None进行比较时，应该使用is。
enumerate用法看语雀
'''