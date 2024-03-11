class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_elements(head, val):
    if not head:
        return None
    
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

head = None

val = 1
head = remove_elements(head, val)

print(head)
