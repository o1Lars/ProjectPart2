"""
This module implements the algorithm Treesort.py. It utilizes the funtionality of DictBinTree.py from module
DictBinTree.py. The algorithm takes multiple inserts into the data structure and finally prints the values in order.

Requirements
------------
Python 3.7 or higher.
DictBinTree.py

Notes
-----
Module is created as part of the group project for the final exam of DS814 Algoritmer og Datastrukturer forår 2024.

Projektgrupe:
Chris Thorbjørn Eichmuller Vandborg
cvand15@student.sdu.dk

Lars Mogensen
lmoge23@student.sdu.dk
"""

import sys
import DictBinTree

tree = DictBinTree.DictBinTree()

n = 0

for line in sys.stdin:
    tree.insert(int(line))
    n = n+1

tree_keys_ordered = tree.orderedTraversal()

for key in tree_keys_ordered:
    print(key)
