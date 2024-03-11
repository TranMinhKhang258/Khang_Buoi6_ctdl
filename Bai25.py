class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def delete_node_at_index(self, index):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            deleted_node = self.head
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            deleted_node = current.next
            current.next = current.next.next
        self.length -= 1
        return deleted_node

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
print(linked_list) 
deleted_node = linked_list.delete_node_at_index(1)
print("Deleted node:", deleted_node.value)
print(linked_list)
