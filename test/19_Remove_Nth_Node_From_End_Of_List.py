from copy import deepcopy

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        count = 0
        counter = head
        while(counter != None):
            count += 1
            counter = counter.next

        left = head
        right = left.next

        if count == n:
            head = head.next

        for i in range(0,count-n):
            if i == count - n - 1:
                left.next = right.next
            else:
                left = right
                right = left.next

        return head


def main():

    c = Solution()
    l = [1,2,3,4,5]
    n = 2
    l = [1]
    n = 1
    #l = [1,4,5,6,8,10,5,7]
    #n = 3
    head = ListNode(l[0])
    before = head
    for ll in l[1:]:
        after = ListNode(ll)
        before.next = after 
        before = after

    s_list = []
    before = head
    while(before != None):
        s_list.append(str(before.val))
        before = before.next
    print("->".join(s_list))

    result = c.removeNthFromEnd(head,n)

    s_list = []
    before = result
    while(before != None):
        s_list.append(str(before.val))
        before = before.next
    print("->".join(s_list))
    

if __name__ == "__main__":
    main()

