class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head
    
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev

head = ListNode(1)
head.next = ListNode(2)

reversed_head = reverse_linked_list(head)

current = reversed_head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")
