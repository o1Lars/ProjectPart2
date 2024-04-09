import unittest
from DictBinTree import DictBinTree
from DictBinTree import BinNode

class DictBinTreeUnitTests(unittest.TestCase):

    def test_if_returns_empty_tree(self):
        myTree = DictBinTree()
        
        self.assertEqual(myTree.root.key, None)
        self.assertEqual(myTree.root.left, None)
        self.assertEqual(myTree.root.right, None)

    def test_if_insert_inserts_as_expected(self):
        myTree = DictBinTree()
        rootBinNode = BinNode()
        rootBinNode.key = 10
        myTree.root = rootBinNode

        myBinNode = BinNode()
        myBinNode.key = 5
        myTree.insert(myBinNode)

        self.assertEqual(myTree.root.key, 10)
        self.assertEqual(myTree.root.left.key, 5)

    def test_ordered_traversal(self):
        myTree = DictBinTree()
        RootBinNode = BinNode()
        RootBinNode.key = 10
        myTree.root = RootBinNode
        BinNode1 = BinNode()
        BinNode1.key = 2
        BinNode2 = BinNode()
        BinNode2.key = 7
        BinNode3 = BinNode()
        BinNode3.key = 4
        BinNode4 = BinNode()
        BinNode4.key = 8
        BinNode5 = BinNode()
        BinNode5.key = 5
        BinNode6 = BinNode()
        BinNode6.key = 3

        myTree.insert(BinNode1)
        myTree.insert(BinNode2)
        myTree.insert(BinNode3)
        myTree.insert(BinNode4)
        myTree.insert(BinNode5)
        myTree.insert(BinNode6)
        mylist=[]

        myTree.orderedTraversal(myTree.root, mylist)
        self.assertEqual(mylist, [2, 3, 4, 5, 7, 8, 10])

if __name__ == '__main__':
    unittest.main()




