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

tree = DictBinTree.DictBinTree(1)
tree.root.left = DictBinTree.BinNode(0)
tree.root.right = DictBinTree.BinNode(3)

print(tree.search(3))

"""
n = 0
for line in sys.stdin:
    PQHeap.insert(pq,int(line))
    n = n+1

print()
while n > 0:
    print(PQHeap.extractMin(pq))
    n = n-1
"""