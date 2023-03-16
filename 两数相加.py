# Definition for singly-linked list.
class ListNode():
    def __init__(self, val):
        if isinstance(val, int):
            self.val = val
            self.next = None

        elif isinstance(val, list):
            self.val = val[0]
            self.next = None
            cur = self
            for i in val[1:]:
                cur.next = ListNode(i)
                cur = cur.next

    def gatherAttrs(self):
        return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())

    def __str__(self):
        return self.__class__.__name__ + " {" + "{}".format(self.gatherAttrs()) + "}"


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(0)
        head = l3
        tmp = 0
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            ans = l1_val + l2_val + tmp
            tmp = ans // 10
            head.next = ListNode(ans % 10)
            head = head.next
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0
        if tmp:
            head.next = ListNode(1)
        return l3.next


if __name__ == '__main__':

    num = Solution()
    l1 = ListNode([2, 4, 3])
    l2 = ListNode([5, 6, 4])
    ans = num.addTwoNumbers(l1, l2)
    tmp = ans
    listnum = []
    while tmp:
        listnum.append(tmp.val)
        tmp = tmp.next
    
    print(listnum)