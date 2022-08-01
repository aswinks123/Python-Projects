#Creating a linked list and implement its operations
#Created by Aswin ks

#creating a node,add data, and point its reference to null

class Node:
    def __init__(self,data):
        self.data=data    #for storing data part of a singly linked dlist
        self.ref=None     #for storing ref part of a singly linked list

#------------------------------------------------------------------------------------------------------------------------------------


class LinkedList:
    def __init__(self):
        self.head=None   #Initially Assign head as None to indicate that it is an empty linkedlist

    def print(self): #Traverse function
        if self.head is None: #checking whether linked list in empty
            print("Linked list is Empty!")
        else:
            n=self.head   #n=First node
            while n is not None: #Do this until n==None
                print(n.data,"->",end="")   #n.data is the data of first node
                n=n.ref   #Go to next node.because n.ref has address of next node

    # ------------------------------------------------------------------------------------------------------------------------------------


    def add_begin(self,data): #function to add node at begining.

        new_node=Node(data)
        new_node.ref=self.head #Now head ref is added to new nodes ref to it can connect to previous head node.
        self.head=new_node #Now change head to new node.
 # ------------------------------------------------------------------------------------------------------------------------------------

    def add_end(self,data):
        new_node=Node(data) #Creating a new node from Node class

        if self.head is None: #if head is None the new node is the first element.so directly assign it
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:  #iterate till self.head or n is None
                n=n.ref  #moving forward
            n.ref=new_node  #finally assign new node to the n.ref

    # ------------------------------------------------------------------------------------------------------------------------------------


    def add_after(self,data,x): #x is the data field value after which we want to add the node
        n=self.head

        while n is not None:  #iterate till self.head is None
            if x==n.data:  #if x ==n.data then we found the position
                break
            else:
                n=n.ref #if x!=n.data then move forward
        if n is None:   #if n is None then it means item is not present
            print("mentioned Item is not present!!")
        if n is not None: #if n is not None then we will add the element after n
            new_node=Node(data)  #creating new node
            new_node.ref=n.ref  # pointing newnode.ref to n.ref(previous node)
            n.ref=new_node     #Now change n.ref(prev nodes reference) to new node

    # ------------------------------------------------------------------------------------------------------------------------------------


    def add_before(self,data,x):
        if self.head==None: #checking whether ll is empty
            print("Linked list is Empty")
            return

        if self.head.data==x:   #then give same code as add_begin()
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return


        n = self.head

        while n.ref is not None:  # iterate till n.ref is None
            if x == n.ref.data:  # if x ==n.data then we found the position
                break
            else:
                n = n.ref
        if n.ref is None:
            print("Node not Found!")
        else:  #same as after
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node

# ------------------------------------------------------------------------------------------------------------------------------------


    def del_beg(self):
        if self.head is None: #checking whether linked list is empty
            print("Linked list is Empty!")
        else:
            self.head=self.head.ref  #changing head to  second item in the linked list
# ------------------------------------------------------------------------------------------------------------------------------------

    def del_end(self):
        if self.head is None: #checking whether linked list is empty
            print("Linked list is Empty!")
        elif self.head.ref is None:
            self.head=None
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None
# ------------------------------------------------------------------------------------------------------------------------------------

    def del_by_value(self,x): #x is the value of node to delete
        if self.head is None:
            print("Linked List is Empty")
            return
        if x==self.head.data: #checking whether x is  first node.
            self.head=self.head.ref
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n=n.ref

        if n.ref is None:
            print("Not Found")
        else:
            n.ref=n.ref.ref




ll1=LinkedList()  #creating an object to do all the operation

print("Choose an Operation")

while True:

    c = int(input("\n0. Traverse, 1.Add to Begining, 2.Add to End, 3.Add after a particular value, 4.Add before a particular value\n5.Delete from begining, 6.Delete from End, 7.Delete a particular value, 8.Quit\n"))

    if c==0:
        ll1.print()
    elif c==1:
        ll1.add_begin(input("Enter the Element to add: "))
    elif c==2:
        ll1.add_end(input("Enter the Element to add: "))
    elif c==3:
        val=input("Enter the data to add: ")
        pos=int(input("After which value you want to add this?: "))
        ll1.add_after(val,pos)
    elif c==4:
        val = input("Enter the data to add: ")
        pos = int(input("Before which value you want to add this?: "))
        ll1.add_before(val,pos)
    elif c==5:
        ll1.del_beg()
        print("Deleted")
    elif c==6:
        ll1.del_end()
        print("Deleted")
    elif c==7:
        pos=input("Enter the value to delete")
        ll1.del_by_value(pos)
        print("Deleted")

    elif c==8:
        print("Quitting...!")
        exit()
    else:
        print("Invalid Choice!")













