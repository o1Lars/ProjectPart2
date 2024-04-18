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
numbers = []
while True:
    try:
        myInput = input()
        if myInput == "":
            break
        numbers.append(int(myInput))
    except EOFError as e:
        print(e)

for num in numbers:
    print(num)

    #number = int(input())
    #tree.insert(number)



    
print(tree.orderedTraversal)


#create a loop for recieving user input
#recieve user input
# insert userinput into tree
# print tree when finished


# tree.insert(34)
# tree.insert(645)
# tree.insert(-45)
# tree.insert(1)
# tree.insert(34)
# tree.insert(0)

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