class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_duplicates(head):
    if not head:
        return head
    
    seen = set()
    current = head
    previous = None
    
    while current:
        if current.val in seen:
            previous.next = current.next
        else:
            seen.add(current.val)
            previous = current
        current = current.next
    
    return head

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(4)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(2)

head = remove_duplicates(head)

current = head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")
