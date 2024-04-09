class DictBinTree:
    def __init__(self):
        self.root = BinNode()
        #for key in keys:
            #self.root = DictBinTree.insert(self.root, key)

    def publicSearch(self, k):
        return self.privateSearch(self.root, k)
    
    def privateSearch(self, bin_node, key):
        if key < self.key:
            if self.left == None:
                return False
            else:
                self.left.search(key)
        elif key > self.key:
            if self.right == None:
                return False
            else:
                self.right.search(key)
        else:
            return True
            

    def insert(self, node):
        y = None
        x = self.root
        while x != None:
            y = x         
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        if y == None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node
        

    def orderedTraversal(self, Node, mylist):
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
    def __init__(self):
        self.left = None
        self.right = None
        self.key = None

    #skal bruges til at repræsentere knuder i træer
    #du skal ikke bruge array struktur
    #skal indeholde to andre BinNodes (knudens venstre og højre børn), med værdi None hvis barnet ikke findes.
    # skal også indeholde nøgle K, men ikke nødvendigt med forælder i dette projekt
    # 