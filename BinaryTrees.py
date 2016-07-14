class BinaryTree(object):
    """"Binary Tree"""

    def __init__(self, data):

        self.root = Node(data)

    def insert(self, data):
        """Inserts the new nodes into the Binary Tree"""

        current_node = self.root

        while True:

            if data == current_node:
                return

            elif data > current_node.data:
                if current_node.right is None:
                    current_node.right = Node(data)
                    return
                else:
                    current_node = current_node.right

            else:
                if current_node.left is None:
                    current_node.left = Node(data)
                    return
                else:
                    current_node = current_node.left


class Node(object):

    """Nodes of a Binary Tree"""

    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None

    def size(self):

        """Returns the total number of nodes in the Tree."""

        total = 1

        if self.right is not None:
            total += self.right.size()

        if self.left is not None:
            total += self.left.size()

        return total

    def sum(self):

        """Returns the sum of the values in a Tree."""

        total = self.data

        if self.right is not None:
            total += self.right.sum()

        if self.left is not None:
            total += self.left.sum()

        return total
