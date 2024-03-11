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

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(6)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(6)

val = 6
head = remove_elements(head, val)

current = head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")
