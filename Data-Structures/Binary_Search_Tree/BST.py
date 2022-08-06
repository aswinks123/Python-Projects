#Implement Binary search Tree and Its Operations
#Created By : Aswin Ks


class BST: #class to create the Node
    def __init__(self,key):#initially setting root's values  it as None
        self.key=key
        self.lchild=None
        self.rchild=None

    #-------------------------------------------------------------------------------------------------------------------

    def insert(self,data):#Insert method
        if self.key is None: #if self.key  is none
            self.key=data #add data as root node
            return #return is to stop the method.
        if self.key==data: #if same data already exist ,then dont do anything
            return
        if self.key>data: #data adding to left tree
            if self.lchild:#means lchild present
                self.lchild.insert(data)#calling insert again to go to its last left sub tree (recurssion)
            else:
                self.lchild=BST(data)#Created new node with data and add it to lchild child.self.
        else:#data > root
            if self.rchild:  #if self.rchild is true the execute this
                self.rchild.insert(data)#calling insert again to go to its last right sub tree (recurssion)
            else:
                self.rchild=BST(data)#Created new node with data and add it to rchild child

    # ------------------------------------------------------------------------------------------------------------------

    def search(self,data): #search operation
        if self.key is None:
            print("Tree is Empty!")
            return
        if self.key==data:
            print("Node Available.!!")
            return
        if self.key>data:#seaerch in left subtree only
            if self.lchild:
                self.lchild.search(data)  #recusrion with self=self.lchild
            else:
                print("Node not Found in left subtree!")
        if self.key<data:#seaerch in right subtree only
            if self.rchild:
                self.rchild.search(data)  #recusrion with self=self.rchild
            else:
                print("Node not Found in right sub tree!")

    # ------------------------------------------------------------------------------------------------------------------

    def preorder(self): #Preorder traversal
        if self.key is None:
            print("Tree is empty")
            return
        print(self.key ," ",end="")#printing root value first as its pre order
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    # ------------------------------------------------------------------------------------------------------------------

    def inorder(self):#Inorder traversal
        if self.key is None:
            print("Tree is empty")
            return
        if self.lchild:
            self.lchild.inorder()
        print(self.key, " ", end="")
        if self.rchild:
            self.rchild.inorder()

    # ------------------------------------------------------------------------------------------------------------------

    def postorder(self):#Postorder traversal
        if self.key is None:
            print("Tree is empty")
            return
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key, " ", end="")

    # ------------------------------------------------------------------------------------------------------------------

    def delete(self,data,current):#Delete a node from tree
        if self.key is None:
            print("Tree is empty!")
            return
        if data<self.key:
            if self.lchild:
                self.lchild=self.lchild.delete(data,current)
            else:
                print("Item Not present in Tree!!")
        elif data>self.key:
            if self.rchild:
                self.rchild=self.rchild.delete(data,current)
            else:
                print("Item Not present in Tree!!")
        else: #then self.key == data.
            if self.lchild is None:
                temp=self.rchild
                if data==current:  #It will run if the node we are deleting is root
                    self.key=temp.key
                    self.lchild=temp.lchild
                    self.rchild=temp.rchild
                    temp=None
                    return
                self=None
                return temp
  

            if self.rchild is None:
                temp=self.lchild
                if data==current:  #It will run if the node we are deleting is root
                    self.key=temp.key
                    self.lchild=temp.lchild
                    self.rchild=temp.rchild
                    temp=None
                    return
                self=None
                return temp

            node=self.rchild#finding smallest node in right subtree.
            while node.lchild:
                node=node.lchild
            self.key=node.key
            self.rchild=self.rchild.delete(node.key,current)
        return self

    # ------------------------------------------------------------------------------------------------------------------

    def min_node(self):#Finding Min node in Tree
        current=self
        while current.lchild:
            current=current.lchild
        print("Min Node is: ",current.key)

    # ------------------------------------------------------------------------------------------------------------------

    def max_node(self):#Finding Max node in Tree
        current=self
        while current.rchild:
            current=current.rchild
        print("Max Node is :",current.key)
    # ------------------------------------------------------------------------------------------------------------------





#This is a function to find the total node count of BST.This count is required when deleting the root node of tree
def count(node):#finding total no of nodes of Tree.its needed for delete opeartion
    if node is None:
        return 0
    return 1+count(node.lchild)+count(node.rchild)






#execution begin here...

root=BST(10) #it create a "root" object with  none data .its  for that init function to execute and ser default value.


lst=[20,30,5,2,100,1]  #Adding some elements to BST
for i in lst:
     root.insert(i)

if count(root)>1:#Delete Operation
    root.delete(30,root.key)
else:
    print("Cant delete root")


root.min_node() #Find Min Node
root.max_node() #Find Max Node
root.inorder()  #calling method

