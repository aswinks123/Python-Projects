#Implementing stack and its operation using list
#Created by Aswin

l=int(input("Enter the length of stack"))  #Asking for stack length if required.(Optional)
stack=[] #creating a list that will act as stack

def push():  #function to push or add element to top
    if len(stack)<l:
        element=input("Enter the element to add: ")
        stack.append(element)
        print(stack)
    else:
        print("Stack overflow")

def pop(): #function to pop or remove element from stack
    if len(stack)<=0:
        print("Stack underflow")
    else:
        x=stack.pop()
        print("Element  removed is ",x)
        print(stack)


while True:  #To run this prompt continuously
    print("Enter the stack operation: 1.PUSH 2.POP 3.Quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
            pop()
    elif choice==3:
        print("Quitting..")
        break
    else:
        print("Invalid choice")  #if none of the choices match


