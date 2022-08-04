#Implementing Doubly Linked List
#Created by Aswin ks


class Node:  #class for creating a node
    def __init__(self,data):
        self.data=data    #for storing data part of a singly linked dlist
        self.nref=None #next reference
        self.pref=None #previous reference

#----------------------------------------------------------------------------------------------------------------------
class doublyll:

    def __init__(self):
        self.head=None  #setting head as none at first
#----------------------------------------------------------------------------------------------------------------------

    def traversal_forward(self):

        if self.head is None:   #if head is null then its empty
            print("Linked list is Empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data,"-->",end="")
                n=n.nref

    # ----------------------------------------------------------------------------------------------------------------------
    def traversal_reverse(self):

        if self.head is None:
            print("Linked list is Empty!")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref


            while n  is not None:
                print(n.data,"-->",end="")
                n=n.pref

    # ----------------------------------------------------------------------------------------------------------------------
    def add_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.nref=self.head   #adding element in front
            self.head.pref=new_node
            self.head=new_node

    # ----------------------------------------------------------------------------------------------------------------------
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.nref is not None: #moving to last element (element having .nref as NONE
                n=n.nref
            new_node.pref=n
            n.nref=new_node
#----------------------------------------------------------------------------------------------------------------------

    def add_after(self,data,x):  #x is the data of the node after which new node need to be added.
        if self.head is None:
            print("Linked list is empty!")
        else:
            n=self.head
            while n is not  None:
                if n.data ==x:
                    break
                n=n.nref

            if n is None:
                print("Given node is not present!!")
            else:

                newnode=Node(data)
                newnode.nref=n.nref
                newnode.pref=n
                if n.nref is not None:
                    n.nref.pref=newnode
                n.nref = newnode
#----------------------------------------------------------------------------------------------------------------------

    def delete_beg(self):
        if self.head is None:
            print("linked list is empty")
            return

        if self.head.nref is None: #checking if there is only one element.if so delete that directly and set head as NONE
            self.head =None
            print("Deleted existing One Node!,Now LL is empty")
            return

        self.head = self.head.nref   #This will run if there is  more than one element
        self.head.pref=None

    # ----------------------------------------------------------------------------------------------------------------------
    def delete_end(self):
        if self.head is None:
            print("linked list is empty")
            return

        if self.head.nref is None: #checking if there is only one element.if so delete that directly and set head as NONE
            self.head = None
            print("Deleted existing One Node!,Now LL is empty")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref

            n.pref.nref=None

    # ----------------------------------------------------------------------------------------------------------------------
    def delete_by_value(self,x):
        if self.head is None:   #Run if head is NONE
            print("linked list is empty")
            return

        if self.head.nref is None:  #RUN if there is only one element in linked list
            if x==self.head.data:
                self.head=None

        else:
            pass
        if self.head.data==x:      #RUN if the element is first element
            self.head=self.head.nref
            self.head.pref=None
            return

        n=self.head    #RUN if element is  between
        while n.nref is not None:
            if n.data==x:
                break
            n=n.nref
        if n.nref is not None:
            n.nref.pref=n.pref
            n.pref.nref=n.nref
        else:

            if n.data==x:  #RUN if element is the last one!
                n.pref.nref=None
            else:
                print("Item not Found!!")  #RUN if the given element is not found in Dlinked list





dl1=doublyll() #creating object
dl1.add_begin(5)  #calling methods
dl1.add_end(200) #calling methods
#
dl1.traversal_forward()#calling methods
print("\n")
dl1.traversal_reverse()#calling methods



