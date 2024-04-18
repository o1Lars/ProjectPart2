import unittest
from DictBinTree import DictBinTree
from DictBinTree import BinNode

class DictBinTreeUnitTests(unittest.TestCase):

    # def test_if_returns_empty_tree(self):
    #     myTree = DictBinTree()
        
    #     self.assertEqual(myTree.root.key, None)
    #     self.assertEqual(myTree.root.left, None)
    #     self.assertEqual(myTree.root.right, None)

    # def test_if_insert_inserts_as_expected(self):
    #     myTree = DictBinTree()
    #     rootBinNode = BinNode()
    #     rootBinNode.key = 10
    #     myTree.root = rootBinNode

    #     myTree.insert(5) ## adds left to parent

    #     self.assertEqual(myTree.root.key, 10)
    #     self.assertEqual(myTree.root.left.key, 5)

    #     myTree.insert(12) ## adds right to parent

    #     self.assertEqual(myTree.root.key, 10)
    #     self.assertEqual(myTree.root.right.key, 12)

    #     myTree.insert(8) ## adds right to the left child

    #     self.assertEqual(myTree.root.key, 10)
    #     self.assertEqual(myTree.root.left.right.key, 8)

    #     myTree.insert(10) ## inserts a duplicate

    #     self.assertEqual(myTree.root.key, 10)
    #     self.assertEqual(myTree.root.left.key, 5)
    #     self.assertEqual(myTree.root.left.right.key, 8)
    #     self.assertEqual(myTree.root.left.left, None)

    #     self.assertEqual(myTree.root.right.key, 12)
    #     self.assertEqual(myTree.root.right.right, None)
    #     self.assertEqual(myTree.root.right.left.key, 10)




    def test_ordered_traversal(self):
        myTree = DictBinTree()
        RootBinNode = BinNode(10)
        myTree.root = RootBinNode
      
        myTree.insert(2)
        myTree.insert(7)
        myTree.insert(4)
        myTree.insert(8)
        myTree.insert(5)
        myTree.insert(3)

        self.assertEqual(myTree.orderedTraversal(), [2, 3, 4, 5, 7, 8, 10])

if __name__ == '__main__':
    unittest.main()




