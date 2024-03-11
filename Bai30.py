class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_sorted_lists(list1, list2):
    dummy = ListNode()  
    current = dummy
    
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    if list1:
        current.next = list1
    if list2:
        current.next = list2
    
    return dummy.next

list1 = []

list2 = []
merged_head = merge_sorted_lists(list1, list2)

current = merged_head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")
