# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        heap = []
        for i in range(len(lists)):
            while lists[i] is not None:
                heapq.heappush(heap, lists[i].val)
                lists[i] = lists[i].next
        if len(heap) == 0:
            return None
        head = ListNode(val=heapq.heappop(heap))
        cur_node = head
        for j in range(len(heap)):
            cur_node.next = ListNode(val=heapq.heappop(heap))
            cur_node = cur_node.next
        return head


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

    solution = Solution()
    out_list = solution.mergeKLists([list1, list2])
    cur_Node = out_list
    while (cur_Node != None):
        print(cur_Node.val)
        cur_Node = cur_Node.next
