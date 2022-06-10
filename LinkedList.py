class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'[val={self.val}, next: {str(self.next)}]'


def create_linked_list(nodes):
    head = None
    if nodes:
        head = ListNode(nodes[0])
    pointer = head
    for n in nodes[1:]:
        pointer.next = ListNode(n)
        pointer = pointer.next
    return head


class Solution:
    def mergeTwoLists(self, list1, list2):
        merged = ListNode()
        head = merged
        while list1 and list2:
            print(list1.val, list2.val, merged.val, head.val)
            if list1.val < list2.val:
                merged.next = list1
                list1 = list1.next
            else:
                merged.next = list2
                list2 = list2.next
            merged = merged.next
        if list1:
            merged.next = list1
        if list2:
            merged.next = list2
        return head.next


if __name__ == '__main__':
    list1, list2 = [1, 2, 3], [1, 2, 4]
    list1 = create_linked_list(list1)
    list2 = create_linked_list(list2)
    s = Solution()
    print(s.mergeTwoLists(list1, list2))