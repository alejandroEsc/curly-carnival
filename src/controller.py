from .node import Node


class Controller(object):
    '''
    The Controller class manages a chain of Nodes

    root: The 1st Node in the chain
    tail: The last Node in the chain
    '''
    root = None
    tail = None

    def add(self, name, weight=None):
        '''
        add a Node to the end of the chain

        name: a name for the new Node
        weight (optional): a weight to assign to the new Node
                           if no weight is passed, one greater than
                           the max weight will be used.
        '''
        # create a tailing weight if weight is None
        if weight is None:
            try:
                weight = self.tail.weight + 1
            except AttributeError:
                weight = 1
        return self._insert(name, weight)

    def _insert(self, name, weight):
        '''
        _insert inserts a new node into the chain
        '''
        new_node = Node(name, weight)
        new_tail = False

        # if there are no nodes yet
        if self.root is None:
            self.root = new_node
            self.tail = new_node
            return True

        # if this is going to be the new tail
        if weight > self.tail.weight:
            parent = self.tail
            new_tail = True
        # otherwise, find the new parent
        else:
            parent = self.root
            node = self.root
            while node is not None:
                if node.weight > weight:
                    parent = node.left
                    break
                node = node.right

        try:
            # insert the new node after the chosen parent
            new_node.insert_after(parent)
        except AssertionError:
            return False
        if new_tail:
            self.tail = new_node
        return True

    def fetch(self, name):
        '''
        fetch a node by name
        '''
        node = self.root
        while node is not None:
            if node.name == name:
                return node
            node = node.right
        return None

    def dump(self, printout=False):
        '''
        dump the chain of Nodes as a list of dicts

        printout(optional): print the nodes to stdout
        '''
        result = []

        node = self.root
        while node is not None:
            result.append(node.dict())
            if printout:
                print('Node "{name}": {weight}'.format_map(node.dict()))
            node = node.right
        return result

    def print_ordered_names(self, printout=True):
        '''
        print a space separated list of Nodes by order of weight to stdout
        '''
        result = ' '.join([x['name'] for x in self.dump()])
        if printout:
            print(result)
        return result
