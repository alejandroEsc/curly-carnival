class Node(object):
    '''
    The Node class defined a weighted node object.

    name: The name of the Node
    weight: An integer weight assigned to self Node
    left: a Node with a lower weight than self Node or None if there is no left neighbor
    right: a Node with a greater weight than self Node or None if there is no right neighbor
    '''

    name = None
    weight = None
    left = None
    right = None

    def __init__(self, name, weight=0):
        '''
        Initialize Node

        name is the name assigned to self node
        weight is the weight assigned to self node

        If inserted into a tree of nodes, name and weight must be unique
        '''
        assert isinstance(name, str), "name is not a string: {0}".format(name)
        assert isinstance(weight, int), "weight is not an integer: {0}".format(weight)
        self.name = name
        self.weight = weight

    def _test_unique_name(self, left, right):
        '''
        Test to see if self name is unique to the tree

        return True if unique, False if not
        '''
        # Walk the tree backwards than forward to ensure self name is unique
        if left is not None:
            inspect = left
            while inspect is not None:
                if inspect.name == self.name:
                    return False
                inspect = inspect.left
        if right is not None:
            inspect = right
            while inspect is not None:
                if inspect.name == self.name:
                    return False
                inspect = inspect.right
        return True

    def insert_after(self, left):
        '''
        Insert self node into a tree of Nodes

        left: Insert self node after self passed Node

        '''
        assert isinstance(left, Node), "left is not an integer: {0}".format(left)
        right = left.right
        assert left is None or left.weight < self.weight, "Cannot insert. This Node's weight {0} must be greather than {1}".format(self.weight, left.weight)
        assert right is None or right.weight > self.weight, "Cannot insert. This Node's weight {0} must be less than {1}".format(self.weight, right.weight)
        assert self._test_unique_name(left, right) is True, "Name, {0} is not unique to self tree. Node cannot be inserted".format(self.name)

        # insert self node into the tree
        self.left = left
        self.right = right
        if right is not None:
            right.left = self

        return True

if __name__ == "__main__":
    node_a = Node('node_a', 3)
    node_b = Node('node_b', 5)
    node_b.insert_after(node_a)
    print("Success")
