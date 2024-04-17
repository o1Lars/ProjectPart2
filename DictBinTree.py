from __future__ import annotations
"""
This module provides DictBinTree, which is a class that constructs the data structure binary search tree with numbers as keys.
The class provides:
 - T.search(k), returns a bolean that return k's placement in the tree
 - T.insert(k), which inserts key k in the tree T
 - T.orderedTraversal(), which returns a list of keys in the tree T in sorted order.

Requirements
------------
Python 3.7 or higher.

Notes
-----
Module is created as part of the group project for the final exam of DS814 Algoritmer og Datastrukturer forår 2024.

Projektgrupe:
Chris Thorbjørn Eichmuller Vandborg
cvand15@student.sdu.dk

Lars Mogensen
lmoge23@student.sdu.dk


"""

class DictBinTree:
    """Constructs an unstructured binary search tree data structure intance."""

    def __init__(self, root: int = None) -> None:
        """
        Parameters
        ----------
        root: int, default = None
            represents the root node of the binary tree. If nothing is provided, root is None and tree is empty.
        """
        self.root = BinNode(root)

        #for key in keys:
        #self.root = DictBinTree.insert(self.root, key)

    # Public methods for the binary search tree
    def search(self, k: int) -> bool:
        """Return true if the k key is in the binary search tree

        Parameters
        ----------
        k: int
            k is an integer value key
        """
        if self.root.key == None:
            return False
        elif self._search(self.root, k):
            return True
        else:
            return False

    def insert(self, k: int) -> None:
        """Creates and inserts a new node with key k into the binary search tree

        Parameters
        ----------
        k, int:
            An integer value
        """

        # Create instance of subtree
        z = BinNode(k)
        z.left = BinNode()
        z.right = BinNode()

        self._insert(z)

    def orderedTraversal(self) -> list[int]:
        """Returns a list of keys from the binary search tree in ascending order"""

        keys_list = []

        keys_list.append(self._orderedTraversal())

        return keys_list

    # private methods for the binary search tree
    def _search(self, x: BinNode, k: int) -> BinNode:
        """Return a pointer to a node with key k if one exists in the subtree

        Parameters
        ----------
        x, BinNode
            A pointer to a subtree
        k: int
            k is an integer value key
        """

        # base case
        if x is None or k == x.key:
            return x

        # Recursively search tree
        if k < x.key:
            return self._search(x.left, k)
        else:
            return self._search(x.right, k)

    def _insert(self, z: BinNode) -> None:
        """Insert node z into binary search tree

        Parameters
        ----------
        z, BinNode:
            Node for which key is to be inserted into binary search tree
        """

        x = self.root       # Node being compared with z
        y = None            # y will be parent of z

        while x.key is not None:        # descend until reaching a leaf
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def _orderedTraversal(self):
        """"""
        if Node != None:
            self.orderedTraversal(Node.left, mylist)
            mylist.append(Node.key)
            self.orderedTraversal(Node.right, mylist)
            return mylist

    #skal have følgende metodekald:
    #T.search() som returnerer en boolean
    #T.insert(), der indsætter nøglen K i træet T
    # - Opretter ét nyt objekt af typen BinNode oprettes
    #T.OrderedTraversal() returnerer en liste med nøglerne i træet T i sorteret orden (fremfor at printe dem på skærmen som i bogens kode)
    # Vigtigt: Træet skal IKKE holdes balanceret (brug ikke metoder fra kapital 13)
    #et objekt af denne skal indeholde BinNode
    # dvs ét objekt af DictBinTree og dets rod svarer til T og T.root fra bogen.
    # hvert træ består derfor af ét objekt (DictBinTree) og nul eller flere objekter af BinNodes. 


class BinNode:
    """Creates a node/subtree with a key and the left and right child of the node"""
    def __init__(self, key: int=None):
        """
        Parameters
        ----------
        key, int=None
            The key value of the node
        """
        self.key = key
        self.left = None
        self.right = None

    #skal bruges til at repræsentere knuder i træer
    #du skal ikke bruge array struktur
    #skal indeholde to andre BinNodes (knudens venstre og højre børn), med værdi None hvis barnet ikke findes.
    # skal også indeholde nøgle K, men ikke nødvendigt med forælder i dette projekt
    #
