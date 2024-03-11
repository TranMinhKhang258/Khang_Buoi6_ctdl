class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_palindrome(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    
    return values == values[::-1]

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)

print(is_palindrome(head))  
