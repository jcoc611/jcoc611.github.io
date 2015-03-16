"""Node in a binary tree"""


class BTNode:
    """Binary Tree node."""

    def __init__(self, data, left=None, right=None):
        """Create BT node with data and children left and right."""
        self.data, self.left, self.right = data, left, right

    def __repr__(self):
        """Represent this node as a string."""
        return 'BTNode({}, {}, {})'.format(repr(self.data),
                                           repr(self.left),
                                           repr(self.right))

    def __str__(self):
        """Return a string representing self inorder"""
        return _str(self, '')

    def is_leaf(self):
        """Is this node a leaf?"""
        return self and not self.left and not self.right

    def height(self):
        """Return height of this tree."""
        return _height(self)


def _str(b, i):
    """Return a string representing b inorder,
    indent by i"""
    return ((_str(b.right, i + '    ') if b.right else '') +
            i + str(b.data) + '\n' +
            (_str(b.left, i + '    ') if b.left else ''))


"""binary search tree ADT"""


class BST:
    """Binary search tree."""

    def __init__(self, root=None):
        """Create BST with BTNode root."""
        self._root = root

    def __repr__(self):
        """Represent this binary search tree."""
        return 'BST({})'.format(repr(self._root))

    def find(self, data):
        """Return node containing data, otherwise return None."""
        return _find(self._root, data)

    def insert(self, data):
        """Insert data, if necessary, into this tree.

        >>> b = BST()
        >>> b.insert(8)
        >>> b.insert(4)
        >>> b.insert(2)
        >>> b.insert(6)
        >>> b.insert(12)
        >>> b.insert(14)
        >>> b.insert(10)
        >>> b
        BST(BTNode(8, BTNode(4, BTNode(2, None, None), BTNode(6, None, None)),\
 BTNode(12, BTNode(10, None, None), BTNode(14, None, None))))
        """
        if(isinstance(data, list)):
            data.sort()
            midata = len(data) // 2
            self.insert(data[midata])
            # dd = 0
            if(len(data) > 1):
                self.insert(data[:midata])
            if(len(data) > 2):
                self.insert(data[midata + 1:])
        else:
            self._root = _insert(self._root, data)

    def delete(self, data):
        """Remove, if there, node containing data.

        >>> b = BST()
        >>> b.insert(8)
        >>> b.insert(4)
        >>> b.insert(2)
        >>> b.insert(6)
        >>> b.insert(12)
        >>> b.insert(14)
        >>> b.insert(10)
        >>> b.delete(12)
        >>> b
        BST(BTNode(8, BTNode(4, BTNode(2, None, None), BTNode(6, None, None)),\
 BTNode(10, None, BTNode(14, None, None))))
        >>> b.delete(14)
        >>> b
        BST(BTNode(8, BTNode(4, BTNode(2, None, None), BTNode(6, None, None)),\
 BTNode(10, None, None)))
        """
        self._root = _delete(self._root, data)

    def delete_balanced(self, data):
        """Remove, if there, node containing data.

        >>> b = BST()
        >>> b.insert([2, 4, 6, 8, 10, 12, 14])
        >>> b
        BST(BTNode(8, BTNode(4, BTNode(2, None, None), BTNode(6, None, None)),\
 BTNode(12, BTNode(10, None, None), BTNode(14, None, None))))
        >>> b.delete_balanced(8)
        >>> b
        BST(BTNode(10, BTNode(4, BTNode(2, None, None), BTNode(6, None, None)),\
 BTNode(12, None, BTNode(14, None, None))))
        >>> b.delete_balanced(10)
        >>> b.delete_balanced(12)
        >>> b
        BST(BTNode(6, BTNode(4, BTNode(2, None, None), None), BTNode(14, None,\
 None)))
        """
        self._root = _delete_balanced(self._root, data)

    def height(self):
        """Return height of this tree."""
        return _height(self._root)


def _insert(node, data):
    """Insert data in BST rooted at node, if necessary, and return root."""
    return_node = node
    if not node:
        return_node = BTNode(data)
    elif data < node.data:
        node.left = _insert(node.left, data)
    elif data > node.data:
        node.right = _insert(node.right, data)
    else:  # nothing to do
        pass
    return return_node


def _find(node, data):
    """Return the node containing data, or else None."""
    if not node or node.data == data:
        return node
    else:
        return (_find(node.left, data) if (data < node.data)
                else _find(node.right, data))


def _delete(node, data):
    """Delete, if exists, node with data and return resulting tree."""
    # Algorithm for _delete:
    # 1. If this node is None, return that
    # 2. If data is less than node.data, delete it from left child and
    #     return this node
    # 3. If data is more than node.data, delete it from right child
    #     and return this node
    # 4. If node with data has fewer than two children,
    #     and you know one is None, return the other one
    # 5. If node with data has two non-None children,
    #     replace data with that of its largest child in the left subtree,
    #     and delete that child, and return this node
    return_node = node
    if not node:
        pass
    elif data < node.data:
        node.left = _delete(node.left, data)
    elif data > node.data:
        node.right = _delete(node.right, data)
    elif not node.left:
        return_node = node.right
    elif not node.right:
        return_node = node.left
    else:
        node.data = _find_max(node.left).data
        node.left = _delete(node.left, node.data)
    return return_node


def _delete_balanced(node, data):
    """Delete, if exists, node with data and return resulting tree."""
    # Algorithm for _delete:
    # 1. If this node is None, return that
    # 2. If data is less than node.data, delete it from left child and
    #     return this node
    # 3. If data is more than node.data, delete it from right child
    #     and return this node
    # 4. If node with data has fewer than two children,
    #     and you know one is None, return the other one
    # 5. If node with data has two non-None children,
    #     replace data with that of its largest child in the left subtree,
    #     and delete that child, and return this node
    return_node = node
    if not node:
        pass
    elif data < node.data:
        node.left = _delete(node.left, data)
    elif data > node.data:
        node.right = _delete(node.right, data)
    elif not node.left:
        return_node = node.right
    elif not node.right:
        return_node = node.left
    else:
        left_size = node.left.height()
        right_size = node.right.height()
        if(left_size > right_size):
            node.data = _find_max(node.left).data
            node.left = _delete(node.left, node.data)
        else:
            node.data = _find_min(node.right).data
            node.right = _delete(node.right, node.data)
    return return_node


def _find_max(node):
    """Find and return maximal node, assume node is not None"""
    return _find_max(node.right) if node.right else node


def _find_min(node):
    """Find and return minimal node, assume node is not None"""
    return _find_min(node.left) if node.left else node


def _height(node):
    """Return height of tree rooted at node."""
    return 1 + max(_height(node.left), _height(node.right)) if node else -1


def contains(node, value):
    ''' (BTNode, object) -> value

    Return whether tree rooted at node contains value.

    >>> contains(None, 5)
    False
    >>> contains(BTNode(5, BTNode(7), BTNode(9)), 7)
    True
    '''
    if node is None:
        return False
    else:
        return (node.data == value or
                contains(node.left, value) or
                contains(node.right, value))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    number_list = list(range(500))
    # add code here to build a BST containing
    # the numbers from number_list
    tree = BST()
    # for number in number_list:
    #     tree.insert(number)
    tree.insert(number_list)
    print(tree.height())

    with open('sample1.txt', 'r') as file_name:
        word_list = file_name.read().split()
    # add code here to build a BST containing
    # the strings from word_list
    tree2 = BST()
    tree2.insert(word_list)
    print(tree2.height())
