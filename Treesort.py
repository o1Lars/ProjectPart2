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
tree.insert(1)
tree.insert(2)
tree.insert(0)
tree.insert(-1)
tree.insert(-2)
tree.insert(30)

print(tree.root.key)
print(tree.root.left.key)
print(tree.root.right.key)
print(tree.root.right.right.key)
print(tree.root.left.left.key)
print(tree.root.left.left.left.key)
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