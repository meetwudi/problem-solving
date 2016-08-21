LEFT = 0
RIGHT = 1
ROTATE_LEFT = 0
ROTATE_RIGHT = 1


class AVLNode(object):
    def __init__(self, num, parent=None):
        self.ch = [None, None] # Children
        self.num = num
        self.parent = parent
        self.occurence = 1 # How many times the number appeared
        self._depth = 0

    @classmethod
    def rotate(cls, node, direction):
        """Apply rotation (ROTATE_LEFT or ROTATE_right) to a node.
        """
        # When doing left rotating, the child being lifted would be the right child. Vice versa.
        lifted_child = node.ch[direction ^ 1]
        if node.is_left_child:
            node.parent.left = lifted_child
        if node.is_right_child:
            node.parent.right = lifted_child
        lifted_child.parent = node.parent
        node.parent = lifted_child
        node.ch[direction ^ 1] = lifted_child.ch[direction]
        if node.ch[direction ^ 1] is not None:
            node.ch[direction ^ 1].parent = node
        lifted_child.ch[direction] = node

        node.update_depth_all_ancestors()

    @classmethod
    def rebalance(cls, node):
        heavy_branch, depth_left, depth_right = cls.get_heavy_branch(node)
        if abs(depth_right - depth_left) <= 1:
            # It's balanced in its own level. There is no need to rebalance.
            return
        if node.num == float('-inf'):
            # Do not rebalance fake root
            return
        heavy_branch_next_level, _1, _2 = cls.get_heavy_branch(node.ch[heavy_branch])
        heavy_branch_root = node.ch[heavy_branch]
        zigzag = heavy_branch_next_level != heavy_branch # is it a zigzag case?
        if zigzag:
            cls.rotate(heavy_branch_root, direction=heavy_branch)
        cls.rotate(node, direction=heavy_branch ^ 1)

    @classmethod
    def get_heavy_branch(cls, node):
        depth_left = cls.get_depth(node.left)
        depth_right = cls.get_depth(node.right)
        if depth_right > depth_left:
            heavy_branch = RIGHT
        elif depth_right < depth_left:
            heavy_branch = LEFT
        else:
            heavy_branch = None
        return (heavy_branch, depth_left, depth_right, )

    @classmethod
    def get_depth(cls, node):
        return node._depth if node is not None else -1

    def update_depth(self):
        self._depth = max(AVLNode.get_depth(self.left),
                AVLNode.get_depth(self.right)) + 1

    def update_depth_all_ancestors(self):
        current = self
        while current:
            current.update_depth()
            current = current.parent

    @property
    def is_left_child(self):
        return self.parent is not None and self.parent.left is self

    @property
    def is_right_child(self):
        return self.parent is not None and self.parent.right is self

    @property
    def left(self):
        return self.ch[LEFT]

    @property
    def right(self):
        return self.ch[RIGHT]

    @left.setter
    def left(self, val):
        self.ch[LEFT] = val

    @right.setter
    def right(self, val):
        self.ch[RIGHT] = val

    def __repr__(self):
        return "AVLNode(num={0}, occurence={1}, depth={2})".format(
                self.num,
                self.occurence,
                AVLNode.get_depth(self))


class AVLTree(object):
    def __init__(self):
        self.root = AVLNode(num=float('-inf'))

    def insert(self, num):
        cursor = self.root.right
        parent = self.root
        ancestors = []
        while cursor is not None:
            if cursor.num == num:
                cursor.occurence += 1
                return
            ancestors.append(cursor)
            if cursor.num > num:
                parent = cursor
                cursor = cursor.left
            else:
                parent = cursor
                cursor = cursor.right

        new_node = AVLNode(num=num, parent=parent)
        if num > parent.num:
            parent.right = new_node
        else:
            parent.left = new_node

        ancestors.reverse()
        for node in ancestors:
            node.update_depth()
            AVLNode.rebalance(node)
        return new_node

    def traverse(self):
        def recursive_build_list(node, result):
            if node is None:
                return
            recursive_build_list(node.left, result)
            result.append(node.num)
            recursive_build_list(node.right, result)

        result = []
        recursive_build_list(self.root, result)
        return result[1:]

    @classmethod
    def serialize(cls, tree):
        def build_key_value_pairs(node, kv, key=1):
            if node is None:
                return
            kv[key] = (node.num, node.occurence, )
            build_key_value_pairs(node.left, kv, key << 1)
            build_key_value_pairs(node.right, kv, (key << 1) + 1)

        kv = {}
        build_key_value_pairs(tree.root.right, kv)
        max_key = max(list(kv))
        serialized_tree = [None] * (max_key + 1)
        for key, val in kv.items():
            serialized_tree[key] = val if val[1] > 1 else val[0]
        return serialized_tree[1:]

    @classmethod
    def deserialize(cls, serialized_tree):
        if not serialized_tree:
            return None
        serialized_tree = [None] + serialized_tree
        if type(serialized_tree[0]).__name__ == 'tuple':
            root = AVLNode(num=serialized_tree[1][0])
            root.occurence = serialized_tree[1][1]
        else:
            root = AVLNode(num=serialized_tree[1])
        nodes = [None, root]
        for i in xrange(2, len(serialized_tree)):
            if serialized_tree[i] is None:
                nodes.append(None)
                continue
            parent = nodes[i >> 1]
            if type(serialized_tree[i]).__name__ == 'tuple':
                node = AVLNode(num=serialized_tree[i][0], parent=parent)
                node.occurence = serialized_tree[i][1]
            else:
                node = AVLNode(num=serialized_tree[i], parent=parent)
            if i % 2 == 0:
                parent.left = node
            else:
                parent.right = node
            nodes.append(node)
        # update depth
        for i in xrange(len(nodes) - 1, -1, -1):
            if nodes[i] is not None:
                nodes[i].update_depth()
        tree = cls()
        tree.root.right = root
        root.parent = tree.root
        tree.root.update_depth()
        return tree

