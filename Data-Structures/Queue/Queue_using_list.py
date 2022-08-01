#Implementing Queue and its operation using list
#Created by Aswin


queue=[] #creating a list that will act as queue

def enqueue():  #function to enqueue or add element queues rear

    element=input("Enter the element to add: ")
    queue.append(element)
    print(queue)

def dequeue(): #function to dequeue or remove element from Queues front.ie, queue[0]

    if not queue:
        print("Queue is Empty")
    else:
        x=queue.pop(0)
        print("Element  removed is ",x)
        print(queue)


while True:  #To run this prompt continuously
    print("Enter the Queue operation: 1.enqueue 2.dequeue 3.Quit")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
            dequeue()
    elif choice==3:
        print("Quitting..")
        break
    else:
        print("Invalid choice")  #if none of the choices match


