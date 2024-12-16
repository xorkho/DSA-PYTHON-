class BinaryTree:
    def __init__(self,item):
        self.item=item
        self.lc=None
        self.rc=None

    def addlc(self,item):
        assert self.lc is None ,"left child already exist"
        self.lc=BinaryTree(item)

    def addrc(self,item):
        assert self.rc is None ,"right child already exist"
        self.rc=BinaryTree(item)

    def dellc(self):
        assert self.lc is not None ,"Left child not exist"
        assert self.lc.lc is None and self.lc.rc is None ,"this node has childs"
        x=self.lc.item
        self.lc=None
        return x
    
    def delrc(self):
        assert self.rc is not None ,"Right child not exist"
        assert self.rc.rc is None and self.rc.lc is None ,"this node has childs"
        x=self.rc.item
        self.rc=None
        return x
    
    def height(self):
        if self.rc is None and self.lc is None:
            return 1
        lh=0
        rh=0
        if self.rc is not None:
            rh=self.rc.height()
        if self.lc is not None:
            lh=self.lc.height()
        
        if lh>rh:
            return lh+1
        return rh+1
    
    def nodecount(self):  #time o(n) space o(h)
        if self.rc is None and self.lc is None:
            return 1
        rightNode=0
        leftNode=0
        if self.rc is not None:
            rightNode=self.rc.nodecount()
        if self.lc is not None:
            leftNode=self.lc.nodecount()
        return rightNode+leftNode+1
    
    def leafcount(self):   #time 0(n) and space o(h)
        if self.rc is None and self.lc is None:
            return 1
        rlc=0    #RIGHT LEAF COUNT
        llc=0    #LEFT LEAF COUNT
        if self.rc is not None:
            rlc=self.rc.leafcount()
        if self.lc is not None:
            llc=self.lc.leafcount()
        return rlc + llc

    def isStrictlyBinary(self):
        if self.lc is None:
            if self.rc is None:
                return True
            return False
        if self.rc is None:
            return False
        return self.lc.isStrictlyBinary() and self.rc.isStrictlyBinary()
    
    def isPerfect(self): #PBT
        h = self.height()
        n = self.nodecount()  #O(n)
        m = pow(2,h) - 1
        if n==m:
            return True
        return False
    
    def isACBT(self): #almost complete binary tree
        if self.isPerfect():
            return True
        if self.lc is None:
            return False     #O(n)
        hl=self.lc.height()
        if self.rc is None:
            if hl==1:
                return True
            return False
        hr=self.rc.height()
        if hl==hr and self.lc.isPerfect():
            return self.rc.isACBT()
        if hl==hr+1 and self.rc.isPerfect():
            return self.lc.isACBT()
        return False
    
    def traverseIn(self):
        if self.lc is not None:
            self.lc.traverseIn()
        print(self.item,end="")
        if self.rc is not None:
            self.rc.traverseIn()

    def traversePre(self):
        print(self.item,end="")
        if self.lc is not None:
            self.lc.traversePre()
        if self.rc is not None:
            self.rc.traversePre()   

    def traversePost(self):
        if self.lc is not None:
            self.lc.traversePost()
        if self.rc is not None:
            self.rc.traversePost() 
        print(self.item,end="")

    def TraverseBreadthFirst(self):
        node=[self]
        print(self.item,end="")
        i=0   #indicating index
        n=1   #number of elements in nodes

        while i<n:
            current=node[i]
            if current.lc is not None:
                print(current.lc.item,end="")
                node.append(current.lc)
                n+=1

            if current.rc is not None:
                print(current.rc.item,end="")
                node.append(current.rc)
                n+=1
            i+=1
        print()
            
