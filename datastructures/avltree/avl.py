import sys
import math


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
        if node.is_left_child:
            node.parent.left = node.right
        if node.is_right_child:
            node.parent.right = node.right
        # When doing left rotating, the child being lifted would be the right child. Vice versa.
        lifted_child = node.ch[direction ^ 1]
        lifted_child.parent = node.parent
        node.parent = lifted_child
        node.right = lifted_child.ch[direction]
        lifted_child.ch[direction] = node
        node.update_depth()
        lifted_child.update_depth()

    @classmethod
    def rebalance(cls, node):
        heavy_branch, depth_left, depth_right = cls.get_heavy_branch(node)
        if math.abs(depth_right - depth_left) <= 1:
            # It's balanced in its own level. There is no need to rebalance.
            return
        heavy_branch_next_level, _1, _2 = cls.get_heavy_branch(node.ch[heavy_branch])
        heavy_branch_root = node.ch[heavy_branch]
        zigzag = heavy_branch_next_level == heavy_branch # is it a zigzag case?
        if zigzag:
            cls.rotate(heavy_branch_root, direction=heavy_branch)
        cls.rotate(node, direction=heavy_branch ^ 1)

    @classmethod
    def get_heavy_branch(cls, node):
        depth_left = cls.get_depth(node.ch[LEFT])
        depth_right = cls.get_depth(node.ch[RIGHT])
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
        self._depth = max(AVLNode.get_depth(self.ch[LEFT]),
                AVLNode.get_depth(self.ch[RIGHT])) + 1

    @property
    def is_left_child(self):
        return self.parent is not None and self.parent.ch[LEFT] is self

    @property
    def is_right_child(self):
        return self.parent is not None and self.parent.ch[RIGHT] is self


class AVL(object):
    def __init__(self):
        self.root = None

    def insert(self, num):
        if self.root is None:
            self.root = AVLNode(num=num)
            return
        cursor = self.root
        parent = None
        while cursor is not None:
            if cursor.num == num:
                cursor.occurence += 1
                return
            elif cursor.num > num:
                parent = cursor
                cursor = cursor.ch[LEFT]
            else:
                parent = cussor
                cursor = cursor.ch[RIGHT]
        new_node = AVLNode(num=num, parent=parent)
        if num > parent.num:
            parent.ch[RIGHT] = new_node
        else:
            parent.ch[LEFT] = new_node
        return new_node

