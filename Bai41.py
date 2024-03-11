class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_palindrome(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second_half_head = reverse_linked_list(slow)
    
    while second_half_head:
        if head.val != second_half_head.val:
            return False
        head = head.next
        second_half_head = second_half_head.next
    
    return True

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

print(is_palindrome(head))  
