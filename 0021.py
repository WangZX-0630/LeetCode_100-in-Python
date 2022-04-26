# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1
        else:
            if list1.val <= list2.val:
                node = ListNode(val=list1.val, next=self.mergeTwoLists(list1.next, list2))
                return node
            else:
                node = ListNode(val=list2.val, next=self.mergeTwoLists(list1, list2.next))
                return node


if __name__ == '__main__':
    NodeList = []
    for i in range(5, 0, -1):
        if i == 5:
            Node = ListNode(val=i, next=None)
            NodeList.append(Node)
        else:
            Node = ListNode(val=i, next=NodeList[-1])
            NodeList.append(Node)
    list1 = NodeList[-1]
    NodeList2 = []
    for i in range(3, 0, -1):
        if i == 3:
            Node = ListNode(val=i, next=None)
            NodeList2.append(Node)
        else:
            Node = ListNode(val=i, next=NodeList2[-1])
            NodeList2.append(Node)
    list2 = NodeList2[-1]

    head = NodeList[-1]

    solution = Solution()
    out_list = solution.mergeTwoLists(list1, list2)
    cur_Node = out_list
    while(cur_Node != None):
        print(cur_Node.val)
        cur_Node = cur_Node.next

