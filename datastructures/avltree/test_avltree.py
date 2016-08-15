import unittest

from unittest import TestCase
from avl import AVLNode
from avl import AVLTree
from avl import LEFT
from avl import RIGHT
from avl import ROTATE_LEFT
from avl import ROTATE_RIGHT


class AVLNodeTest(TestCase):
    def test_deserialize(self):
        serialized_tree = [3, 1, 5, None, None, 4, 6]
        tree = AVLTree.deserialize(serialized_tree)
        root = tree.root.right
        assert AVLTree.serialize(tree) == [3, 1, 5, None, None, 4, 6]
        assert root.num == 3
        assert root.occurence == 1
        assert root.left.num == 1
        assert root.right.num == 5
        assert root.right.left.num == 4
        assert root.right.right.num == 6
        assert AVLNode.get_depth(root) == 2
        assert AVLNode.get_depth(root.left) == 0

    def test_rotate(self):
        serialized_tree = [3, 1, 5, None, None, 4, 6]
        tree = AVLTree.deserialize(serialized_tree)
        actual_root = tree.root.right
        node5 = actual_root.right
        AVLNode.rotate(node5, ROTATE_LEFT)
        assert AVLTree.serialize(tree) == [3, 1, 6, None, None, 5, None, None, None, None, None, 4]
        assert AVLNode.get_depth(actual_root) == 3
        assert AVLNode.get_depth(actual_root.right) == 2
        assert AVLNode.get_depth(actual_root.right.left) == 1
        node6 = actual_root.right
        AVLNode.rotate(node6, ROTATE_RIGHT)
        assert AVLTree.serialize(tree) == [3, 1, 5, None, None, 4, 6]

    def test_rotate_actual_root(self):
        serialized_tree = [3, 1, 5, None, None, 4, 6]
        tree = AVLTree.deserialize(serialized_tree)
        actual_root = tree.root.right
        AVLNode.rotate(actual_root, ROTATE_RIGHT)
        assert AVLTree.serialize(tree) == [1, None, 3, None, None, None, 5, None,
                None, None, None, None, None, 4, 6]

    def test_rebalance_regular_case_simple(self):
        serialized_tree = [3, 2, None, 1]
        tree = AVLTree.deserialize(serialized_tree)
        actual_root = tree.root.right
        AVLNode.rebalance(actual_root)
        assert AVLTree.serialize(tree) == [2, 1, 3]

    def test_rebalance_regular_case_simple_2(self):
        serialized_tree = [1, None, 2, None, None, None, 3]
        tree = AVLTree.deserialize(serialized_tree)
        actual_root = tree.root.right
        AVLNode.rebalance(actual_root)
        assert AVLTree.serialize(tree) == [2, 1, 3]

    def test_rebalance_zigzag_case_simple(self):
        serialized_tree = [3, 1, None, None, 2]
        tree = AVLTree.deserialize(serialized_tree)
        actual_root = tree.root.right
        AVLNode.rebalance(actual_root)
        assert AVLTree.serialize(tree) == [2, 1, 3]


if __name__ == '__main__':
    unittest.main()
