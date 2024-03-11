class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_elements(head, val):
    dummy = ListNode(0)
    dummy.next = head
    prev, current = dummy, head
    
    while current:
        if current.val == val:
            prev.next = current.next
        else:
            prev = current
        current = current.next
    
    return dummy.next

head = ListNode(7)
head.next = ListNode(7)
head.next.next = ListNode(7)
head.next.next.next = ListNode(7)

val = 7
head = remove_elements(head, val)

print(head)
