# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head == None or head.next == None:
            return None
        cur_Node = head
        length = 1

        while(cur_Node.next != None):
            cur_Node = cur_Node.next
            length += 1

        LeftNode = head
        for i in range(length - n - 1):
            LeftNode = LeftNode.next
        if n == 1:
            LeftNode.next = None
        elif n == length:
            head = LeftNode.next
        else:
            LeftNode.next = LeftNode.next.next

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
    head = NodeList[-1]
    cur_Node = head
    for j in range(5):
        print(cur_Node.val)
        cur_Node = cur_Node.next

    solution = Solution()
    head = solution.removeNthFromEnd(head, 4)
    cur_Node = head
    while(cur_Node != None):
        print(cur_Node.val)
        cur_Node = cur_Node.next


