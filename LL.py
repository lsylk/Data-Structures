class LinkedList(object):

    """LinkedList"""

    def __init__(self, data=None):

        self.head = Node(data)

    def insert(self, data):

        """Inserts a new node into the LinkedList"""

        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def get_head(self):

        """Returns the data at the head"""

        return self.head.data

    def len_of_LL(self):

        """Returns the length of the LinkedList"""

        # Starts counting from the head; therefore the total starts at 1.

        current = self.head

        total = 1

        while current.next is not None:

            current = current.next
            total += 1

        return total

    def print_values(self):

        """Prints all values in the LinkedList"""

        # Starts to print from the head of the LinkedList.
        current = self.head

        print current.data

        while current.next is not None:

            current = current.next
            print current.data

        return

    def reverse(self):

        """Reverses the LinkedList."""

        prev = None
        current = self.head

        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev

        return self.head


class Node(object):

    """Node in a LinkedList"""

    def __init__(self, data):

        self.data = data
        self.next = None
