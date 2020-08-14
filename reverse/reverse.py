class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.value) + '--->'
            itr = itr.next_node

        print(llstr)

    def reverse_list(self, node, prev=None):
        itr = node

        while itr:
            next = itr.next_node
            itr.next_node = prev

            prev = itr
            itr = next


        self.head = prev

sll = LinkedList()
sll.add_to_head(4)
sll.add_to_head(3)
sll.add_to_head(2)
sll.add_to_head(1)
sll.print()
sll.reverse_list(sll.head)
sll.print()