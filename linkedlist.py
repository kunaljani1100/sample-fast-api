from pymongo.common import validate_unicode_decode_error_handler


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

# Inserting into tail of linked list.
head = Node(1)
tail = head
tail.next = Node(2)
tail = tail.next
tail.next = Node(3)
tail = tail.next

# Inserting into head of linked list.
newNode = Node(4)
newNode.next = head
head = newNode

# Iterating through a linked list.

np = head
while np:
    print(np.value)
    np = np.next


